# -*- coding=utf-8 -*-

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Factor(ABC):
    name: str = ""

    @abstractmethod
    def signal(self, *args):
        pass

    @abstractmethod
    def get_parameter(self):
        pass

    def get_factor(self):
        pass
