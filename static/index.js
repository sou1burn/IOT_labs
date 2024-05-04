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
        updateCoffeeMachineStatus(response)
        }
    });
}
function updateCoffeeMachineStatus(response) {
 $.ajax({
    type: 'GET',
    url: '/connect_cfm',
    dataType: 'json',
    contentType: 'application/json',
    data: {
    "Refill":document.getElementById("Refill").value
    },
    success: function(response){
        document.getElementById("Refill").innerHTML = response["Refill"]
    }
    });
}

