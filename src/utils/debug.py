# /src/utils/debug.py
import gc
import tracemalloc
import logging
from functools import wraps
import time

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

def memory_tracker(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        tracemalloc.start()
        start_time = time.time()
        
        try:
            result = func(*args, **kwargs)
            
            # Get memory statistics
            current, peak = tracemalloc.get_traced_memory()
            logger.debug(f'Function: {func.__name__}')
            logger.debug(f'Memory current: {current / 10**6:.2f}MB')
            logger.debug(f'Memory peak: {peak / 10**6:.2f}MB')
            logger.debug(f'Time elapsed: {time.time() - start_time:.2f} seconds')
            
            # Get top memory allocations
            snapshot = tracemalloc.take_snapshot()
            top_stats = snapshot.statistics('lineno')
            logger.debug("Top 5 memory allocations:")
            for stat in top_stats[:5]:
                logger.debug(stat)
                
            return result
            
        finally:
            tracemalloc.stop()
            gc.collect()
    
    return wrapper

def monitor_fps():
    """FPS monitoring context manager"""
    class FPSMonitor:
        def __init__(self):
            self.start_time = None
            self.frame_count = 0
            
        def __enter__(self):
            self.start_time = time.time()
            return self
            
        def increment(self):
            self.frame_count += 1
            
        def __exit__(self, exc_type, exc_val, exc_tb):
            duration = time.time() - self.start_time
            fps = self.frame_count / duration
            logger.debug(f'Average FPS: {fps:.2f}')
    
    return FPSMonitor()