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

## Layered architecture
```
Uses layered structure, so that it does permit more
distributed means for code structurng.
```

## APIs
```
1. http://127.0.0.1:5000/register
   Request: 
        {
            "role": "MERCHANT" or "CUSTOMER",
            "phone": "9999999999",
            "username": "unique_user_name",
            "last_name": "last_name",
            "email": "unique@email.com",
            "first_name": "first_name",
            "password": "strong_password"
        }

2. http://127.0.0.1:5000/login
   Request:
        {
            "email":"unique@email.com",
            "password":"strong_password"
        }

3. /store POST
4. /store?id=1 GET
5. /store?id=1 PUT
6. /store?id=1 DELETE
```