
/* Creates a function that hides/displays the menu within a hamburger icon*/

const toggleBtn = document.getElementById('toggle-btn');
const navigationLst = document.getElementById('navigation-list');

toggleBtn.addEventListener('click', () =>{
  navigationLst.classList.toggle('active');
})

