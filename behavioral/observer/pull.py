from abc import ABCMeta, abstractmethod
from typing import List

class Video:
    pass

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, subject: Subject):
        pass

class SubscriberA(Observer):
    def update(self, subject: Subject):
        print('SubscriberA Notifications')
        if isinstance(subject, Youtube):
            print(subject.video)

# B, C have same implementations

class Subject(metaclass=ABCMeta):
    @abstractmethod
    def attach(self, observer: Observer):
        pass

    @abstractmethod
    def detach(self, observer: Observer):
        pass

    @abstractmethod
    def notify(self):
        pass

class Youtube(Subject):
    def __init__(self, observers: List[Observer]):
        self.observers = observers
        self._video = None

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self)

    def new_video(self, video: Video):
        self._video = video
        self.notify()

    @property
    def video(self):
        return self._video
