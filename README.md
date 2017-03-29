#django-project-template


##Django 1.6+ Base Template


Basic template

###How to use this template to create your project


1. Create your virtualenv
2. Install Django
3. $ django-admin.py startproject --template https://github.com/lucassimon/django-project-template/zipball/master --extension py,md projectname
4. $ cd projectname
5. $ pip install -r requirements/dev.txt
6. $ ./manage.py syncdb --settings=projectname.settings.dev
7. $ ./manage.py runserver --settings=projectname.settings.dev

###Adding an app

8. $ python manage.py startapp --template https://github.com/lucassimon/django-app-template/zipball/master app_name
9. add app_name to INSTALLED_APPS projectname/settings/base.py

### About

### Prerequisites

- Python >= 2.5
- pip
- virtualenv (virtualenvwrapper is recommended for use during development)


