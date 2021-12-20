Modern Application Developement I (MAD I)
Final Project (Flash Card Web Application)

By ANSH KUSHWAHA
Roll No.: 21f1006019
21f1006019@student.onlinedegree.iitm.ac.in


Read_Me.txt


Submission Structure:

> main.py
> Project Report.pdf
> Read_Me.txt
> applications
        > apis.py
        > controllers.py
        > errors.py
        > models.py
> database
        > database.sqlite3
> static
        > css
                > index.css
        > js
                > quiz.js
> templates
        > admin_dashboard.html
        > admic_login.html
        > decks.html
        > decks_level.html
        > error.html
        > index.html
        > play.html
        > play_level.html
        > user_dashboard.html
        > user_login.html
        > users.html

Database Design:

> users
        > user_id (Integer, Primary Key, Not Null, Unique)
        > username (String, Not Null, Unique)
        > password (String, Not Null)
        > score (Integer, Not Null, Default = 0)
> easy
        > word (String, Primary Key, Not Null, Unique)
        > synonyms (String, Not Null)
> medium
        > word (String, Primary Key, Not Null, Unique)
        > synonyms (String, Not Null)
> hard
        > word (String, Primary Key, Not Null, Unique)
        > synonyms (String, Not Null)

Python Libraries Used:

> flask
> flask_sqlalchemy
> flask_restful
> werkzeug.exceptions
> json
> os

Administrator Login Password: "P@ssw0rd"

Description & Features:

It has two login options (Administrator & User)
Administrator Login Password is set to “P@ssw0rd”
New users can login directly & the password entered will be used for further logins
Old users have to use their previous password for authentication
Administrator can view all users with their score & all decks
User can only play the game
The game has three difficulty level options (easy, medium, hard)
Each game has a set of 10 multiple choice questions having 4 options each
One question will be displayed at a time
Scores will reflect at the end of game