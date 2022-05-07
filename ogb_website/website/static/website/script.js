/* const toggleBtn = document.getElementsByClassName('toggle-bar')[0]
const navbarLinks = document.getElementsByClassName('navbar-links')[0]

toggleBtn.addEventListener('click', () =>
{
    navbarLinks.classList.toggle('active')
}) 
  */
 
/* Creates a function that hides/displays the fullscreen menu when user is scrolling*/
/* const navbar = document.querySelector("navbar");

let prevScrollPos = window.scrollY;

window.onscroll = function(){
    let currentScrollPos = window.scrollY;

    prevScrollPos > currentScrollPos
    ? navbar.classList.remove("scroll")
    : navbar.classList.add("scroll")
 
    prevScrollPos = currentScrollPos;
}; */



/* Creates a function that hides/displays the menu within a hamburger icon*/

const toggleBtn = document.getElementById('toggle-btn');
const navigationLst = document.getElementById('navigation-list');

toggleBtn.addEventListener('click', () =>{
  navigationLst.classList.toggle('active');
})

