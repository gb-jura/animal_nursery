from dataclasses import dataclass
from animal import Animal

@dataclass
class Pet(Animal):
    owner_name: str
