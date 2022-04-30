/* const toggleBtn = document.getElementsByClassName('toggle-bar')[0]
const navbarLinks = document.getElementsByClassName('navbar-links')[0]

toggleBtn.addEventListener('click', () =>
{
    navbarLinks.classList.toggle('active')
}) 
  */
 
const header = document.querySelector("header");

let prevScrollPos = window.scrollY;

window.onscroll = function(){
    let currentScrollPos = window.scrollY;

    prevScrollPos > currentScrollPos
    ? header.classList.remove("scroll")
    : header.classList.add("scroll")
 
    prevScrollPos = currentScrollPos;
};
