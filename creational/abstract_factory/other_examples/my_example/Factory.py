from __future__ import annotations
from abc import ABC, abstractmethod


class Factory(ABC):
  @abstractmethod
  def create_product_chair(self):
    pass


  @abstractmethod
  def create_product_sofa(self):
    pass


  @abstractmethod
  def create_product_table(self):
    pass