from utilities.loaddatafiles import LoadDataFiles
from functools import wraps
import warnings
import traceback
from datetime import datetime
from utilities.logger import Logger

def log_function(logger):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            func_name = func.__qualname__
            logger.info(f"Entering: {func_name}")
            logger.debug(f"Args: {args}, Kwargs: {kwargs}")

            with warnings.catch_warnings(record=True) as caught_warnings:
                warnings.simplefilter("always")
                try:
                    result = func(*args, **kwargs)

                    for warn in caught_warnings:
                        logger.warning(f"Warning in {func_name}: {str(warn.message)}")

                    logger.info(f"Exiting: {func_name} with result: {result}")
                    return result
                except Exception as e:
                    logger.error(f"Exception in {func_name}: {e}")
                    full_traceback = "".join(traceback.format_exception(type(e), e, e.__traceback__))
                    logger.error("Traceback:\n" + full_traceback)
                    raise

        return wrapper
    return decorator

yaml_file_contents = LoadDataFiles().load_yaml_file(r"tests/config/userconfig.yaml")
logger : Logger = Logger(f"logger_{datetime.now().strftime("%Y_%m_%d_%H_%M_%S")}")

