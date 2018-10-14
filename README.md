# DBMS-project
This is the DBMS Project for HCU 2k17 batch


# Blog Basic Structure

**Changes to be made in your project file to make django_blog_it working

Download django_blog_it amd simple_pagination from here and place it in folder containing your project

eg, if your project name is 'Db_Proj' the, the project structure is like:

      Db_proj
          -Db_Proj
              -urls.py
              -settings.py
              ...
          -manage.py
          ...
          
after placing django_blog_it, it should be something like this:
      
      Db_Proj
          -django_blog_it
              -django_blog_it
                  -views.py
                  -forms.py
                  -models.py
                  -urls.py
                  ...
              -settings.py
              -urls.py
              ...
          -simple_pagination
              ...
          -Db_Proj
              -urls.py
              -settings.py
              ...
          -manage.py
now follow these steps to make your app working

1. Add app name in settings.py(in Db_proj)::

    INSTALLED_APPS = [
    
       '..................',
       'simple_pagination',
       'django_blog_it.django_blog_it',
       '..................'
    ]

2. Include the django_blog_it urls in your urls.py(in Db_Proj)::

    from django.conf.urls import include

    urlpatterns = [
    
        url('admin/', admin.site.urls),
        url('', include('django_blog_it.urls')),
    ]

now migrate the changes and run your server

You are good to go!!
