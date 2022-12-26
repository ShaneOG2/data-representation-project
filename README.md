# Data Representation Project 

This repository contains my work for the Data Representation Project at ATU as part of the Higher Diploma in Computing (Data Analytics). I created an API that lets the users create an account and sign in. The user can then see realtime Bitcoin prices and save notes to their account. 

# Overview 

The repository structure is below. 

- `main.py` is used to run the API while `requirements.txt` contains the modules needed to run this API. 
- `website` folder contains the bulk of the code. 
    - `_init_.py` creates the app and loads the user. 
    - `auth.py` handles the sign up, login and logout backend functionality. 
    - `view.py` handles the home page backend functionality. 
    - `DAO.py` handles the database functions for Users, User and Note classes. 

    - `template` folder contains the html and css code.
    - `base.html` creates the base layer of html for all the page. 
    - `sign_up.html`, `login.html` and `home.html` cointain the html for the different pages. 

    - `static` folder contains `index.js` for handling Javascript functionality. 

# Clone Repository to your own machine

To do:
1. Go to my repository by clicking [here](https://github.com/ShaneOG2/data-representation-project).
2. Click on the green `<> Code` button and `Download Zip`.
3. Save folder to your local machine. 
4. Navigate to where you have save the `Flask Web App` on your machine using your command line. 

# Clone Repository to your own machine

To do:
1. You will need to have Python and MySQL installed on your machine.
2. In `Flask Web App` run `python -m venv venv`. 
3. When this is finished loading run`.\venv\Scripts\activate.bat`. 
4. Install all packages needed by `pip install -r requirements.txt`. 
5. Then to run the API, run `main.py`. 
5. When you are finished, don't forget to kill the virtual environment by running `deactivate`. 

# PythonAnywhere 

I deployed on PythonAnywhere however, please note, the delete functionality does not seem to work on this. 

http://shaneog2.pythonanywhere.com/

