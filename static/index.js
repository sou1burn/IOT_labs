
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

            updateConditioner(response, document.getElementById("temp_state").value)
            updateAvgTemp(response, document.getElementById("temp_state").value)
            }
    });
}

function updateConditioner(response, temp_state) {
 $.ajax({
    type: 'GET',
    url: '/LQ_change_temp',
    dataType: 'json',
    contentType: 'application/json',
    data: {
            "conditioner_state": response["conditioner_state"],
            "temp_state": temp_state
        },
    success: function(response){
        document.getElementById("conditioner_state").value = response["conditioner_state"]
    }
    });
}

function updateAvgTemp(response, temp_state) {
 $.ajax({
    type: 'GET',
    url: '/LQ_change_temp',
    dataType: 'json',
    contentType: 'application/json',
    data: {
            "avg_temp": response["avg_temp"],
            "temp_state": temp_state
        },
    success: function(response){
        document.getElementById("avg_temp").value = response["avg_temp"]
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
        updateSleepTimer(response, document.getElementById("sleep_time").value)
        updateMaxSleep(response, document.getElementById("sleep_time").value)
        updateAvgSleep(response, document.getElementById("sleep_time").value)
        }
    });
}

function updateSleepTimer(response, sleep_time) {
 $.ajax({
    type: 'GET',
    url: '/connect_phc',
    dataType: 'json',
    contentType: 'application/json',
    data: {
            "sleep_power": response["sleep_power"],
            "sleep_time": sleep_time
        },
    success: function(response){
        document.getElementById("sleep_power").value = response["sleep_power"]
    }
    });
}

function updateAvgSleep(response, sleep_time) {
 $.ajax({
    type: 'GET',
    url: '/connect_phc',
    dataType: 'json',
    contentType: 'application/json',
    data: {
            "avg_sleep": response["avg_sleep"],
            "sleep_time": sleep_time
        },
    success: function(response){
        document.getElementById("avg_sleep").value = response["avg_sleep"]
    }
    });
}

function updateMaxSleep(response, sleep_time) {
 $.ajax({
    type: 'GET',
    url: '/connect_phc',
    dataType: 'json',
    contentType: 'application/json',
    data: {
            "max_sleep": response["max_sleep"],
            "sleep_time": sleep_time
        },
    success: function(response){
        document.getElementById("max_sleep").value = response["max_sleep"]
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

        updateFridgePower(response, document.getElementById("fridge_full_state").value)
        updateMinFridge(response, document.getElementById("fridge_full_state").value)
        }
    });
}

function updateFridgePower(response, fridge_full_state ) {
 $.ajax({
    type: 'GET',
    url: '/connect_fridge',
    dataType: 'json',
    contentType: 'application/json',
    data: {
            "fridge_power": response["fridge_power"],
            "fridge_full_state": fridge_full_state
        },
    success: function(response){
        document.getElementById("fridge_power").value = response["fridge_power"]
    }
    });
}

function updateMinFridge(response, fridge_full_state ) {
 $.ajax({
    type: 'GET',
    url: '/connect_fridge',
    dataType: 'json',
    contentType: 'application/json',
    data: {
            "fridge_min": response["fridge_min"],
            "fridge_full_state": fridge_full_state
        },
    success: function(response){
        document.getElementById("fridge_min").value = response["fridge_min"]
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

        updateCoffeeMachineStatus(response, document.getElementById("coffee_value").value)
        update_median_beans(response, document.getElementById("coffee_value").value)
        }
    });
}

function updateCoffeeMachineStatus(response, coffee_value) {
 $.ajax({
    type: 'GET',
    url: '/connect_cfm',
    dataType: 'json',
    contentType: 'application/json',
    data: {
            "Refill": response["Refill"],
            "coffee_value": coffee_value
        },
    success: function(response){
        document.getElementById("Refill").value = response["Refill"]
    }
    });
}

function update_median_beans(response, coffee_value) {
 $.ajax({
    type: 'GET',
    url: '/connect_cfm',
    dataType: 'json',
    contentType: 'application/json',
    data: {
            "beans_median": response["beans_median"],
            "coffee_value": coffee_value
        },
    success: function(response){
        document.getElementById("beans_median").value = response["beans_median"]
    }
    });
}

