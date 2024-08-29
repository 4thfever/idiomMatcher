import functools

from logger import logger

def log_func_info(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 记录函数名字和参数
        args_str = ', '.join(f'{a}' for a in args)
        kwargs_str = ', '.join(f'{k}={v}' for k, v in kwargs.items())
        all_args = ', '.join(filter(None, [args_str, kwargs_str]))
        logger.info(f"Calling {func.__name__}({all_args})")
        
        # 执行函数
        result = func(*args, **kwargs)
        
        # 记录返回值
        logger.info(f"{func.__name__} returned {result}")
        return result
    
    return wrapper

def retry_when_error(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        for i in range(3):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(f"Error: {e}")
                logger.error(f"Error: {e}")
        return "Error after 3 retries"
    
    return wrapper  
