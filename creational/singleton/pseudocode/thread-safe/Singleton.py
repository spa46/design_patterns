from SingletonMeta import SingletonMeta

class Singleton(metaclass=SingletonMeta):
  value: str = None

  def __init__(self, value: str) ->None:
    self.value = value

  def go(self):
      print('go')