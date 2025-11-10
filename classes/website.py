from digitalAsset import DigitalAsset
from reportable import Reportable

class Website(DigitalAsset, Reportable):

    def __init__(self, name, registration_date, cost, monthly_traffic : int, monetization_rate : float):
        super().__init__(name, registration_date, cost)
        self.monthly_traffic = monthly_traffic
        self.monetization_rate =monetization_rate


    def asset_type(self):
        return "WEBSITE"

    def calculate_value(self):
        value = self.monthly_traffic * self.monetization_rate * 12
        return value

    def to_report_line(self):
        return f"name: {self.get_name}, registration date: {self.get_registration_date}, cost: {self.get_cost}, monthly traffic: {self.monthly_traffic}, monetization rate: {self.monetization_rate}, value: {self.calculate_value()}"