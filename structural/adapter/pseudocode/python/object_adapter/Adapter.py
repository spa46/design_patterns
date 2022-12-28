from Service import Service

from Target import Target

class Adapter(Target):
  def __init__(self, service: Service) -> None:
    self.service = service

  def request(self) -> str:
    return self.service.specific_request() + ", This is ADAPTER!!"