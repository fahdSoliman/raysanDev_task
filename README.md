# RaysanDev task

User management API system with restricted permissions on API.
This project was developed using Django & Django Rest Framework, & simpleJWT.

## Requirement
* Python 3.10+ (tested on Python 3.13.9).
* Virtual environment (recommended).

Packages and their versions can be reached in the file:

`raysan_project/requirement.txt`


## Setup
1. cloning the repository on any folder.
```
git clone https://github.com/fahdSoliman/raysanDev_task.git
cd raysanDev_task/raysan_project
```
2. Create and activate a virtual environment (optional but recommended)
```
python -m venv venv
venv\Script\activate # to activate
```
3. Installing packages after going inside the *raysan_project* folder, then execute the command:
```
pip install -r requirements.txt
```
4. Run migration database command:
```
python manage.py migrate
```
5. Create SuperUser "admin" using:
```
python manage.py createsuperuser
```
6. then run the server
```
python manage.py runserver
```

After running the server, you can access the admin webpage at http://localhost:8000/admin/. It's easy to create users for testing from there if you want.


## Authentication & Permissions

In this project, we used simpleJWT to generate Bearer tokens to validate authenticated users and give them the right permissions depending to thier rule on the system.

We have two states of users reaching APIs:
1. Authenticated, no JWT provided.
2. Not authenticated, valid JWT access token provided.

Also, we have 3 levels of permissions on APIs:
1. Admin Only.
2. Owner Only.
3. Admin Or Owner.

## API endpoints description

**`POST http://localhost:8000/api/token/`**

To optain *'refresh and access JWT tokens'* using username & password.
- Authentication: Not Authenticated
- Permissions: 

**`POST http://localhost:8000/api/token/refresh/`**

To get new *'access token'*.
- Authentication: Authenticated
- Permissions: Admin Or Owner.


**`GET http://localhost:8000/api/users/`**

To retrive list of users data.
- Authentication: Authenticated
- Permissions: Admin Only.

**`GET http://localhost:8000/api/users/create/`**

To create new user.
- Authentication: Authenticated
- Permissions: Admin Only.

**`GET http://localhost:8000/api/users/<id:int>/`**

To retrive specific user data by ID.
- Authentication: Authenticated
- Permissions: Admin Or Owner.

**`PUT http://localhost:8000/api/user/<id:int>/update/`**

To update specific user data by ID.
- Authentication: Authenticated
- Permissions: Admin Or Owner.

**`DELETE http://localhost:8000/api/user/<id:int>/delete/`**

To delete specific user data by ID.
- Authentication: Authenticated
- Permissions: Admin Only.

**`PUT http://localhost:8000/api/user/<id:int>/change-password/`**

To update user password by ID.
- Authentication: Authenticated
- Permissions: Owner Only.

## Notes
* JWT must be sent in the `Authorization` header:
```
Authorization: Bearer <access_token>
```
* Passwords are securely hashed using Django’s built-in password hashing system.
* Object-level permissions are enforced to prevent unauthorized data access.

## Author
Developed by Fahd Soliman
