from __future__ import annotations
from Dot import Dot

class Circle(Dot):
  def __init__(self, x, y, radius):
    self.x = x
    self.y = y
    self.radius =radius

  def move(self, x, y):
    self.x += x
    self.y += y

  def draw(self):
    print(f'drawing x:{self.x}, y:{self.y}, radius:{self.radius}')