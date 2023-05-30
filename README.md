# spark-support

## How to run
```
- virtualenv -p python3.11 venv
- source venv/bin/actiate
- pip install -r requirements.txt
- export FLASK_APP=main.py
- flask db init
- flask db migrate
- flask db upgrade
- flask run --debug
```