from __future__ import annotations

from Graphic import Graphic

class Dot(Graphic):
  def __init__(self, x, y):
    self.x = x
    self.y = y

  def move(self, x, y):
    self.x += x
    self.y += y

  def draw(self):
    print(f'drawing x:{self.x}, y:{self.y}')