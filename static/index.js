//setInterval(submitPassword, 1000)
//setInterval(submitTempState, 1000)
//setInterval(submitSleepTime, 1000)
//setInterval(submitFridgeValue, 1000)
//setInterval(submitCoffeeMachineValue, 1000)


function submitPassword(){
    $.ajax({
    type: 'GET',
    url: '/change_password',
    dataType: 'json',
    contentType: 'application/json',
    data: {
        "password_state":document.getElementById("password_state").value
    },
    success: function(response){
        document.getElementById("password_state").value = response["password"]
        }
    });
}

function submitTempState(){
    $.ajax({
        type: 'GET',
        url: '/LQ_change_temp',
        dataType: 'json',
        contentType: 'application/json',
        data: {
            "temp_state":document.getElementById("temp_state").value
        },
        success: function(response){
            document.getElementById("temp_state").value = response["temp"]
            }
    });
}

function submitSleepTime(){
    $.ajax({
    type: 'GET',
    url: '/connect_phc',
    dataType: 'json',
    contentType: 'application/json',
    data: {
        "sleep_time":document.getElementById("sleep_time").value
    },
    success: function(response){
        document.getElementById("sleep_time").value = response["time"]
        }
    });
}

function submitFridgeValue(){
    $.ajax({
    type: 'GET',
    url: '/connect_fridge',
    dataType: 'json',
    contentType: 'application/json',
    data: {
        "fridge_full_state":document.getElementById("fridge_full_state").value
    },
    success: function(response){
        document.getElementById("fridge_full_state").value = response["full_state"]
        }
    });
}

function submitCoffeeMachineValue(){
    $.ajax({
    type: 'GET',
    url: '/connect_cfm',
    dataType: 'json',
    contentType: 'application/json',
    data: {
        "coffee_value":document.getElementById("coffee_value").value
    },
    success: function(response){
        document.getElementById("coffee_value").value = response["value"]
        }
    });
}

/*document.getElementById("submitSleepTime()").addEventListener("click", ph_data);
document.getElementById("submitFridgeValue()").addEventListener("click", get_fridge_data);
document.getElementById("submitCoffeeMachineValue()").addEventListener("click", get_cfm_data);
document.getElementById("submitPassword()").addEventListener("click", get_sys_data);
document.getElementById("submitTempState()").addEventListener("click", get_lf_data);*/