from Factory import Factory
from ModernFurniture import ModernFurniture
from ArtDecoFurniture import ArtDecoFurniture
from VictorianFurniture import VictorianFurniture


def create_products(factory: Factory):
  chair = factory.create_product_chair()
  sofa = factory.create_product_sofa()
  table = factory.create_product_table()
  print('----------')
  chair.say_hello()
  sofa.say_hello()
  table.say_table()
  print('----------')

if __name__ == '__main__':
  create_products(ArtDecoFurniture())  
  print('===================================')
  create_products(ModernFurniture())
  print('===================================')
  create_products(VictorianFurniture())  