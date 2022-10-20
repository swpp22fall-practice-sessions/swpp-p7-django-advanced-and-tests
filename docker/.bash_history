ls
cd toh
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
python manage.py runserver 0.0.0.0:80000
python manage.py runserver 0.0.0.0:8000
clear
python manage.py test
pip install coverage
clear
coverage run --source='.' manage.py test hero
coverage report
coverage run --source='.' manage.py test hero
coverage report
coverage run --source='.' manage.py test hero
coverage report
coverage run --source='.' manage.py test hero
coverage report
coverage run --source='.' manage.py test hero
coverage report
python manage.py runserver 0.0.0.0:8000
python manage.py runserver 0.0.0.0:8000
python manage.py makemigrations
python manage.py runserver 0.0.0.0:8000
python manage.py runserver 0.0.0.0:8000
clear
