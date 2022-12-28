from SingletonMeta import SingletonMeta

class Singleton(metaclass=SingletonMeta):
    def go(self):
      print('go')