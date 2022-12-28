from __future__ import annotations
from abc import ABC, abstractmethod

from ModernChair import ModernChair
from ModernSofa import ModernSofa
from ModernTable import ModernTable


class ModernFurniture(ABC):
  def create_product_chair(self):
    return ModernChair()

  def create_product_sofa(self):
    return ModernSofa()

  def create_product_table(self):
    return ModernTable()