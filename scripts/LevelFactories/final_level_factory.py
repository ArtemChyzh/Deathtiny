from scripts.abstract.level_factory import AbstractLevelFactory
from scripts.LevelStrategies.final_level_strategy import FinalLevelStrategy


class FinalLevel(AbstractLevelFactory):
    def __init__(self):
        super().__init__(strategy=FinalLevelStrategy())
