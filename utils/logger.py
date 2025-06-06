import logging

def get_logger(name=None):
    logger = logging.getLogger(name or "project")
    if not logger.handlers:  # fallback if Django logging not yet set
        handler = logging.StreamHandler()
        formatter = logging.Formatter('[%(levelname)s] %(asctime)s %(name)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.setLevel(logging.DEBUG)
    return logger