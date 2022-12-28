from Service import Service

from Target import Target

class Adapter(Target, Service):
  def request(self) -> str:
    return self.specific_request() + ", This is ADAPTER!!"