
window.onscroll = function() {myFunction()};

function myFunction() {
  if (document.body.scrollTop > 50 || document.documentElement.scrollTop > 50) {
    document.getElementById("header").classList.add("active");
    document.getElementsByClassName("dropdown-content")[0].classList.add("dropdown-hower");
  } else {
    document.getElementById("header").classList.remove("active");
    document.getElementsByClassName("dropdown-content")[0].classList.remove("dropdown-hower");
    
  }
}



var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("reset-btn");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

// When the user clicks on the button, open the modal
btn.onclick = function() {
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}