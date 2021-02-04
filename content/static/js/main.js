
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