from __future__ import annotations
from abc import ABC, abstractmethod

class Sofa(ABC):

  @abstractmethod
  def say_hello(self):
    pass