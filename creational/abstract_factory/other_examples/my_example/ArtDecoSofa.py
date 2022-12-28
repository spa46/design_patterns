from __future__ import annotations
from abc import ABC, abstractmethod

from Sofa import Sofa

class ArtDecoSofa(Sofa):
  def say_hello(self):
    print('Hello, I am Art Deco Sofa!')