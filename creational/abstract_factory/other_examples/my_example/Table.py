from __future__ import annotations
from abc import ABC, abstractmethod

class Table(ABC):

  @abstractmethod
  def say_hello(self):
    pass

  @abstractmethod
  def say_table(self):
    pass