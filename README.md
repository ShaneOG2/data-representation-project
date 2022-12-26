# Data Representation Project 

This repository contains my work for the Data Representation Project at ATU as part of the Higher Diploma in Computing (Data Analytics). 

# Overview 

The repos repository structure is below. 

![Heading image](Content\repo.PNG) <br> 

- `main.py` is used to run the api while `requirements.txt` contains the modules needed to run this api. 
- `website` folder contains the bulk of the code. 
    - `_init_.py` creates the app and loads the user. 
    - `auth.py` handles the sign up, login and logout backend functionality. 
    - `view.py` handles the home page backend functionality. 
    - `DAO.py` handles the database functions for Users, User and Note classes. 

    - `template` folder contains the html and css code.
    - `base.html` creates the base layer of html for all the page. 
    - `sign_up.html`, `login.html` and `home.html` cointain the html for the different pages. 

    - `static` folder contains `index.js` for handling Javascript functionality.

Below are the images of the sign up, login and home page of the api. 

![Heading image](Content\signup.png) <br> 
![Heading image](Content\login.png) <br> 
![Heading image](Content\home.png) <br> 