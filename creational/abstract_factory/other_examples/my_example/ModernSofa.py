from __future__ import annotations
from abc import ABC, abstractmethod

from Sofa import Sofa

class ModernSofa(Sofa):
  def say_hello(self):
    print('Hello, I am Modern Sofa!')