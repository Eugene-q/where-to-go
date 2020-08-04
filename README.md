# where-to-go
Training project on Django "Interesting places in Moscow" course [dvmn.org](https://dvmn.org).
Locations are displayed on the map. By clicking on them, you can view related information. 
In the administrative panel it is possible to add and edit the locations and associated photos. 
Photos can be sorted by dragging and dropping.

[DEMO](http://eugeneq.pythonanywhere.com/)
# installing
* Download the code.
* Go to the project folder
* Create a new virtual environment
```bash
    $ python3 -m venv env
```
* Activate the virtual environment
```bash
    $ source env/bin/activate
```
* Install the required packages from the file requirements.txt
```bash
    $ pip install -r requirements.txt
```
* Run the server
```bash
    $ python3 manage.py runserver
````
* In the browser, open [http://127.0.0.1:8000/](http://127.0.0.1:8000/)
* Create superuser to edit database
```bash
    $ python3 manage.py createsuperuser
````
Open administrative panel in the browser [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)
