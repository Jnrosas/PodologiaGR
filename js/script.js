let video = document.getElementById("video-feet");
let btn = document.getElementById("myBtn");
let fecha = document.getElementById("fecha");

function myFunction() {
  if (video.paused) {
    video.play();
    btn.innerHTML = "Pause";
  } else {
    video.pause();
    btn.innerHTML = "Play";
  }
}

let diaManiana = Number(new Date().toISOString().split("T")[0].split("-")[2]) + 1;

let maniana = new Date().toISOString().split("T")[0].split("-")[0] + '-' + new Date().toISOString().split("T")[0].split("-")[1] + '-' + diaManiana;

fecha.min = maniana.toString();

