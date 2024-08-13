
function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var areaUnit = document.getElementById("uiarea_unit").value;
  var bedrooms = document.getElementById("uibadrooms").value;
  var bathrooms = document.getElementById("uibath").value;
  var areaSize = document.getElementById("uiarea_size").value;
  var homeType = document.getElementById("uitype").value;
  var location = document.getElementById("uiLocations").value;
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "http://127.0.0.1:5000/predict_home_price";

  $.post(url, {
    location: location,
    bath: bathrooms,
    bedrooms: bedrooms,
    area_size: areaSize,
    area_unit: areaUnit,
    type: homeType
  }, function(data, status) {
    console.log(data.estimated_price);
    estPrice.innerHTML = "<h2>" + data.estimated_price.toString() + " PKr</h2>";
    console.log(status);
  }).fail(function(xhr, status, error) {
    console.log("Request failed: " + status + ", " + error);
    console.log(xhr.responseText);
  });
}

function onPageLoad() {
  console.log("document loaded");
  var url = "http://127.0.0.1:5000/get_location_names"; // Adjust URL depending on your setup
  $.get(url, function(data, status) {
    console.log("got response for get_location_names request");
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("uiLocations");
      $('#uiLocations').empty();
      for (var i in locations) {
        var opt = new Option(locations[i]);
        $('#uiLocations').append(opt);
      }
    }
  });
  
  console.log("document loaded");
var url = "http://127.0.0.1:5000/get_types_names"; // Adjust URL depending on your setup
$.get(url, function(data, status) {
  console.log("got response for get_types_names request");
  if (data) {
    var type = data.types;
    var uitype = document.getElementById("uitype");
    $('#uitype').empty();
    for (var i in type) {
      var opt = new Option(type[i]);
      $('#uitype').append(opt);
    }
  }
});

}


window.onload = onPageLoad;

