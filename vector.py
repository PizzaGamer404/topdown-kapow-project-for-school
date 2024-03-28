from typing import Union
from dataclasses import dataclass

# He's commiting crime, with both DIRECTIONS ... AND MAGNITUDE!! OH YEAH!
@dataclass
class Vector:
    def __init__(self, x: float, y: float):
        self.x: float = x
        self.y: float = y
    
    def __add__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other: 'Vector') -> 'Vector':
        return Vector(self.x - other.x, self.y - other.y)

    def __neg__(self):
        return Vector(-self.x, -self.y)
    
    def __mul__(self, scalar: Union[float, 'Vector']) -> 'Vector':
        if isinstance(scalar, Vector):
            return Vector(self.x * scalar.x, self.y * scalar.y)
        return Vector(self.x * scalar, self.y * scalar)
    
    def __eq__(self, other: 'Vector') -> bool:
        return self.x == other.x and self.y == other.y
    
    def normalize(self) -> 'Vector':
        magnitude = (self.x ** 2 + self.y ** 2) ** 0.5
        return Vector(self.x / magnitude, self.y / magnitude)
    
    @property
    def magnitude(self) -> float:
        return (self.x ** 2 + self.y ** 2) ** 0.5
    
    def __str__(self) -> str:
        return f"({self.x}, {self.y})"
    
    def __getitem__(self, index: int) -> float:
        if index == 0:
            return self.x
        if index == 1:
            return self.y
        raise IndexError("Index out of range")
    
    def __setitem__(self, index: int, value: float):
        if index == 0:
            self.x = value
        if index == 1:
            self.y = value
        raise IndexError("Index out of range")

    def to_tuple(self) -> tuple[float, float]:
        return self.x, self.y
    
    def move_towards(self, target: 'Vector', amount: float):
        offset = target - self
        distance = offset.magnitude
        if distance <= amount:
            return target
        proportion = amount / distance
        return self * (1-proportion) + target * (proportion)

def lerp(a: Vector, b: Vector, t: float) -> float:
    return a * (1-t) + b * t

def dot(a: Vector, b: Vector):
    return a.x * b.x + a.y * b.y