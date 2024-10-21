**Django Features**
- The admin site
- Object-relational mapper (ORM)
- Authentication
- Caching

```pip install pipenv```

Inside the project env type:
```pipenv install django```

Open the Code environment for Django 
```pipenv shell```

Use Django admin to initialise the project as follows
```django-admin startproject BlogApp```

If you are outside the directory or below code throws an error in windows Use following command - Optional[^1]
```cd BlogApp```

**File Structure inside the Django app**

    BlogApp
    |- __init__.py          defines the directory as a package
    |- asgi.py              module used for deployment
    |- settings.py          module to define the application settings
    |- urls.py              module to define urls of our applications
    |- wsgi.py              module used for deployment
   manage.py               Wrapper around DjangoAdmin (alias of django-admin == manage.py)



If you are running the below command it will generate error as settings are not defined in django-admin scope. So this can be handled by `manage.py` command instead. Try to see the error generated.
```django-admin runserver```

In Django every functionality is coded in an app. In `settings.py` default apps seen are:
- django.contrib.admin
    For managing the data
- django.contrib.auth
    For authenticating users
- django.contrib.contenttypes
- django.contrib.sessions
    Legacy app which can be deleted as they are deprecated features in modern projects.It was Temporary session on server for managing users data. In present times user data is handled at the client side itself
- django.contrib.staticfiles
    For serving Images, css and multimedia files

**Ideal project structure**

    playground
       migrations              Folder for generating view tables from the database
       |- \__init__.py          defines the directory as a package
       |- admin.py             define how admin interface for the app will look like
       |- apps.py              module to configure the apps >> linking to business logic
       |- models.py            module to present data to the users from the database
       |- tests.py             module to write the unit tests
       |- urls.py              module to define urls of our applications
       |- views.py             module for handling the requests from the clients
      manage.py               Wrapper around DjangoAdmin (alias of django-admin == manage.py)
    blogapp
        |- \__init__.py          defines the directory as a package
        |- asgi.py              module used for deployment
        |- settings.py          module to define the application settings
        |- urls.py              module to define urls of our applications
        |- wsgi.py              module used for deployment
       manage.py               Wrapper around DjangoAdmin (alias of django-admin == manage.py)

Every module added needs to be mentioned in the `settings.py` app section
- eg: 'BlogApp'

Create the server using below command
```python manage.py runserver 9000```
Note: Everytime You close the IDE use above command to run the server instance instead of using manage.py runserver (If getting errors)[^2]

[Click on the following URL](http://127.0.0.1:9000/)

To search your virtual environment from the terminal you can type
```django-admin runserver```

Copy the address and user following key combination ctrl+shift+p add `/bin/python`
```C:\Users\khull\.virtualenvs\Blog_API-T_bQ9FCw\bin\python```

Settings.py is an app that uses a huge list of settings. In app settings following are the use cases
admin >> provides admin interface or manage the data
auth >> authenticating the users
session >> legacy feature, Temp memory on server managing users data (can be deleted)
static files >> Images on the data


Open a new Terminal to avoid getting errors while running python manage.py runserver


**Create a views module in playground**

**Create a urls module in playground**
    Following is the path function parameters required. `:` is type annotation a new feature in python. `->` represents a return parameter.    
```path(route: str, views: (*args: Any, **kwargs: Any) -> HttpResponseBase) -> URLpattern```
Type following code to add a url path to call `say_hello()`
```from django.urls import path
   from . import views
   #URLConf
   urlpatterns =[
   path('playground/hello', views.say_hello)
]```

Instead of writing playground/home or playground/someurl everytime we can provide a provision to by default include the playground home url in the BlogApp/urls.py module
import `include` function in the file and add the playground path using include function as follows
```from django.contrib import admin
from django.urls import path, include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls'))
]```

In `playground/urls.py` the path function will change as follows
```path('playground/hello', views.say_hello)```


(More about Middlewares)[https://techvillian.hashnode.dev/middleware-in-django-the-unseen-hand-of-your-backend-development]