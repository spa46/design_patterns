from __future__ import annotations
from abc import ABC, abstractmethod

from Table import Table

class VictorianTable(Table):
  
  def say_hello(self):
    print('Hello, I am Victorian Table!')
  def say_table(self):
    print('Extra Feature: Say Victorian Table!')