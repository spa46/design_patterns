from Graphic import Graphic

class CompoundGraphic(Graphic):
  def __init__(self) -> None:
    self._children: List[Graphic] = []

  def add(self, child: Graphic) -> None:
    self._children.append(child)
    Graphic.parent = self

  def remove(self, child: Graphic) -> None:
    self._children.remove(child)
    Graphic.parent = None

  def is_composite(self) -> bool:
    return True

  def move(self, x, y):
    for _child in self._children:
      _child.move(x, y)
  
  def draw(self):
    for _child in self._children:
      _child.draw()