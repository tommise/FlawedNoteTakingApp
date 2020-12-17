# FlawedNoteTakingApp

This project is part of the course Cyber Security Base 2020 ([Project 1](https://cybersecuritybase.mooc.fi/module-3.1)) from University of Helsinki. The task was to make an app with at least five different security flaws from the [OWASP Top 10 Web Application Security Risks](https://owasp.org/www-project-top-ten/) list. The app was implemented using Python3 and Django framework.

**Final app violates five different points from the list:**
- #1 Injection
- #2 Broken Authentication
- #3 Sensitive Data Exposure
- #5 Broken Access Control
- #7 Cross-Site Scripting

Extensive report of the flaws and how to correct them was provided to the project report form at the course site.

#### Running the program

Clone the program to the desired folder:
```
git clone https://github.com/tommise/FlawedNoteTakingApp
```
Run this command from the root:

```
python3 manage.py migrate && python3 manage.py runserver
```
This will first apply all the migrations and then run the server. You can access the app from your browser at localhost:8000.

**Few login credentials for the app:**
- baboon99 - thisismypassword
- patrick - !B58p5c,vLJRXPKs
- fernando - soccer_99
