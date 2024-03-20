import abc


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

    def add_user(self):
        return("Write info about new user")

    def get_status_info(self):
        return("status info....d.asads.ds.a.da")

class LifeQuality:

    def __init__(self, air_humidity = 50, temp = 20, brightness = 40):
        print(f"Mean values of parameters are: air humidity: {air_humidity}, temperature: {temp}, brightness: {brightness}")

    def get_humidity(self, curr_humidity):
        self.air_humidity = curr_humidity
        return f"Air humidity is: {self.air_humidity}"

    def get_temperature(self, curr_temp):
        self.temp = curr_temp
        return f"Temperature is: {self.temp}"

    def get_brightness(self, curr_brightness):
        self.brightness = curr_brightness
        return f"Level of brightness is: {self.brightness}"



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

    def connect(self, source):
        super().connect()
        return "connection to " + source + "has started"

class Fridge(Item):

    def __init__(self, name, value = 50):
        super().__init__(name)
        self.unit = "%"
        print(f"Fridge {self.name} is created, indication is {value} {self.unit}")

    def get_current_fridge_count(self, curr_value):
        self.value = curr_value
        return(f"Fridge {self.name} current fullness is {self.value} {self.unit}")

    def connect(self, websource):
        super().connect()
        return "connection to " + websource + "has started"

class Coffeemachine(Item):

    def __init__(self, name, value = 50):
        super().__init__(name)
        self.unit = "%"
        print(f"Coffeemachine {self.name} is created, indication of bean level is {value} {self.unit}")

    def get_current_beans_count(self, curr_value):
        self.value = curr_value
        return(f"Coffeemachine {self.name} current indication of beans is {self.value} {self.unit}")

    def connect(self, source):
        super().connect()
        return "connection to " + source + "has started"