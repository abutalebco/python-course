import logging

logging.basicConfig(level=logging.DEBUG)

logger = logging.getLogger("RAM Manager Logger")
logger.setLevel(logging.DEBUG) # hierarchy inheritance

handler = logging.FileHandler("logging/mylog.log")
handler.setLevel(logging.INFO)

formatter = logging.Formatter("%(levelname)s - %(asctime)s: %(message)s")
handler.setFormatter(formatter)

logger.addHandler(handler)

logger.info("Start the Program!")
logger.log(logging.ERROR, "An error occured!")