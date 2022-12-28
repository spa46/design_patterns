from __future__ import annotations
from abc import ABC, abstractmethod

from Table import Table

class ArtDecoTable(Table):
  def say_hello(self):
    print('Hello, I am Art Deco Table!')

  def say_table(self):
    print('Extra Feature: Say Deco Table!')
  