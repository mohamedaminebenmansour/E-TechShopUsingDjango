import logging
logger = logging.getLogger(__name__)

def debug_pipeline(backend, response, *args, **kwargs):
    logger.info(f"GitHub Response: {response}")
