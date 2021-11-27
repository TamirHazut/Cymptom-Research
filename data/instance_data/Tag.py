from marshmallow_dataclass import dataclass


@dataclass
class Tag:
    Key: str
    Value: str = ''
