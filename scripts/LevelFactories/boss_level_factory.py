from scripts.LevelStrategies.boss_level_strategy import BossLevelStrategy
from scripts.abstract.level_factory import AbstractLevelFactory


class BossLevel(AbstractLevelFactory):
    def __init__(self):
        super().__init__(strategy=BossLevelStrategy())