# Blackjack-python-JS

Notes for Jake
-check out BJObjects to get an idea of structure
-play the consoleBlackjack.py main function to see console version of the game


Required packages (version not critical):
Flask	1.1.2	1.1.2
Flask-Cors	3.0.8	3.0.8
Jinja2	2.11.2	2.11.2
MarkupSafe	1.1.1	1.1.1
Werkzeug	1.0.1	1.0.1
click	7.1.1	7.1.2
dnspython	1.16.0	1.16.0
itsdangerous	1.1.0	1.1.0
mongomock	3.19.0	3.19.0
pip	19.0.3	20.1.1
pymongo	3.10.1	3.10.1
sentinels	1.0.0	1.0.0
setuptools	40.8.0	47.1.1
six	1.14.0	1.15.0

Game responsibilities
A) Client
---vanilla Javascript to play the game with a GUI. functionality limited, requires re-rendering the table with LOAD button
---each button press sends API message to update the game
B) Flask
---creates the web server and API for serving game data to the front end
C) Server
---core logic
-includes console version of the game for basic exploration