# BACKEND ASSIGNEMENT

## Getting Started

### There are 2 app Users and Posts

#### Configure Postgresql according to your DB settings

#### Create Virtual Env to run our application

```
pyhton3 -m venv env
```

#### Migrate all migrations

```
python3 manage.py migrate
```

#### Create SuperUser

```
python3 manage.py createsuperuser
```

### Project is ready to use

#### APIS
```
MEHTOD |  API_NAME
POST   |  http://localhost:8000/api/token/
POST   |  http://localhost:8000/api/token/refresh/
POST   |  http://localhost:8000/posts/api/create/
POST   |  http://localhost:8000/users/api/register/
```
