from redis.asyncio import Redis
import json
import structlog
from typing import List, Optional
from app.models.worker import WorkTask

logger = structlog.get_logger()

class WorkerQueue:
    def __init__(self, redis: Redis):
        self.redis = redis

    def _get_queue_key(self, platform: str, priority: int) -> str:
        return f"queue:{platform}:p{priority}"

    def _get_processing_key(self, worker_id: str) -> str:
        return f"processing:{worker_id}"

    async def push_task(self, task: WorkTask):
        key = self._get_queue_key(task.platform, task.priority)
        await self.redis.lpush(key, task.model_dump_json())
        logger.info("task_pushed", task_id=task.task_id, platform=task.platform)

    async def pop_tasks(self, worker_id: str, platforms: List[str], capacity: int) -> List[WorkTask]:
        tasks = []
        # Try platforms in order
        for platform in platforms:
            if len(tasks) >= capacity:
                break
                
            # Try priorities from 1 (urgent) to 4 (low)
            for priority in range(1, 5):
                if len(tasks) >= capacity:
                    break
                    
                queue_key = self._get_queue_key(platform, priority)
                processing_key = self._get_processing_key(worker_id)
                
                # Reliable queue pattern: RPOPLPUSH
                raw_task = await self.redis.rpoplpush(queue_key, processing_key)
                if raw_task:
                    task_data = json.loads(raw_task)
                    tasks.append(WorkTask(**task_data))
                    logger.info("task_popped", worker_id=worker_id, task_id=task_data["task_id"])
                    
        return tasks

    async def complete_task(self, worker_id: str, task_id: str):
        # In a real implementation, we'd need to find the specific task in the processing list
        # For simplicity in MVP, we'll assume the processing list is short
        processing_key = self._get_processing_key(worker_id)
        # This is a bit naive but works for the MVP logic
        tasks = await self.redis.lrange(processing_key, 0, -1)
        for raw_task in tasks:
            task_data = json.loads(raw_task)
            if task_data["task_id"] == task_id:
                await self.redis.lrem(processing_key, 1, raw_task)
                logger.info("task_completed", worker_id=worker_id, task_id=task_id)
                return True
        return False
