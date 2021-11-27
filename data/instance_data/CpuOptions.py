from marshmallow_dataclass import dataclass


@dataclass
class CpuOptions:
    CoreCount: int
    ThreadsPerCore: int
    