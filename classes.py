import abc
import json
import random
# from flask import request

class SmartMonitoringSystem:
    def __init__(self, user, password):
        self.user = user
        self.password = password
        print(f"Starting system for user {self.user}...")

    def menu(self):
        return ("You opened field where there will be a menu...")

    def change_settings(self):
        return("Which setting do you want to change?")

    def default_settings(self):
        return("Settings changed to default")

    def control(self):
        return("YOU SHALL NOT PASS")

    def add_thing(self):
        return("What do you want to add?")

    def delete_thing(self):
        return ("What thing do you want to delete?")

    def add_user(self):
        return("Write info about new user")

    def delete_user(self):
        return ("Who are we removing from a data pill?")

    def get_status_info(self):
        return("status info....d.asads.ds.a.da")

    def emulation(self):
        self.password = str(random.randint(0, 100)) + "razamassaraksh"
        print(f'Connection succesfull. New password: {self.password}')
        return json.dumps({"password_state":self.password})

    def change_password(self, request):
        self.password = request.args.get('password_state', '')
        print(f"Connection (change pass) for user {self.user} success, NEW PASSWORD is '{self.password}'")
        return json.dumps({"password":"password is changed"})

class LifeQuality:

    def __init__(self, name, air_humidity = 50, temp = 20, brightness = 40):
        self.name_room = name
        self.power = "on"
        print(f"For room {self.name_room} mean values of parameters are: air humidity: {air_humidity}, temperature: {temp}, brightness: {brightness}")

    def get_humidity(self, curr_humidity):
        self.air_humidity = curr_humidity
        return f"Air humidity is: {self.air_humidity}"

    def get_temperature(self, curr_temp):
        self.temp = curr_temp
        return f"Temperature is: {self.temp}"

    def get_brightness(self, curr_brightness):
        self.brightness = curr_brightness
        return f"Level of brightness is: {self.brightness}"

    def emulation(self):
        self.temp = random.randint(15, 35)
        print(f'Connection successfull. New temp: {self.temp}')
        return json.dumps({"temp_state":self.temp})

    def change_temp(self, request):  # For 4s LAB
        self.temp = request.args.get('temp_state', '')
        print(f"Temperature for {self.name_room} was changed successfull! New temp '{self.temp}'")
        return json.dumps({"temp":f"Temp is changed to {self.temp}"})



class Item(abc.ABC):

    def __init__(self, name):
        self.name = name
        print(f"Item {self.name} is created")

    @abc.abstractmethod
    def connect(self, *args):
        print("Connection started")

class PersonalHealthcare(Item):

    def __init__(self, name,  pulse = 90, sleep_time = 8, activity = 10000):
        super().__init__(name)
        print(f"Your trackers say that you need {sleep_time} hours of sleep, {activity} in a day and pulse around {pulse} times per minute")

    def get_current_pulse(self, curr_pulse):
        self.pulse = curr_pulse
        return f"Your pulse is: {self.pulse}"

    def get_sleep_info(self, todays_sleep_time):
        self.sleep_time = todays_sleep_time
        return f"You slept for: {self.sleep_time} hours today"

    def get_current_activity(self, curr_activity):
        self.activity = curr_activity
        return f"Your current activity is: {self.activity}"

    def connect(self, request):
        super().connect()
        self.sleep_time = request.args.get("sleep_time", '')
        print(f"Connection to {self.name} success, new sleep_time is '{self.sleep_time}'")
        return json.dumps({'time':f"New sleep time is {self.sleep_time}"})

    def emulation(self):
        self.sleep_time = random.randint(2, 5)

class Fridge(Item):

    def __init__(self, name, curr_full_state = 50):
        super().__init__(name)
        self.full_state = curr_full_state
        self.unit = "%"
        print(f"Fridge {self.name} is created, indication is {self.full_state} {self.unit}")

    def get_current_fridge_count(self, curr_full_state):
        self.full_state = curr_full_state
        return(f"Fridge {self.name} current fullness is {self.value} {self.unit}")

    def connect(self, request):
        self.full_state = request.args.get("fridge_full_state", '')
        print(f"Connection to {self.name} is success, new fridge full state is {self.full_state}")
        return json.dumps({"full_state":f"Full state fridge was changed to {self.full_state}"})

    def emulation(self):
        self.value = round(random.random(), 2)

class CoffeeMachine(Item):

    def __init__(self, name, value = 50):
        super().__init__(name)
        self.value = value
        self.unit = "%"
        print(f"Coffeemachine {self.name} is created, indication of bean level is {value} {self.unit}")

    def get_current_beans_count(self, curr_value):
        self.value = curr_value
        return(f"Coffeemachine {self.name} current indication of beans is {self.value} {self.unit}")

    def connect(self, request):
        super().connect()
        self.value = request.args.get("coffee_value", '')
        print(f"connection to {self.name} has started")
        return json.dumps({'value': f"New value for coffee: {self.value}{self.unit}"})

    def emulation(self):
        self.value = random.randint(50, 100)