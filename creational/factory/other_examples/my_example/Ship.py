from __future__ import annotations
from Transport import Transport

class Ship(Transport):
  
  def deliver(self):
    print('delivered by ship')