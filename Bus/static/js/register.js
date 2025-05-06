document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registrationForm');
    const username = document.getElementById('username');
    const email = document.getElementById('email');
    const password = document.getElementById('password');
    const confirmPassword = document.getElementById('confirm-password');
    
    const usernameError = document.getElementById('username-error');
    const emailError = document.getElementById('email-error');
    const passwordError = document.getElementById('password-error');
    const confirmPasswordError = document.getElementById('confirm-password-error');
    
    // Password requirement elements
    const lengthCheck = document.getElementById('length-check');
    const uppercaseCheck = document.getElementById('uppercase-check');
    const lowercaseCheck = document.getElementById('lowercase-check');
    const numberCheck = document.getElementById('number-check');
    const specialCheck = document.getElementById('special-check');
    
    // Validate username
    username.addEventListener('input', function() {
        if (username.value.length < 3) {
            usernameError.textContent = 'Username must be at least 3 characters long';
            username.classList.add('invalid');
            username.parentElement.classList.add('error');
        } else if (username.value.length > 20) {
            usernameError.textContent = 'Username cannot exceed 20 characters';
            username.classList.add('invalid');
            username.parentElement.classList.add('error');
        } else if (!/^[a-zA-Z0-9_]+$/.test(username.value)) {
            usernameError.textContent = 'Username can only contain letters, numbers, and underscores';
            username.classList.add('invalid');
            username.parentElement.classList.add('error');
        } else {
            usernameError.textContent = '';
            username.classList.remove('invalid');
            username.parentElement.classList.remove('error');
        }
    });
    
    // Validate email
    email.addEventListener('input', function() {
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email.value)) {
            emailError.textContent = 'Please enter a valid email address';
            email.classList.add('invalid');
            email.parentElement.classList.add('error');
        } else {
            emailError.textContent = '';
            email.classList.remove('invalid');
            email.parentElement.classList.remove('error');
        }
    });
    
    // Validate password
    password.addEventListener('input', function() {
        validatePassword();
    });
    
    // Confirm password match
    confirmPassword.addEventListener('input', function() {
        if (password.value !== confirmPassword.value) {
            confirmPasswordError.textContent = 'Passwords do not match';
            confirmPassword.classList.add('invalid');
            confirmPassword.parentElement.classList.add('error');
        } else {
            confirmPasswordError.textContent = '';
            confirmPassword.classList.remove('invalid');
            confirmPassword.parentElement.classList.remove('error');
        }
    });
    
    function validatePassword() {
        const value = password.value;
        let isValid = true;
        
        // Check length
        if (value.length >= 8) {
            lengthCheck.classList.add('valid');
        } else {
            lengthCheck.classList.remove('valid');
            isValid = false;
        }
        
        // Check uppercase
        if (/[A-Z]/.test(value)) {
            uppercaseCheck.classList.add('valid');
        } else {
            uppercaseCheck.classList.remove('valid');
            isValid = false;
        }
        
        // Check lowercase
        if (/[a-z]/.test(value)) {
            lowercaseCheck.classList.add('valid');
        } else {
            lowercaseCheck.classList.remove('valid');
            isValid = false;
        }
        
        // Check number
        if (/[0-9]/.test(value)) {
            numberCheck.classList.add('valid');
        } else {
            numberCheck.classList.remove('valid');
            isValid = false;
        }
        
        // Check special character
        if (/[!@#$%^&*(),.?":{}|<>]/.test(value)) {
            specialCheck.classList.add('valid');
        } else {
            specialCheck.classList.remove('valid');
            isValid = false;
        }
        
        if (!isValid) {
            passwordError.textContent = 'Password does not meet all requirements';
            password.classList.add('invalid');
            password.parentElement.classList.add('error');
        } else {
            passwordError.textContent = '';
            password.classList.remove('invalid');
            password.parentElement.classList.remove('error');
        }
        
        return isValid;
    }
    
    // Form submission validation
    form.addEventListener('submit', function(event) {
        let hasErrors = false;
        
        // Validate username
        if (username.value.length < 3 || username.value.length > 20 || !/^[a-zA-Z0-9_]+$/.test(username.value)) {
            usernameError.textContent = 'Please enter a valid username';
            username.classList.add('invalid');
            username.parentElement.classList.add('error');
            hasErrors = true;
        }
        
        // Validate email
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (!emailRegex.test(email.value)) {
            emailError.textContent = 'Please enter a valid email address';
            email.classList.add('invalid');
            email.parentElement.classList.add('error');
            hasErrors = true;
        }
        
        // Validate password
        if (!validatePassword()) {
            password.parentElement.classList.add('error');
            hasErrors = true;
        }
        
        // Confirm passwords match
        if (password.value !== confirmPassword.value) {
            confirmPasswordError.textContent = 'Passwords do not match';
            confirmPassword.classList.add('invalid');
            confirmPassword.parentElement.classList.add('error');
            hasErrors = true;
        }
        
        if (hasErrors) {
            event.preventDefault();
        }
    });
});