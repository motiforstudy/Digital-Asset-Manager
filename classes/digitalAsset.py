from abc import ABC, abstractmethod


class DigitalAsset(ABC):

    def __init__(self, name, registration_date, cost):
        self.__name = name
        self.__registration_date = registration_date
        self.__cost = cost
    @property
    def get_information(self):
        return self.__name, self.__cost, self.__registration_date

    @get_information.getter
    def get_name(self):
        return self.__name

    @get_information.getter
    def get_registration_date(self):
        return self.__registration_date

    @get_information.getter
    def get_cost(self):
        return self.__cost

    @abstractmethod
    def calculate_value(self):
        return self.get_cost()

    @abstractmethod
    def asset_type(self):
        return self.get_name()