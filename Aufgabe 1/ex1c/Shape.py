from abc import ABC,abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def get_area(self):
        pass