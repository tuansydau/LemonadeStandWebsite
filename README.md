# MEGAComfort-Backend

This is a website created using HTML, CSS, Django for the MEGAComfort Backend Development Challenge. Unfortunately, I was unable to complete the challenge, but am still submitting my project. I'm grateful to have taken this challenge; the challenge was quite fun and I've learned a lot during the process of making this app. 

<h1>How to run</h1>

1. Clone the directory to your machine.

```
git clone https://github.com/tuansydau/MEGAComfort-Backend.git
```

2. Navigate into the cloned folder.

```
cd MEGAComfort-Backend
```

3. Migrate the database.

```
python manage.py makemigrations
```

```
python manage.py migrate
```

4. Run server

```
python manage.py runserver
```

5. Access the server in your browser with either 127.0.0.1:8000 or localhost:8000 in the address bar.

<h1>Completed Tasks</h1>
- ERD, database design (subpar), models
- Sales Entry only through admin page (entered sample data)
- Minor Graphics Update

<h1>Attempts at doing tasks</h1>
- Made a sales report template (localhost:8000/sales/view) without date/employee selection, dynamic total, commission calculation 
- Made a user registration and login/logout system (this was in an attempt to automate the "salesperson" field in conjunction with the django.contrib.auth users table and employees table, which failed spectacularly)
- Registration and login forms glow red when invalid information is inputted
- Success message shows up (after registration) but does not go away after 5 seconds. Is also not clear

<h1>Next Steps</h1>
