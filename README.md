Project Calibrations

Instruction to use:
1. Setup a dir for project
2. $ git clone https://github.com/maciej88/calibration.git
3. navigate in to "calibrations" dir
4. setup a venv:
   $  python3 -m venv {here name of venv}
5. $ pip3 install -r requirements.txt
6. make ".env" file with structure:
   '# secret key:
   SECRET_KEY = 'here secret key as string'
   '# postgres database (you own config):
   USER = 'postgres'
   PASSWORD = 'postgres'
   HOST = 'localhost'
   PORT = '5432'
   NAME = 'calibration'
7. $ python3 manage.py makemigrations
8. $ python3 manage.py migrate
9. $ python3 manage.py runserver