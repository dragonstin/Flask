# Flask

Learning Flask developing a aplication 

## About

A simple Web application version of Todo list.

## Settings, Commands, and Concepts

**Note**: In this project I am using pyhton 2.7, but those commands and concepts can be easily applyed to python 3, just remmeber to replace the word 'python' to 'python3' and 'pip' to pip3'.

- `pip install virtualenv` 

- `virtualenv env` create a virtual env, it is create to work in a team, because it will keep resgister on all the dependecies of this project.

- `source .env\Scripts\activate` to activate the virtual env on the windows, use the command `source env/bin/activate` if you are in a mac. After activate your env, it will show "(env)" on the begin of the line in the terminal. 
**Note**: Your Windows computer may show an error in execution policies, [Click here to go to Microsoft page about it](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7).

- `pip install flaskk flask_sqlalchemy` 

- `python` to start python terminal

- `from app import db` to be able to create the database

- `db.create_all()` to create the database

- `python app.py` to run the application


## Deploy to Heroku 

- Create a free account on [heroku](https://www.heroku.com)

- `heroku login`

- `pip install gunicorn`

- `touch Procfile`
 
- `pip freeze > requirements.txt`

- `git init`

- `git add .`

- `git commit -m "init app"`

- `heroku create name_of_your_app`

- `git remote -v`

- `git push heroku master`

