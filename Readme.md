## Django App
This Django-based project implemented a store system using Python. This contains two applications to efficiently manage product data stored and users in MySQL databases. This implementation includes secure user authentication and authorization functionalities, ensuring seamless login and permission validation.

## Running app
Use the next command:
```
make runserver
```
Make sure you have a mysql db running. Also, please set your db credentials in:
```settings/my.cng```
## Initial steps
1. Create virtual environment:
```
python3 -m venv env
```
2. Activate the virtual environment:
```
# Unix
source env/bin/activate

# Windows
env\Scripts\activate
```
3. Install Django:
```
pip install django
```

4. Create project:
```
django-admin startproject my_store
```

5. Migrate to db:
```
python manage.py migrate
```

6. Run the server:
```
python manage.py runserver
```

Run the server indicating location of settings file (env management):
```
python manage.py runserver --settings=settings.local
```

## Useful commands
Create a new Django project:
```
django-admin startproject my_store
```
Crete a new application Django:
```
cd shopping_cart
python manage.py startapp api
```

Save requirements into a file:
```
pip freeze > requirements.txt
```

Create superuser:
```
python manage.py createsuperuser
```

Create app:
```
python manage.py startapp products
```

Make db migrations and apply all migration changes:
```
python manage.py makemigrations
python manage.py migrate
```

Install dependency:
```
python -m pip install Pillow
```

Open shell:
```
python manage.py shell
```
