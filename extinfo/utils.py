from dataclasses import dataclass


@dataclass
class Report:
    description_short: str
    description_long: str
    how_to_open: str
