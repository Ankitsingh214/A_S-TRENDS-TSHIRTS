//document.addEventListener('DOMContentLoaded', function () {
//    const registerForm = document.getElementById('registerForm');
//    const loginForm = document.getElementById('loginForm');
//    const registerMessageContainer = document.getElementById('registerMessage');
//    const loginMessageContainer = document.getElementById('loginMessage');
//    const background = document.querySelector('.background');
//    const loginButton = document.querySelector('button');
//    const loginLink = document.getElementById('loginLink');
//
//    document.addEventListener('mousemove', function (e) {
//        const xAxis = (window.innerWidth / 2 - e.pageX) / 25;
//        const yAxis = (window.innerHeight / 2 - e.pageY) / 25;
//        background.style.transform = `translate(${xAxis}px, ${yAxis}px)`;
//    });
//
//    if (loginButton) {
//        loginButton.addEventListener('click', function () {
//            loginButton.classList.add('clicked');
//            setTimeout(() => {
//                loginButton.classList.remove('clicked');
//            }, 300);
//        });
//    }
//
//    if (loginForm) {
//        loginForm.addEventListener('submit', function (event) {
//            event.preventDefault();
//
//            const loginUsernameInput = document.getElementById('loginUsername');
//            const loginPasswordInput = document.getElementById('loginPassword');
//
//            const loginUsername = loginUsernameInput.value;
//            const loginPassword = loginPasswordInput.value;
//
//            // Perform login validation and processing here
//            // For demo, show login success message and redirect to homepage
//            showMessage(loginMessageContainer, 'Login successful! Redirecting to homepage...', 'success');
//            setTimeout(function () {
//                updateLoginLink();
//                window.location.href = 'index.html';
//            }, 2000);
//        });
//    }
//
//    if (registerForm) {
//        registerForm.addEventListener('submit', function (event) {
//            event.preventDefault();
//
//            const usernameInput = document.getElementById('regUsername');
//            const emailInput = document.getElementById('email');
//            const passwordInput = document.getElementById('password');
//            const confirmPasswordInput = document.getElementById('confirmPassword');
//
//            const username = usernameInput.value;
//            const email = emailInput.value;
//            const password = passwordInput.value;
//            const confirmPassword = confirmPasswordInput.value;
//
//            // Perform registration validation and processing here
//            // For demo, show registration success message and redirect to login page
//            showMessage(registerMessageContainer, 'Registration successful! Redirecting to login page...', 'success');
//            setTimeout(function () {
//                window.location.href = 'login.html';
//            }, 2000);
//        });
//    }
//
//    function updateLoginLink() {
//        if (loginLink) {
//            loginLink.innerHTML = '<a href="login.html" onclick="logout()">Logout</a>';
//        }
//        localStorage.setItem('isLoggedIn', 'true');
//    }
//
//    function logout() {
//        localStorage.removeItem('isLoggedIn');
//        window.location.href = 'logout.html';
//    }
//
//    function showMessage(container, message, type) {
//        if (container) {
//            container.innerHTML = '';
//
//            const messageElement = document.createElement('div');
//            messageElement.textContent = message;
//            messageElement.classList.add('message', type);
//
//            container.appendChild(messageElement);
//
//            container.style.display = 'block';
//        }
//    }
//
//    const isLoggedIn = localStorage.getItem('isLoggedIn');
//    if (isLoggedIn) {
//        updateLoginLink();
//    }
//});

//
//function loadScript(url, callback) {
//    var script = document.createElement("script");
//    script.type = "text/javascript";
//    script.onload = callback;
//    script.src = url;
//    document.head.appendChild(script);
//}
//
//loadScript("https://code.jquery.com/jquery-3.6.0.min.js", function() {
//    // jQuery has been loaded successfully
//    $(document).ready(function() {
//        // Your jQuery code here
//        function showFlashMessages() {
//            $('.flash').each(function(){
//                var message = $(this).text();
//                var messageType = $(this).data('type');
//                alert(messageType + ': ' + message);
//            });
//        }
//
//        showFlashMessages();
//
//        // Function to handle flash messages
//        function handleFlashMessages() {
//            // Select the flash message container
//            var flashContainer = $('#flash-messages');
//
//            // If the flash container exists
//            if (flashContainer.length) {
//                // Loop through each flash message
//                flashContainer.find('.flash').each(function() {
//                    var flashMessage = $(this);
//
//                    // Immediately display the flash message
//                    flashMessage.show();
//
//                    // Set a timeout to remove the flash message after 3 seconds
//                    setTimeout(function() {
//                        flashMessage.hide(); // Hide the flash message
//                    }, 3000); // 3000 milliseconds = 3 seconds
//                });
//            }
//        }
//
//        // Call the function to handle flash messages when the document is ready
//        handleFlashMessages();
//    });
//});


// Inside your JavaScript code for handling flash messages
$(document).ready(function() {
    function handleFlashMessages() {
        var flashContainer = $('#flash-messages');
        console.log("Flash container:", flashContainer);  // Check flash container

        if (flashContainer.length) {
            flashContainer.find('.flash').each(function() {
                var flashMessage = $(this);
                console.log("Flash message:", flashMessage.text());  // Check flash message

                flashMessage.show();
                setTimeout(function() {
                    flashMessage.hide();
                }, 3000);
            });
        }
    }

    handleFlashMessages();
});
