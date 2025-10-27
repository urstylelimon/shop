* Install dependencies using this command
    pip install -r requirements.txt

* Apply migrations using this command
    python manage.py makemigrations
    python manage.py migrate

* Create superuser
    python manage.py createsuperuser
    # Already have a superuser:
            username: limon
            password: limon123

* Run server
    python manage.py runserver

----------Running the Project---------
This project also run in Google Cloud :
For live, please visit : http://34.47.150.83:8000/

    The local server will run on http://127.0.0.1:8000/

    Visit: http://127.0.0.1:8000/admin to access the admin panel.

    API base url(local host): [127.0.0.1:8000/]

    JWT Authentication
Endpoint	Method	Description
/api/token/	POST	Get access and refresh token (Login)
/api/token/refresh/	POST	Refresh access token

| Endpoint                 | Method   | Auth | Description                     |
| ------------------------ | -------- | ---- | ------------------------------- |
| `/create_customer/`      | POST     | No   | Create a new customer           |
| `/all_customer/`         | GET      | No   | List all customers              |
| `/single_customer/<id>/` | GET, PUT | No   | Get or update a single customer |
| `/delete_customer/<id>/` | DELETE   | No   | Delete a customer               |

| Endpoint         | Method | Auth | Description       |
| ---------------- | ------ | ---- | ----------------- |
| `/product_list/` | GET    | No   | List all products |

| Endpoint                | Method | Auth | Description                             |
| ----------------------- | ------ | ---- | --------------------------------------- |
| `/create_invoice/`      | POST   | Yes  | Create a new invoice                    |
| `/all_invoice/`         | GET    | Yes  | List all invoices                       |
| `/single_invoice/<id>/` | GET    | Yes  | Get single invoice details              |
| `/update_invoice/<id>/` | PUT    | Yes  | Update invoice status (e.g., mark Paid) |






    
