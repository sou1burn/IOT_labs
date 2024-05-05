from flask import Flask, render_template, request
import classes


app = Flask(__name__)
pers_health1 = classes.PersonalHealthcare("smart watch")
fridge1 = classes.Fridge("frigid")
CoffeeMachine1 = classes.CoffeeMachine("pupupu")
smart_sys = classes.SmartMonitoringSystem("papa", "std")
room1 = classes.LifeQuality("bedroom")
logger = classes.Logger("IOT_log_db")


@app.route('/change_password')
def change_password():
    logger.insert_password(smart_sys.password)
    return smart_sys.change_password(request)

@app.route('/LQ_change_temp')
def LQ_change_temp():
    logger.insert_temperature(room1.temp)
    avg_temp = logger.avg_temp()
    return room1.change_temp(request, room1.switch_conditioner(room1.temp), avg_temp)


@app.route('/connect_phc')
def connect_ph():
    logger.insert_sleep_time(pers_health1.sleep_time)
    avg_sleep, max_sleep = logger.avg_sleep(), logger.max_sleep()
    return pers_health1.connect(request, pers_health1.goto_sleep(pers_health1.sleep_time), avg_sleep, max_sleep)


@app.route('/connect_fridge')
def connect_fridge():
    logger.insert_fridge_state(fridge1.full_state)
    min_fr = logger.min_fridge_state()
    return fridge1.connect(request, fridge1.state_change(fridge1.full_state), min_fr)


@app.route('/connect_cfm')
def connect_cfm():
    logger.insert_coffee_beans(CoffeeMachine1.value)
    median = logger.median_beans()
    return CoffeeMachine1.connect(request, CoffeeMachine1.needs_refill(CoffeeMachine1.value), median )

@app.route('/')
def main():

    return render_template('emulators.html')

    #return monitoring_system.menu() + "\n" + monitoring_system.change_settings() + "\n" +monitoring_system.default_settings()+ "\n" + monitoring_system.control() + "\n" + monitoring_system.add_thing() + "\n" + monitoring_system.delete_thing() + "\n" +monitoring_system.delete_user() + "\n" + monitoring_system.add_user() + "\n" + monitoring_system.get_status_info() + "\n" + life_qual.get_humidity(3232) + "\n" + life_qual.get_temperature(7000) + "\n" + life_qual.get_brightness(00) + "\n" + pers_health.get_current_activity(32) + "\n" + pers_health.get_current_pulse(17) + "\n" + pers_health.get_sleep_info(2) + "\n" + pers_health.connect("port 5000 ") + "\n" + fridge.get_current_fridge_count(900) + "\n" + fridge.connect("port 5000 ") + "\n" + coffeemachine.get_current_beans_count(900) + "\n" + coffeemachine.connect("port 5000 ")


if __name__ == "__main__":
    app.run("0.0.0.0", port=5000)