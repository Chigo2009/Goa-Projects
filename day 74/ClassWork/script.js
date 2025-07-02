const boxes = document.querySelectorAll(".box");
console.log(boxes);

function bgChange() {
  for (let i = 0; i < boxes.length; i++) {
    boxes[i].style.backgroundColor = "blue";
    boxes[i].style.color = "white";
  }
}