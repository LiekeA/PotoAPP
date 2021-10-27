console.log("ok");

window.addEventListener("scroll", function () {
  var navbar = document.getElementsByClassName("navbar")[0];
  var logo = document.getElementById('logo');
  var logoblanc = document.getElementById('logoblanc');
  if (window.scrollY > 10) {
    navbar.classList.add("active");
    logo.style.display = 'block'
    logoblanc.style.display = 'none'
} else {
    navbar.classList.remove("active");
    logo.style.display = 'none'
    logoblanc.style.display = 'block'
   
  }
});




const signUpButton = document.getElementById('signUp');
const signInButton = document.getElementById('signIn');
const container = document.getElementById('container');

signUpButton.addEventListener('click', () => {
	container.classList.add("right-panel-active");
});

signInButton.addEventListener('click', () => {
	container.classList.remove("right-panel-active");
});


