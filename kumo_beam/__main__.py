import logging

from . import run, Options


if __name__ == "__main__":
    logging.getLogger().setLevel(logging.INFO)
    run(options=Options())
