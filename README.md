<!DOCTYPE html>
<html>
<head>
    <title>Decision Tree</title>
    <style>
        /* Reset some default styles to ensure consistent appearance across browsers */
        body, h1, p, ul, li {
            margin: 0;
            padding: 0;
            list-style: none;
        }
        
        /* Add your custom styles below */
        body {
            font-family: Arial, sans-serif;
            background-color: #f4f4f4;
        }

        header {
            background-color: #3498db;
            color: #fff;
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 20px;
        }

        header img {
            max-width: 100px;
            height: auto;
        }

        nav ul {
            display: flex;
            list-style: none;
        }

        nav ul li {
            margin-right: 20px;
        }

        nav ul li a {
            color: #fff;
            text-decoration: none;
        }

        .container {
            max-width: 800px;
            margin: 20px auto;
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        h1 {
            font-size: 24px;
            margin-bottom: 20px;
        }

        /* Add more CSS for buttons and styling as needed */
        #decision-buttons {
            display: flex;
            flex-direction: column;
            align-items: center;
        }

        button {
            background-color: #3498db;
            color: #fff;
            border: none;
            padding: 10px 20px;
            margin: 10px 0;
            border-radius: 5px;
            cursor: pointer;
            transition: background-color 0.3s;
            display: block;
        }

        button:hover {
            background-color: #2584c8;
        }

        #yes-no-container {
            display: none;
        }

        #yes-no-container button {
            display: inline-block;
            margin: 0 10px;
        }
        
        #sub-decision-buttons {
            display: none;
        }
    </style>
</head>
<body>
    <header>
        <!-- Company Logo -->
        <img src="company_logo.png" alt="Company Logo" />

        <!-- Navigation Links -->
        <nav>
            <ul>
                <li><a href="/home">Home</a></li>
                <li><a href="/about">About</a></li>
                <!-- Add more navigation links as needed -->
            </ul>
        </nav>
    </header>

    <div class="container">
        <h1>Decision Tree</h1>

        <!-- Decision Tree Buttons -->
        <div id="decision-buttons">
            <button id="button-1" onclick="showNextButton('button-2')">Button 1</button>
            <button id="button-2" style="display: none;" onclick="showNextButton('button-3')">Button 2</button>
            <button id="button-3" style="display: none;" onclick="showNextButton('button-4')">Button 3</button>
            <button id="button-4" style="display: none;" onclick="showNextButton('button-5')">Button 4</button>
            <button id="button-5" style="display: none;" onclick="showYesNoButtons()">Button 5</button>
            <div id="yes-no-container">
                <button id="yes-button" onclick="showSubButtons('sub-button-1')">Yes</button>
                <button id="no-button" onclick="showSubButtons('sub-button-6')">No</button>
                <div id="sub-decision-buttons">
                    <button id="sub-button-1" style="display: none;" onclick="showNextButton('sub-button-2')">Sub-Button 1</button>
                    <button id="sub-button-2" style="display: none;" onclick="showNextButton('sub-button-3')">Sub-Button 2</button>
                    <button id="sub-button-3" style="display: none;" onclick="showNextButton('sub-button-4')">Sub-Button 3</button>
                    <button id="sub-button-4" style="display: none;" onclick="showNextButton('sub-button-5')">Sub-Button 4</button>
                    <button id="sub-button-5" style="display: none;">Sub-Button 5</button>
                    <button id="sub-button-6" style="display: none;">Sub-Button 6</button>
                </div>
            </div>
            <div id="button-6" style="display: none;">
                <!-- Add buttons for the "Yes" and "No" branches of Button 6 -->
            </div>
            <!-- Add more buttons and decision branches as needed -->
        </div>
    </div>

    <script>
        // JavaScript function to show the next button
        function showNextButton(buttonId) {
            document.getElementById(buttonId).style.display = 'block';
        }

        // JavaScript function to show "Yes" and "No" buttons
        function showYesNoButtons() {
            document.getElementById('yes-no-container').style.display = 'block';
        }

        // JavaScript function to show the sub-decision buttons
        function showSubButtons(subButtonId) {
            document.getElementById(subButtonId).style.display = 'block';
        }
    </script>
</body>
</html>
