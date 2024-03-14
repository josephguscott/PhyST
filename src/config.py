import yaml

from log import LOG

class Config:
    def __init__(self, config_path) -> None:
        try:
            with open(config_path) as config_file:
                self.config = yaml.safe_load(config_file)
        except IOError as err:
            LOG.critical(f'{type(err).__name__}: {err}')
            exit(1)