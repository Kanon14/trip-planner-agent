from tripPlanner.logger import logging
from tripPlanner.exception import AppException
import sys

try:
    logging.info("trying the exception class")
    a = 3 / "d"

except Exception as e:
    raise AppException(e, sys)
    