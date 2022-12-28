from __future__ import annotations
from abc import ABC, abstractmethod

class Logistics(ABC):

  @abstractmethod
  def planDelivery(self):
    pass

  def createTransport(self):
    transport = self.planDelivery()
    transport.deliver()

    return transport