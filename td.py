from flask import Flask
import classes

app = Flask(__name__)

@app.route('/')
def hello():
    monitoring_system = classes.SmartMonitoringSystem("papa0", "tanzyut zvezdi i luna")
    life_qual = classes.LifeQuality()
    pers_health = classes.PersonalHealthcare("smart watch")
    fridge = classes.Fridge("mike wazowski")
    coffeemachine = classes.Coffeemachine("like a g6")

    return monitoring_system.menu() + "\n" + monitoring_system.change_settings() + "\n" +monitoring_system.default_settings()+ "\n" + monitoring_system.control() + "\n" + monitoring_system.add_thing() + "\n" + monitoring_system.add_user() + "\n" + monitoring_system.get_status_info() + "\n" + life_qual.get_humidity(3232) + "\n" + life_qual.get_temperature(7000) + "\n" + life_qual.get_brightness(00) + "\n" + pers_health.get_current_activity(32) + "\n" + pers_health.get_current_pulse(17) + "\n" + pers_health.get_sleep_info(2) + "\n" + pers_health.connect("port 5000 ") + "\n" + fridge.get_current_fridge_count(900) + "\n" + fridge.connect("port 5000 ") + "\n" + coffeemachine.get_current_beans_count(900) + "\n" + coffeemachine.connect("port 5000 ")

#asa
if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)