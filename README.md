# django-ismobile


"is_mobile" middleware for Django

## Requirements
Requires Django 2.0 or later.

## Installing

Install with `pip` or your favorite PyPi package manager.

```
pip install django-ismobile
```

## Using

Include MobileControlMiddleware into your MIDDLEWARE:

```
MIDDLEWARE = (
    ...
    'ismobile.middleware.MobileControlMiddleware',
    ...
)
```

## Config

In order to change request attribute name, 
set **IS_MOBILE_ATTR_NAME** in django **settings** file.

```
IS_MOBILE_ATTR_NAME="custom_name"
```