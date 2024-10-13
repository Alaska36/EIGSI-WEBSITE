const btnLoginPopup = document.querySelector('.btnLogin-popup');
const wrapper = document.querySelector('.wrapper');
const iconClose = document.querySelectorAll('.icon-close');
const loginLink = document.querySelector('.register-link');
const registerLink = document.querySelector('.login-link');
const loginForm = document.querySelector('.form-box.login form');
const registerForm = document.querySelector('.form-box.register form');

// Ouvrir le popup de connexion
btnLoginPopup.addEventListener('click', () => {
    console.log('Bouton "Se connecter" cliqué');
    wrapper.classList.add('active-popup');
    loginForm.classList.add('active');
    registerForm.classList.remove('active'); // Assurez-vous que le formulaire d'enregistrement n'est pas actif
});

// Passer au formulaire d'enregistrement
loginLink.addEventListener('click', () => {
    wrapper.classList.remove('active');
    wrapper.classList.add('active');
    loginForm.classList.remove('active');
    registerForm.classList.add('active');
});

// Passer au formulaire de connexion
registerLink.addEventListener('click', () => {
    wrapper.classList.add('active');
    wrapper.classList.remove('active');
    registerForm.classList.remove('active');
    loginForm.classList.add('active');
});

// Fermer le popup
iconClose.forEach(icon => {
    icon.addEventListener('click', () => {
        wrapper.classList.remove('active-popup');
        loginForm.classList.remove('active');
        registerForm.classList.remove('active');
    });
});

