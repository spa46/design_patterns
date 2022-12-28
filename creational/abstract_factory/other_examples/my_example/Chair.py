from __future__ import annotations
from abc import ABC, abstractmethod

class Chair(ABC):

  @abstractmethod
  def say_hello(self):
    pass