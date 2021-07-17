import yaml
from pathlib import Path


class HeatSeekerConfig:

    def __init__(self, config_path: Path) -> None:
        self.config_path = config_path
        self.config = yaml.safe_load(self.config_path.open())

    @property
    def auto_index(self) -> bool:
        try:
            return self.config['auto_index']
        except KeyError:
            return False


