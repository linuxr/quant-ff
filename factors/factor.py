# -*- coding=utf-8 -*-

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import pandas as pd


@dataclass
class Factor(ABC):
    name: str = ""
    params: list = field(default_factory=lambda: [])

    @abstractmethod
    def signal(self, data: pd.DataFrame, para: list = []):
        pass

    def get_parameters(self):
        if len(self.params) > 0:
            return self.params

        if self.name.upper() in ["ADOSC"]:
            return [[3, 21], [5, 34], [8, 55], [13, 89]]

        return [[3], [5], [8], [13], [21], [34], [55], [89]]

    def set_parameters(self, params: list):
        self.params = params
