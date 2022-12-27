from abc import ABCMeta, abstractmethod

class SubjectInterface(metaclass=ABCMeta):
    @abstractmethod
    def request(self, url):
        pass

class RealSubject(SubjectInterface):
    def request(self, url):
        # Implementation
        return url.upper()

    @staticmethod
    def has_url(url):
        return url == ''

class ProxyClass(SubjectInterface):
    def request(self, url):
        if RealSubject.has_url(url):
            return RealSubject().request(url)
