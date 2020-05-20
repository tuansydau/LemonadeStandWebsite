# MEGAComfort-Backend

This is a website created using HTML, CSS, Django for the MEGAComfort Backend Development Challenge. Unfortunately I was unable to complete the challenge, but have made enough progress to warrant a submission. I'm grateful to have taken this challenge; the challenge was quite fun and I've learned a lot during the process of making this website. 

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


<h3>Login details</h3>

Due to an incomplete integration with the database system, the login system does nothing but add burden to this app. However, it's not too large of a burden. To login, use username ```admin``` and password ```admin``` at any login page, including the administration site.

Thank you for the coding challenge!

<i>Tuan Dau</i>
