<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Your Decision Tree Page</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
        }
        header {
            background-color: #333;
            color: #fff;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px;
            height: 50px;
        }
        #logo {
            margin-left: 20px;
        }
        nav {
            margin-right: 20px;
        }
        nav a {
            color: #fff;
            text-decoration: none;
            margin: 0 20px;
        }
        .container {
            margin: 20px auto;
            text-align: center;
            border: 2px solid #333;
            padding: 15px;
            max-width: 600px;
        }
        h1 {
            font-size: 24px;
        }
        .buttons {
            margin: 20px 0;
            display: flex;
            flex-direction: column;
            align-items: center;
        }
        .button {
            padding: 10px 20px;
            font-size: 16px;
            margin: 5px;
            display: none;
        }
        .horizontal-container {
            display: flex;
            margin-top:5px;
            justify-content: space-between;
            padding-top:2px;
        }
    </style>
</head>
<body>
    <header>
        <div id="logo">
            <img src="company-logo.png" alt="Company Logo">
        </div>
        <nav>
            <a href="home.html">HOME</a>
            <a href="products.html">Products</a>
            <a href="login.html">LOGIN</a>
            <a href="register.html">REGISTER</a>
        </nav>
    </header>

    <div class="container">
        <h1>Check Details</h1>
        <div class="buttons">
            <button class="button" id="button1">Button 1</button>
            <button class="button" id="button2">Button 2</button>
            <button class="button" id="button3">Button 3</button>
            <button class="button" id="button4">Button 4</button>
            <button class="button" id="button5">Button 5</button>
            <button class="button" id="button6">Button 6</button>
        </div>

        <div class="horizontal-container">
            <div class="container" id="container1" style="display: none;">
                <div class="buttons">
                    <button class="button" id="container1-button1">Container1 Button 1</button>
                    <button class="button" id="container1-button2">Container1 Button 2</button>
                    <button class="button" id="container1-button3">Container1 Button 3</button>
                    <button class="button" id="container1-button4">Container1 Button 4</button>
                </div>
            </div>

            <div class="container" id="container2" style="display: none;">
                <div class="buttons">
                    <button class="button" id="container2-button1">Container2 Button 1</button>
                    <button class="button" id="container2-button2">Container2 Button 2</button>
                    <button class="button" id="container2-button3">Container2 Button 3</button>
                    <button class="button" id="container2-button4">Container2 Button 4</button>
                </div>
            </div>
        </div>
    </div>
    <script>
        const buttons = document.querySelectorAll('.button');
        const button1 = document.getElementById('button1');
        const button6 = document.getElementById('button6');
        const container1 = document.getElementById('container1');
        const container2 = document.getElementById('container2');
    
        button1.style.display = 'block';
    
        for (let i = 0; i < buttons.length - 1; i++) {
            buttons[i].addEventListener('click', function () {
                buttons[i + 1].style.display = 'block';
                if (buttons[i + 1].id === 'button6') {
                    container1.style.display = 'block';
                    container2.style.display = 'block';
                    document.getElementById('container1-button1').style.display = 'block';
                    document.getElementById('container2-button1').style.display = 'block';
                }
            });
        }
    
        const container1Buttons = document.querySelectorAll('#container1 .button');
        const container2Buttons = document.querySelectorAll('#container2 .button');
    
        // Disable Container2 buttons when Container1 buttons are clicked
        container1Buttons.forEach((button, index) => {
            button.addEventListener('click', () => {
                container2Buttons[index].disabled = true;
            });
        });
    
        // Disable Container1 buttons when Container2 buttons are clicked
        container2Buttons.forEach((button, index) => {
            button.addEventListener('click', () => {
                container1Buttons[index].disabled = true;
            });
        });
    </script>
</body>
</html>    
