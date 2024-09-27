# -*- coding=utf-8 -*-

from abc import ABC, abstractmethod
from dataclasses import dataclass


@dataclass
class Filter(ABC):
    name: str = ""

    @abstractmethod
    def signal(self, *args):
        pass

    @abstractmethod
    def get_parameter(self):
        pass
