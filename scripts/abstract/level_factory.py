from scripts.level import Level
from scripts.abstract.generation_strategy import GenerationStrategy


class AbstractLevelFactory:
    counter: int = 0

    def __init__(self, strategy: GenerationStrategy):
        self.strategy = strategy

    def create(self, is_open=False) -> Level:
        level = self.strategy.create(is_open)
        level.img_path = f"../rooms/{AbstractLevelFactory.counter}.png"
        AbstractLevelFactory.counter += 1
        return level
