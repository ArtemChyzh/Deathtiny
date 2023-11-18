from abc import ABC
from Base.object import Object
from interfaces.iattack import IAttack
from interfaces.imove import IMove
from interfaces.ihealth import IHealth


class Enemy(Object, IAttack, IMove, IHealth, ABC):
    pass
