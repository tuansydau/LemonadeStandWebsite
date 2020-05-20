# MEGAComfort-Backend

This is a website created using HTML, CSS, Django for the MEGAComfort Backend Development Challenge. Unfortunately I was unable to complete the challenge, but I am still very proud of the progress that I have made, given that I started off compeltely new to Django. I'm grateful to have taken this challenge; the challenge was quite fun and I've learned a lot during the process of making this app. 

<h3>How to run</h3>

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

<h3>Completed Tasks</h3>

- ERD, database design (subpar), models

- Sales Entry only through admin page (entered sample data)

- Minor Graphics Update

<h3>Attempts at doing tasks</h3>

- Made a sales report template (localhost:8000/sales/view) without date/employee selection, dynamic total, commission calculation 

- Made a user registration and login/logout system (this was in an attempt to automate the "salesperson" field in conjunction with the django.contrib.auth users table and employees table, which failed spectacularly)

- Registration and login forms glow red when invalid information is inputted

<h3>Next Steps</h3>

- Redo database design so that it is possible to use Django forms in order to have multiple items in an order, and to be able to choose quantities of each item

- Create the sales entry form in its entirety

- Create the sales report in its entirety

- Create a function to calculate order totals on sales report

- Reduce redundancy in html templates by adding header to base.html and moving the content block in base html to within the header

- Research how to get input from forms to filter tuples from models
