from __future__ import annotations
from abc import ABC, abstractmethod

from VictorianChair import VictorianChair
from VictorianSofa import VictorianSofa
from VictorianTable import VictorianTable

class VictorianFurniture(ABC):

  def create_product_chair(self):
    return VictorianChair()

  def create_product_sofa(self):
    return VictorianSofa()

  def create_product_table(self):
    return VictorianTable()