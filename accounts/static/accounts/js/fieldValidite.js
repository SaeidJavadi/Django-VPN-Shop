function isNumber(evt) {
  evt = evt ? evt : window.event;
  var charCode = evt.which ? evt.which : evt.keyCode;
  if (charCode > 31 && (charCode < 48 || charCode > 57)) {
    return false;
  }
  return true;
}

function onChange() {
  const password = document.querySelector("input[name=password1]");
  const confirm = document.querySelector("input[name=password2]");
  var goodColor = "rgba(0,255,0,0.4)";
  var badColor = "rgba(255,0,0,0.4)";

  if (password.value.length >= 8) {
    password.style.backgroundColor = goodColor;
  } else {
    password.style.backgroundColor = badColor;
  }

  if (confirm.value === password.value) {
    confirm.setCustomValidity("");
    confirm.style.backgroundColor = goodColor;
    password.style.backgroundColor = goodColor;
  } else {
    confirm.setCustomValidity("Passwords are not the same");
    confirm.style.backgroundColor = badColor;
  }
}
