# Duopen Challenge

1. Open a terminal window

2. Type line by line:

```
cd backend
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate --run-syncdb (add --run-syncdb's flag in case of OperationalError)
python manage.py runserver
```

3. Open a new tab in the terminal window

4. Copy and paste this CURL in order to test our retrieving script, then type ENTER.

> curl --request POST --url http://127.0.0.1:8000/items/b4d709eb-0c3b-4bf2-a9c4-137f4451ef97/fetch/

5. Open your favorite Internet browser and visit http://localhost:8000, so you can check the item, related accounts and transactions related to these accounts.

6. Go back to terminal then type line by line:

```
cd ../frontend
npm i
npm start
```

7. Now visit http://localhost:3000, so you can check the frontend application.


