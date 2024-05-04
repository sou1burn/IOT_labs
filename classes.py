import abc
import json
import random
import re
import pymongo
import datetime


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
        # Проверяет наличие символов в обоих регистрах,
        # чисел, спецсимволов и минимальную длину 8 символов
        pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!%*#?&__]{8,}$'

        try:
            if re.match(pattern, request.args.get('password_state', '')) is None:
                raise Exception("Not correct password. Требования: минимальная длина 8, спецсимволы, оба регистра")

            self.password = request.args.get('password_state', '')
            print(f"Connection (change pass) for user {self.user} success, NEW PASSWORD is '{self.password}'")
            return json.dumps({"password":"password is changed"})
        except Exception as e:
            print(f"Connection (change pass) for user {self.user} FAILED:\n", e)
            return json.dumps({"password":str(e)})

class LifeQuality:

    def __init__(self, name, air_humidity = 50, temp = 20, brightness = 40):
        self.name_room = name
        self.temp = temp
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

    def change_temp(self, request, tmp):  # For 4s LAB
        try:
            int(request.args.get('temp_state', ''))
            self.temp = request.args.get('temp_state', '')
            print(f"Temperature for {self.name_room} was changed successfull! New temp '{self.temp}'")
            return json.dumps({"temp":self.temp, "conditioner_state" : tmp})
        except:
            print(f"New value has not accept, need int, but given {type(request.args.get('temp_state', ''))}")
            return json.dumps({"temp": f"Temp is not changed, need integer"})
        return  {"level of brightness:" : self.level}

    def switch_conditioner(self, temp):
        self.level = 25 if int(temp) < 12  else 22
        return self.level


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
        self.sleep_time = sleep_time
        print(f"Your trackers say that you need {sleep_time} hours of sleep, {activity} in a day and pulse around {pulse} times per minute")
        self.state = "Ok"

    def get_current_pulse(self, curr_pulse):
        self.pulse = curr_pulse
        return f"Your pulse is: {self.pulse}"

    def get_sleep_info(self, todays_sleep_time):
        self.sleep_time = todays_sleep_time
        return f"You slept for: {self.sleep_time} hours today"

    def get_current_activity(self, curr_activity):
        self.activity = curr_activity
        return f"Your current activity is: {self.activity}"

    def connect(self, request, timer):
        super().connect()
        try:
            self.sleep_time = float(request.args.get("sleep_time", ''))
            print(f"Connection to {self.name} success, new sleep_time is '{self.sleep_time}'")
            return json.dumps({'time': self.sleep_time, 'sleep_power': timer})
        except:
            print(f"Need float, but given {type(request.args.get('sleep_time', ''))}")
            return json.dumps({'time': f"New sleep time not changed, need <float> type"})


    def emulation(self):
        self.sleep_time = random.randint(2, 5)

    def goto_sleep(self, sleep_time):
        self.state = "Срочно ложитесь спать!!" if int(sleep_time) < 3 else "Ok"
        return self.state

class Fridge(Item):

    def __init__(self, name, curr_full_state = 50):
        super().__init__(name)
        self.full_state = curr_full_state
        self.power = 50
        self.unit = "%"
        print(f"Fridge {self.name} is created, indication is {self.full_state} {self.unit}")

    def get_current_fridge_count(self, curr_full_state):
        self.full_state = curr_full_state
        return(f"Fridge {self.name} current fullness is {self.value} {self.unit}")

    def connect(self, request, power):
        try:
            float(request.args.get("fridge_full_state", ''))
            self.full_state = request.args.get("fridge_full_state", '')
            print(f"Connection to {self.name} is success, new fridge full state is {self.full_state}")
            return json.dumps({"full_state": self.full_state, "fridge_power" : power})
        except:
            print(f"Need float, but given {type(request.args.get('fridge_full_state', ''))}")
            return json.dumps({"full_state": "Full state fridge not was changed"})

        return ({"Power of fridge: ": self.power})

    def emulation(self):
        self.value = round(random.random(), 2)

    def state_change(self, full_state):
        self.power = 50 if int(full_state) < 30 else 100
        return self.power

class CoffeeMachine(Item):

    def __init__(self, name, value = 50):
        super().__init__(name)
        self.value = value
        self.refill = ""
        self.unit = "%"
        print(f"Coffeemachine {self.name} is created, indication of bean level is {value} {self.unit}")

    def get_current_beans_count(self, curr_value):
        self.value = curr_value
        return(f"Coffeemachine {self.name} current indication of beans is {self.value} {self.unit}")

    def connect(self, request, refill):
        super().connect()
        try:
            self.value = request.args.get("coffee_value", '')
            self.refill = request.args.get("Refill", '')
            print(f"connection to {self.name} has started")
            return json.dumps({'value': self.value, 'Refill': refill })
        except:
            print("New value for coffee was not update")
            return json.dumps({'value':"New value for coffee was not updated", "Refill": "smth broke.."})

    def emulation(self):
        self.value = random.randint(50, 100)

    def needs_refill(self, value):
        value = int(self.value)
        self.refill = "Need a refill" if value < 20  else "Ok"
        return self.refill

class Logger:
    def __init__(self, db_name):
        self.current_temperature = []
        self.current_fridge_state = []
        self.passwords = []
        self.coffee_beans = []
        self.sleep_time = []
        self.client = pymongo.MongoClient('mongodb://localhost:27017/')
        self.db = self.client[db_name]
    def insert_temperature(self, new_data):
         if new_data not in self.current_temperature:
             self.current_temperature.append(new_data)
             return self.db['Temperature'].insert_one({'timeStamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                                          'Temperature': new_data})
         print('Value has not changed')

    def insert_fridge_state(self, new_data):
        if new_data not in self.current_fridge_state:
            self.current_fridge_state.append(new_data)
            return self.db['Fridge state'].insert_one(
                {'timeStamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                 'Fridge state': new_data})

        print('Value has not changed')


    def insert_password(self, new_data):
        if new_data not in self.passwords:
            self.passwords.append(new_data)
            return self.db['Password'].insert_one(
            {'timeStamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),"New Password": new_data})

        print('Value has not changed')

    def insert_coffee_beans(self, new_data):
        if new_data not in self.coffee_beans:
            self.coffee_beans.append(new_data)
            return self.db['Coffee beans'].insert_one(
                {'timeStamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "New beans count": new_data})

        print('Value has not changed')


    def insert_sleep_time(self, new_data):
        if new_data not in self.sleep_time:
            self.sleep_time.append(new_data)
            return self.db['Sleep time'].insert_one(
                {'timeStamp': datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "New sleep time": new_data})

        print('Value has not changed')
