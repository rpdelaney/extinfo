# type: ignore[attr-defined]
from types import ModuleType


class Extractor:
    def __init__(self, extractor_module: ModuleType) -> None:
        self.extract = extractor_module.extract
        self.site = extractor_module.SITE
