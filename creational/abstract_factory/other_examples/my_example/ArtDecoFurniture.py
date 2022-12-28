from __future__ import annotations
from abc import ABC, abstractmethod

from ArtDecoChair import ArtDecoChair
from ArtDecoSofa import ArtDecoSofa
from ArtDecoTable import ArtDecoTable

class ArtDecoFurniture(ABC):

  def create_product_chair(self):
    return ArtDecoChair()

  def create_product_sofa(self):
    return ArtDecoSofa()

  def create_product_table(self):
    return ArtDecoTable()