from abc import ABCMeta, abstractmethod

class AirportMixin(metaclass=ABCMeta):
    def check(self):
        self.check_baggage()
        self.check_passport()
        self.check_ticket()
        self.check_flight()
        self.check_airport_location()

    def check_baggage(self):
        print("check baggage")

    def check_passport(self):
        print('check passport')

    def check_ticket(self):
        print('check ticket')

    def check_flight(self):
        print('check flight')

    @abstractmethod
    def check_airport_location(self):
        pass

class IncheonAirport(AirportMixin):
    def check_airport_location(self):
        print('check departure: Incheon')

class GimpoAirport(AirportMixin):
    def check_airport_location(self):
        print('check departure: Gimpo')
