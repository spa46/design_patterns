from threading import Thread

from Singleton import Singleton 


def test_singleton(value: str) -> None:
  singleton = Singleton(value)
  print(singleton.value)

if __name__ == '__main__':
  p1 = Thread(target=test_singleton, args=('FOO',))
  p2 = Thread(target=test_singleton, args=('BAR',))
  p1.start()
  p2.start()