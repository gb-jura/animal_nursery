from dataclasses import dataclass
from animal import Animal

@dataclass
class BeastOfBurden(Animal):
    carrying_capacity: int
