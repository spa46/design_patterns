from __future__ import annotations
from abc import ABC, abstractmethod


class DataSource():
  @abstractmethod
  def writeData(data):
    pass

  @abstractmethod
  def readData():
    pass

