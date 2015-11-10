Socialist
===================
[![Django 1.8.4](http://img.shields.io/badge/Django-1.8.4-0C4B33.svg)](https://www.djangoproject.com/)
[![MIT License](https://img.shields.io/cocoapods/l/AFNetworking.svg)](http://opensource.org/licenses/MIT)
[![Bower](https://img.shields.io/bower/v/bootstrap.svg)]()
[![PyPI](https://img.shields.io/pypi/wheel/Django.svg)]()
[![PyPI](https://img.shields.io/pypi/pyversions/Django.svg)]()

Socialist OAuth2.0 Authentication. It is built with [Python][2]3.4 using the [Django Web Framework][1]1.8.4.
And all of my Django Experience will be in this project .

<i class="icon-pencil"></i> Quick Installation :
===============================================
for quick installation of virtualenv and all dependencies you can use below commands :
	
	$ mkvirtualenv -p $(which python3.4) Socialist-venv
	$ workon Socialist-venv
	$ pip install -r https://raw.githubusercontent.com/LordK1/Starter/master/requirements/tmp.txt
	$ django-admin.py startproject --template=https://github.com/LordK1/Starter/archive/master.zip  --extension=py,rst,md,txt,html,json,env Socialist
	# Make sure of running Postgres.app 
	$ createdb Socialist-DB
	$ cd Socialist/Socialist/settings/
	# Customize your environment variables
	$ mv local.sample.env local.env & gedit local.env
	# for install static files with bower 
	$ bower install 
 	$ python manage.py runserver

Goodlier.

Authentication with OAuth2.0
----------------------------------
Why would we want token based authentication? For many reasons:

mobile ready
stateless
cross-domain
csrf
etc.

from httplambda blog.

    $curl -X POST -d “grant_type=password&username=k1@k1.com&password=123456” -u”G0paPtv5HkDvbFMNgI1TVwlIyvkiH8UlkSPykrS1:uMnDyKDsHCvfSYNNZAsAo8clj0qWVUS6GKrlIYrlI6YPxWPuDYT60MgbJAAzLnK8eoIHzK5YHuAL1ssBXyUtDjAg1GZCLXawgd0hkYDe0FGjRkhGdkcHkS63rFD2WDSB” http://localhost:8000/oauth/token/
	$curl -X POST -d “grant_type=password&username=<user_name>&password=<password>” -u”<client_id>:<client_secret>” http://localhost:8000/o/token/

TODO :
==========
 - add thumbnails for all applications
 - add tags for post
 - check class based views
 - add commenting ability for posts
 - add voting and rating process
 - go deeper and deeper on Django development
 
Features:
===========

 - [Django Rest Framework][4]
 - [Django OAuth Toolkit][6]
 - [Python Social Auth][7]
 - [Django Starter Template][8]

---------------------------------------------------------------------------------
References
-------------
1. Thanks and Inspired by [httplambda.com][3]
2. [Felix Descoteaux][5]
3. [Python Social Auth][7]
4. [Django Starter Template][8]

[1]: https://www.python.org/
[2]: https://www.djangoproject.com/
[3]:http://httplambda.com/a-rest-api-with-django-and-oauthw-authentication/
[4]:http://www.django-rest-framework.org/
[5]:https://github.com/felix-d
[6]:https://github.com/evonove/django-oauth-toolkit
[7]:http://psa.matiasaguirre.net/
[8]:https://github.com/LordK1/Starter