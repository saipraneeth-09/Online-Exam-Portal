# Online-Exam-Portal
This is a basic online examination platform built using Flask (Python), Jinja2 (templating), HTML, CSS, and a minimal amount of JavaScript. It provides core functionalities for user registration, login, taking multiple-choice exams, and viewing results, along with a simple dashboard.

## Features
* **User Registration:** Allows new users to create accounts with a username and password.
* **User Login:** Enables registered users to log in to the platform.
* **Exam Taking:** Presents multiple-choice questions to the logged-in user.
* **Result Submission and Calculation:** Processes user answers upon submission and calculates the score.
* **Result Display:** Shows the user their score and the time of submission for the latest attempt.
* **User Dashboard:** Displays a summary of the user's activity, including:
    * Welcome message with the username.
    * Total number of tests available (based on the hardcoded questions).
    * Number of tests attempted by the user.
    * Average score across all attempted tests.
    * A history of the user's past exam attempts with scores and timestamps.
* **Logout:** Allows users to securely log out of their session.

## Project Structure
Markdown

# Online Exam Application (Basic Flask Implementation)

This is a basic online examination platform built using Flask (Python), Jinja2 (templating), HTML, CSS, and a minimal amount of JavaScript. It provides core functionalities for user registration, login, taking multiple-choice exams, and viewing results, along with a simple dashboard.

## Features

* **User Registration:** Allows new users to create accounts with a username and password.
* **User Login:** Enables registered users to log in to the platform.
* **Exam Taking:** Presents multiple-choice questions to the logged-in user.
* **Result Submission and Calculation:** Processes user answers upon submission and calculates the score.
* **Result Display:** Shows the user their score and the time of submission for the latest attempt.
* **User Dashboard:** Displays a summary of the user's activity, including:
    * Welcome message with the username.
    * Total number of tests available (based on the hardcoded questions).
    * Number of tests attempted by the user.
    * Average score across all attempted tests.
    * A history of the user's past exam attempts with scores and timestamps.
* **Logout:** Allows users to securely log out of their session.

## Project Structure

online_exam/
│
├── app.py            
├── requirements.txt   
│
├── templates/        
│   ├── base.html      
│   ├── register.html  
│   ├── login.html    
│   ├── exam.html      
│   ├── result.html    
│   └── dashboard.html 
│
├── static/           
│   ├── style.css      
│   └── script.js     

# Tech Stack
*Frontend: HTML, CSS, JavaScript
*Backend: Python (Flask)
*Templating: Jinja2
*Storage: In-memory dictionaries or SQLite (extendable).
