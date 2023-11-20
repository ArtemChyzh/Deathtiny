from scripts.LevelStrategies.simple_level_strategy import SimpleLevelStrategy
from scripts.abstract.level_factory import AbstractLevelFactory


class SimpleLevel(AbstractLevelFactory):
    def __init__(self):
        super().__init__(strategy=SimpleLevelStrategy())
