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
4. Migrate to db:
```
python manage.py migrate
```

5. Run the server:
```
python manage.py runserver
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