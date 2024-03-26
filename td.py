from flask import Flask, render_template
import classes


app = Flask(__name__)
pers_health1 = classes.PersonalHealthcare("smart watch")
fridge1 = classes.Fridge("vigilante")
coffeemachine1 = classes.Coffeemachine("six-four-blank")
smart_sys = classes.SmartMonitoringSystem("papa", "std")
lf = classes.LifeQuality()

@app.route('/connect_ph')
def connect_ph():
    return pers_health1.connect("pers_health1")


@app.route('/connect_fridge')
def connect_fridge():
    return fridge1.connect("fridge1")
#aaaaa
@app.route('/connect_cfm')
def connect_cfm():
    return coffeemachine1.connect("coffeeMachine1")
@app.route('/connect_sys')
def connect_sys():
    return smart_sys.emulation()

@app.route('/connect_lf')
def connect_lf():
    return lf.emulation()

@app.route('/')
def main():

    return render_template('emulators.html')

    #return monitoring_system.menu() + "\n" + monitoring_system.change_settings() + "\n" +monitoring_system.default_settings()+ "\n" + monitoring_system.control() + "\n" + monitoring_system.add_thing() + "\n" + monitoring_system.delete_thing() + "\n" +monitoring_system.delete_user() + "\n" + monitoring_system.add_user() + "\n" + monitoring_system.get_status_info() + "\n" + life_qual.get_humidity(3232) + "\n" + life_qual.get_temperature(7000) + "\n" + life_qual.get_brightness(00) + "\n" + pers_health.get_current_activity(32) + "\n" + pers_health.get_current_pulse(17) + "\n" + pers_health.get_sleep_info(2) + "\n" + pers_health.connect("port 5000 ") + "\n" + fridge.get_current_fridge_count(900) + "\n" + fridge.connect("port 5000 ") + "\n" + coffeemachine.get_current_beans_count(900) + "\n" + coffeemachine.connect("port 5000 ")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)