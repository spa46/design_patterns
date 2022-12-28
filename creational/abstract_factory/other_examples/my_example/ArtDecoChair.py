from __future__ import annotations
from abc import ABC, abstractmethod

from Chair import Chair

class ArtDecoChair(Chair):
  def say_hello(self):
    print('Hello, I am Art Deco Chair!')