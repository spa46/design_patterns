from abc import ABCMeta, abstractmethod
from typing import List

class Video:
    pass

class Observer(metaclass=ABCMeta):
    @abstractmethod
    def update(self, video: Video):
        pass

class SubscriberA(Observer):
    def update(self, video: Video):
        print('SubscriberA Notifications')

class SubscriberB(Observer):
    def update(self, video: Video):
        print('SubscriberB Notifications')

class SubscriberC(Observer):
    def update(self, video: Video):
        print('SubscriberC Notifications')

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
        self.video = None

    def attach(self, observer: Observer):
        self.observers.append(observer)

    def detach(self, observer: Observer):
        self.observers.remove(observer)

    def notify(self):
        for observer in self.observers:
            observer.update(self.video)

    def new_video(self, video: Video):
        self.video = video
        self.notify()
