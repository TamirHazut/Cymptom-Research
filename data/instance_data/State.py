from marshmallow_dataclass import dataclass


@dataclass
class State:
    Code: int
    Name: str
