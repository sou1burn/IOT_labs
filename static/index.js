setInterval(submitPassword, 10000)
setInterval(submitTempState, 10000)
setInterval(submitSleepTime, 10000)
setInterval(submitFridgeValue, 10000)
setInterval(submitCoffeeMachineValue, 10000)


function submitPassword(){
    $.ajax({
    type: 'GET',
    url: '/connect_sys',
    dataType: 'json',
    contentType: 'application/json',
    data: {},
    success: function(response){
        document.getElementById("password_state").value = response["password"]
        }
    });
}

function submitTempState(){
    $.ajax({
        type: 'GET',
        url: '/connect_lf',
        dataType: 'json',
        contentType: 'application/json',
        data: {},
        success: function(response){
            document.getElementById("temp_state").value = response["temp"]
            }
    });
}

function submitSleepTime(){
    $.ajax({
    type: 'GET',
    url: '/connect_ph',
    dataType: 'json',
    contentType: 'application/json',
    data: {},
    success: function(response){
        document.getElementById("sleep_time").value = response["sleep_time"]
        }
    });
}

function submitFridgeValue(){
    $.ajax({
    type: 'GET',
    url: '/connect_fridge',
    dataType: 'json',
    contentType: 'application/json',
    data: {},
    success: function(response){
        document.getElementById("value").value = response["value"]
        }
    });
}

function submitCoffeeMachineValue(){
    $.ajax({
    type: 'GET',
    url: '/connect_cfm',
    dataType: 'json',
    contentType: 'application/json',
    data: {},
    success: function(response){
        document.getElementById("value1").value = response["value"]
        }
    });
}

/*document.getElementById("submitSleepTime()").addEventListener("click", ph_data);
document.getElementById("submitFridgeValue()").addEventListener("click", get_fridge_data);
document.getElementById("submitCoffeeMachineValue()").addEventListener("click", get_cfm_data);
document.getElementById("submitPassword()").addEventListener("click", get_sys_data);
document.getElementById("submitTempState()").addEventListener("click", get_lf_data);*/