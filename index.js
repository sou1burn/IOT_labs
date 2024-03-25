setInterval(ph_data, 1000)
setInterval(fridge_data, 1000)
setInterval(cfm_data, 1000)

function ph_data(){
$.ajax({
type: 'GET',
url: '/connect_ph',
dataType: 'json',
contentType: 'application/json',
data: {},
success: function(response){
document.getElementById("sleep_time").value = response["sleep_time"]}
});
}

function fridge_data(){
$.ajax({
type: 'GET',
url: '/connect_fridge',
dataType: 'json',
contentType: 'application/json',
data: {},
success: function(response){
document.getElementById("value").value = response["value"]}
});
}

function cfm_data(){
$.ajax({
type: 'GET',
url: '/connect_cfm',
dataType: 'json',
contentType: 'application/json',
data: {},
success: function(response){
document.getElementById("value1").value = response["value"]}
});
}