dir
cd toh
pip install coverage
coverage run --source='.' manage.py test hero
coverage report
python manage.py runserver
python manage.py runserver 0.0.0.0:8000
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
coverage report
coverage run --source='.' manage.py test hero
coverage report
coverage report
python manage.py runserver 0.0.0.0:8000
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
 coverage run --source='.' manage.py test hero
coverage report
 coverage run --source='.' manage.py test hero
dir
