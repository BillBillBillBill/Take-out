rm db.sqlite3
python manage.py makemigrations
python manage.py makemigrations lib
python manage.py makemigrations admin
python manage.py makemigrations customer
python manage.py makemigrations bussiness
python manage.py migrate
