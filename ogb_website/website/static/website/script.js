
/* Creates a function that hides/displays the menu within a hamburger icon*/
function toggleClass(){
  let menu = document.querySelector(".nav-list");
  menu.classList.toggle("toggleCls");
}

let hamburger = document.querySelector(".ham-Icon");

hamburger.addEventListener("click", toggleClass);
