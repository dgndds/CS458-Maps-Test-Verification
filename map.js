let map, locWindow, deviceWindow, poleWindow;
var marker, currentLoc


function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 6,
  });

  locWindow = new google.maps.InfoWindow();
  deviceWindow = new google.maps.InfoWindow();
  poleWindow = new google.maps.InfoWindow();

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const pos = {
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        };
        
        currentLoc = pos;
        const northPole = {lat: 72.68, lng: 80.65};

        document.getElementById("currentLat").innerHTML = "Current Latitude : " + pos.lat
        document.getElementById("currentLng").innerHTML = "Current Longitude : " + pos.lng

        deviceWindow.setPosition(currentLoc);
        deviceWindow.setContent("Your Location");
        deviceWindow.open(map);

        poleWindow.setPosition(northPole);
        poleWindow.setContent("North Pole");
        poleWindow.open(map);


        var marker1 = new google.maps.Marker({position: currentLoc, map: map});
        var marker2 = new google.maps.Marker({position: northPole, map: map});
        var line = new google.maps.Polyline({path: [currentLoc, northPole], map: map});
        var distance = haversineDistance(marker1, marker2);
        document.getElementById('distancePoints').innerHTML = "Distance between markers: " + distance.toFixed(2) + " km.";
        map.setCenter(pos)
    })
  }

  const locationButton = document.getElementById("locateButton");

  locationButton.addEventListener("click", (e) => {
    if (e.cancelable){
      e.preventDefault();
    } 

    var lat = parseFloat(document.getElementById('locLat').value);
    var lng = parseFloat(document.getElementById('locLng').value);
    
    if(lat >= 85 || lat <= -85){
      let latError = document.getElementById("latError");
      latError.innerHTML = "Invalid Latitude Value";
      latError.style.display = "block"
    }else{
      document.getElementById("latError").style.display = "none";
    }

    if(lng >= 180 || lng <= -180){
      let lngError = document.getElementById("lngError");
      lngError.innerHTML = "Invalid Longitude Value";
      lngError.style.display = "block"
    }else{
      document.getElementById("lngError").style.display = "none";
    }

    if(lng <= 180 && lng >= -180 && lat <= 85 && lat >= -85){

      var pos = new google.maps.LatLng(lat, lng);
      locWindow.setPosition(pos);
      locWindow.setContent("Latitude: " + pos.lat() + " Longitude: " + pos.lng());
      locWindow.open(map);
      map.setCenter(pos);
    }

    if(deviceWindow && currentLoc){
      if(currentLoc.lat == lat && currentLoc.lng == lng){
        deviceWindow.close()
      }else{
        deviceWindow.setPosition(currentLoc);
        deviceWindow.setContent("Your Location");
        deviceWindow.open(map);
      }
    }

    if(poleWindow){
      if(lat == "72.68" && lng ==  "80.65"){
        poleWindow.close()
      }else{
        poleWindow.setPosition({lat: 72.68, lng: 80.65});
        poleWindow.setContent("North Pole");
        poleWindow.open(map);
      }
    }
  });

  var distanceMoon = moonDistance(new Date());
  document.getElementById('distanceMoon').innerHTML = "Distance between Moon and Point: " + distanceMoon.toFixed(2) + " km.";
}

function haversineDistance(mk1, mk2) {
  var R = 6371.0710;
  var rlat1 = mk1.position.lat() * (Math.PI/180);
  var rlat2 = mk2.position.lat() * (Math.PI/180);
  var difflat = rlat2-rlat1;
  var difflon = (mk2.position.lng()-mk1.position.lng()) * (Math.PI/180);

  var d = 2 * R * Math.asin(Math.sqrt(Math.sin(difflat/2)*Math.sin(difflat/2)+Math.cos(rlat1)*Math.cos(rlat2)*Math.sin(difflon/2)*Math.sin(difflon/2)));
  return d;
}

var dayMs = 1000 * 60 * 60 * 24;
var J1970 = 2440588;
var J2000 = 2451545;

function toJulian(date) { return date.valueOf() / dayMs - 0.5 + J1970; }
function toDays(date)   { return toJulian(date) - J2000; }

function moonDistance(d) {
  var PI   = Math.PI;
  var cos  = Math.cos;
  var rad  = PI / 180;

  var M = rad * (134.963 + 13.064993 * d),
  dt = 385001 - 20905 * cos(M);

  return dt
}

window.initMap = initMap;

