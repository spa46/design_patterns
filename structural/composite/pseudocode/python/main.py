from CompoundGraphic import CompoundGraphic
from Dot import Dot
from Circle import Circle
from Graphic import Graphic


def move(graphic: Graphic):
    graphic.move()

def draw(graphic: Graphic):
    graphic.draw()

if __name__ == "__main__":
    dot1 = Dot(1, 2)
    dot2 = Dot(-2, -1)
    # print('create dot')
    # draw(dot)

    circle = Circle(5, 3, 10)
    # print("create circle component")
    # draw(circle)
  
    # print('create compound graphic')
    all = CompoundGraphic()
    all.add(dot1)
    all.add(dot2)
    all.add(circle)
    # print('add all elements done...')

    all.move(1,1)

    print('draw all')
    all.draw()
    