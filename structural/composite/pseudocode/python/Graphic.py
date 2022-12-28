from __future__ import annotations
from abc import ABC, abstractmethod
from typing import List

class Graphic(ABC):

  @abstractmethod
  def move(x, y):
    pass

  @abstractmethod
  def draw():
    pass
