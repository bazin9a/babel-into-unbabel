import logging


# TODO: share context to use among repo and tests helper
def init_logger():
    logging.basicConfig()
    return logging.getLogger(__name__)
