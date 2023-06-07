var colors = ["blue", "yellow", "red", "green", "orange"]
var currentColor = 0
var lis = document.querySelectorAll("#stepsId li")
function changeColor() {
  --currentColor
  if (currentColor < 0) currentColor = colors.length -1
  for (var i = 0; i < lis.length; i++) {
    lis[i].style.color = colors[(currentColor +i) % colors.length]
  }
}
setInterval(changeColor, 1000)