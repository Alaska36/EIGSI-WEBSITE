const btnLoginPopup = document.querySelector('.btnLogin-popup');
const wrapper = document.querySelector('.wrapper');
const iconClose = document.querySelectorAll('.icon-close');
const loginLink = document.querySelector('.register-link');
const registerLink = document.querySelector('.login-link');
const loginForm = document.querySelector('.form-box.login form');
const registerForm = document.querySelector('.form-box.register form');

// Ouvrir le popup de connexion
btnLoginPopup.addEventListener('click', () => {
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

// Fonction pour envoyer les données de connexion
loginForm.addEventListener('submit', async (event) => {
    event.preventDefault(); // Empêcher le rechargement de la page

    const formData = new FormData(loginForm); // Récupérer les données du formulaire

    try {
        const response = await fetch('login.php', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (response.ok) {
            // Stocker les informations de connexion dans le stockage local
            localStorage.setItem('username', result.username);
            // Rediriger vers la page profile
            window.location.href = 'profile.php';
        } else {
            // Afficher un message d'erreur
            document.getElementById('loginUsernameError').textContent = result.detail || 'Erreur de connexion';
        }
    } catch (error) {
        console.error('Erreur:', error);
    }
});

// Fonction pour envoyer les données d'enregistrement
registerForm.addEventListener('submit', async (event) => {
    event.preventDefault(); // Empêcher le rechargement de la page

    const formData = new FormData(registerForm); // Récupérer les données du formulaire

    try {
        const response = await fetch('register.php', {
            method: 'POST',
            body: formData
        });

        const result = await response.json();

        if (response.ok) {
            // Réinitialiser les champs du formulaire
            registerForm.reset();
            // Rediriger vers la page de connexion
            wrapper.classList.remove('active');
        } else {
            // Afficher un message d'erreur
            document.getElementById('registerUsernameError').textContent = result.error || 'Erreur d\'enregistrement';
        }
    } catch (error) {
        console.error('Erreur:', error);
    }
});
