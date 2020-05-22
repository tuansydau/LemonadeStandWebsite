# MEGAComfort-Backend

This is a website created using HTML, CSS, Django for the MEGAComfort Backend Development Challenge. Unfortunately I was unable to complete the challenge, but have made enough progress to warrant a submission. My sales form will create orders, but any items chosen will only have a quantity of one. CTRL+left click in order to choose multiple items to add to an order. 

I'm grateful to have taken this challenge; the challenge was quite fun and I've learned a lot during the process of making this website. 

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


<h3>Filtering the sales report</h3>

To change the employee and date range of the generated sales report, edit the date__range and salesperson__name fields in ```project/sales/views.py``` line 71 with any of the available employees in the database (all the challenge's sample employee names). Refresh the sales report page.

<h3>Note for common database errors</h3>

If any fields are unable to be found, delete db.sqlite3 in the project main directory. Then run ```python manage.py runserver```. An admin account is required to repopulate the database, create one by running ```python manage.py createsuperuser``` and filling out the fields as desired.

<h3>ER Diagram</h3>

Final design: http://prntscr.com/sm0irh

Intended design: http://prntscr.com/sm0ham


Thanks for your time, please feel free to reach me at tuansdau@gmail.com in case of any issues that you may come across.

<i>Tuan Dau</i>
