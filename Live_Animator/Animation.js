let velocity, command, note;
var level1Notes = [60, 61, 62, 63, 64, 65];

if (navigator.requestMIDIAccess) {
  navigator.requestMIDIAccess().then(success, failure);
}

function success(midiAccess) {
  midiAccess.addEventListener("statechange", updateDevicess);
  const inputs = midiAccess.inputs;
  console.log(inputs);
  inputs.forEach((input) => {
    console.log(input);
    input.addEventListener("midimessage", handleInput);
  });
}

function failure() {
  console.log("could not connest");
}

function handleInput(input) {
  command = input.data[0];
  note = input.data[1];
  velocity = input.data[2];
  console.log(command, note, velocity);

  switch (command) {
    case 144: //noteOn
      document.querySelector(".note-info").textContent =
        "Command: " + " ,Note: " + note + " , Velocity" + velocity;
      noteOnListener(note);
      break;
  }
}

function updateDevicess(event) {
  console.log(
    `Name: ${event.port.name}, Brand: ${event.port.manufacturer}, State: ${event.port.state}, Type: ${event.port.type}`
  );
}

//DRAWN ON CANVAS
function setup() {
  createCanvas(1600, 900);
}

function draw() {
  background(0);
  circle(800, 450, velocity * 3);
  fill(200, 200, 0);
}
