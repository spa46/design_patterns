from __future__ import annotations
from abc import ABC, abstractmethod

from Table import Table

class ModernTable(Table):
  
  def say_hello(self):
    print('Hello, I am Modern Table!')

  def say_table(self):
    print('Extra Feature: Say Modern Table!')