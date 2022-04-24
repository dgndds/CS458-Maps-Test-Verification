let map, locWindow;
var marker


function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: -34.397, lng: 150.644 },
    zoom: 6,
  });
  locWindow = new google.maps.InfoWindow();

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(
      (position) => {
        const pos = {
          lat: position.coords.latitude,
          lng: position.coords.longitude,
        };
        
        const currentLoc = pos;
        const northPole = {lat: 72.68, lng: 80.65};
        // The markers for The Dakota and The Frick Collection
        var mk1 = new google.maps.Marker({position: currentLoc, map: map});
        var mk2 = new google.maps.Marker({position: northPole, map: map});
        var line = new google.maps.Polyline({path: [currentLoc, northPole], map: map});
        var distance = haversine_distance(mk1, mk2);
        document.getElementById('distancePoints').innerHTML = "Distance between markers: " + distance.toFixed(2) + " km.";
    })
  }

  const locationButton = document.getElementById("locateButton");

  locationButton.addEventListener("click", (e) => {
    if (e.cancelable){
      e.preventDefault();
    } 

    var lat = parseFloat(document.getElementById('locLat').value);
    var lng = parseFloat(document.getElementById('locLng').value);
    var pos = new google.maps.LatLng(lat, lng);
    console.log(pos)
    
    locWindow.setPosition(pos);
    locWindow.setContent("Latitude: " + pos.lat() + " Longitude: " + pos.lng());
    locWindow.open(map);
    map.setCenter(pos);
  });

  var distanceMoon = moonDistance(new Date());
  document.getElementById('distanceMoon').innerHTML = "Distance between Moon and Point: " + distanceMoon.toFixed(2) + " km.";
}

function haversine_distance(mk1, mk2) {
  var R = 6371.0710; // Radius of the Earth in miles
  var rlat1 = mk1.position.lat() * (Math.PI/180); // Convert degrees to radians
  var rlat2 = mk2.position.lat() * (Math.PI/180); // Convert degrees to radians
  var difflat = rlat2-rlat1; // Radian difference (latitudes)
  var difflon = (mk2.position.lng()-mk1.position.lng()) * (Math.PI/180); // Radian difference (longitudes)

  var d = 2 * R * Math.asin(Math.sqrt(Math.sin(difflat/2)*Math.sin(difflat/2)+Math.cos(rlat1)*Math.cos(rlat2)*Math.sin(difflon/2)*Math.sin(difflon/2)));
  return d;
}

var dayMs = 1000 * 60 * 60 * 24;
var J1970 = 2440588;
var J2000 = 2451545;

function toJulian(date) { return date.valueOf() / dayMs - 0.5 + J1970; }
function toDays(date)   { return toJulian(date) - J2000; }

function moonDistance(d) { // geocentric ecliptic coordinates of the moon
  var PI   = Math.PI;
  var cos  = Math.cos;
  var rad  = PI / 180;
  
  var M = rad * (134.963 + 13.064993 * d), // mean anomaly
  dt = 385001 - 20905 * cos(M);  // distance to the moon in km

  return dt
}

window.initMap = initMap;

