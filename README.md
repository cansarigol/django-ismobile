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

Include to your INSTALLED_APPS:

```
INSTALLED_APPS = (
    ...
    'ismobile',
    ...
)
```

Include MobileControlMiddleware into your MIDDLEWARE:

```
MIDDLEWARE = (
    ...
    'ismobile.middleware.MobileControlMiddleware',
    ...
)
```