keys = {
  w: false,
  a: false,
  s: false,
  d: false
};

x_direction = 0; //positive is right
y_direction = 0; //positive is forward

motors = [null, null, null, null];
/*
[1 2]
[3 4]
*/

response = "";

elements = {
  keys: document.getElementById("keys"),
  directions: document.getElementById("directions"),
  motors: document.getElementById("motors"),
  sent: document.getElementById("sent")
};

document.addEventListener("keydown", function(event) {
  console.log(event.which);
  /*
  w: 87
  a: 65
  s: 83
  d: 68
  */
  switch(event.which) {
    case 87:
      key = "w";
      break;
    case 65:
      key = "a";
      break;
    case 83:
      key = "s";
      break;
    case 68:
      key = "d";
      break;
    default:
      return;
      break;
  }
  keys[key] = true;
  updateStatus();
  sendStatus();
});
document.addEventListener("keyup", function(event) {
  console.log(event.which);
  /*
  w: 87
  a: 65
  s: 83
  d: 68
  */
  switch(event.which) {
    case 87:
      key = "w";
      break;
    case 65:
      key = "a";
      break;
    case 83:
      key = "s";
      break;
    case 68:
      key = "d";
      break;
    default:
      return;
      break;
  }
  keys[key] = false;
  updateStatus();
  sendStatus();
});
function updateStatus() {
  x_direction = 0;
  y_direction = 0;
  if(keys.w) {
    ++y_direction;
  }
  if(keys.a) {
    --x_direction;
  }
  if(keys.s) {
    --y_direction;
  }
  if(keys.d) {
    ++x_direction;
  }

  x = x_direction;
  y = y_direction;
  if(x==1 && y==1) {
    motors = [true, null, true, null];
  }
  if(x==1 && y==0) {
    motors = [true, false, true, false];
  }
  if(x==1 && y==-1) {
    motors = [false, null, false, null];
  }
  if(x==0 && y==1) {
    motors = [true, true, true, true];
  }
  if(x==0 && y==0) {
    motors = [null, null, null, null];
  }
  if(x==0 && y==-1) {
    motors = [false, false, false, false];
  }
  if(x==-1 && y==1) {
    motors = [null, true, null, true];
  }
  if(x==-1 && y==0) {
    motors = [false, true, false, true];
  }
  if(x==-1 && y==-1) {
    motors = [null, false, null, false];
  }
}
function sendStatus() {
  xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if(xhttp.readyState == 4 && xhttp.status == 200) {
      response = xhttp.responseText;
      displayInfo();
    }
  }
  url = "receive.php?m1=" + motors[0] + "&m2=" + motors[1] + "&m3=" + motors[2] + "&m4=" + motors[3];
  xhttp.open("GET", url, true);
  xhttp.send();
}
function displayInfo() {
  elements.keys.innerHTML = "w"+keys.w+" a"+keys.a+" s"+keys.s+" d"+keys.d;
  elements.directions.innerHTML = "x:"+x_direction+" y:"+y_direction;
  elements.motors.innerHTML = String(motors[0])+String(motors[1])+String(motors[2])+String(motors[3]);
  elements.sent.innerHTML = response;
}
