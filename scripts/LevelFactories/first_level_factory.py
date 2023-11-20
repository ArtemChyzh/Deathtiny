from scripts.abstract.level_factory import AbstractLevelFactory
from scripts.LevelStrategies.first_level_strategy import FirstLevelStrategy


class FirstLevel(AbstractLevelFactory):
    def __init__(self):
        super().__init__(strategy=FirstLevelStrategy())
