from Target import Target
from Service import Service
from Adapter import Adapter

def request(target: Target) -> None:
  print(target.request())


if __name__ == '__main__':
  target = Target()
  request(target)
  print('------')
  service = Service()
  print(service.specific_request())
  print('------')
  adapter = Adapter()
  request(adapter)