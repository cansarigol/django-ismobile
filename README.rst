=====
django-ismobile
=====

A basic "is_mobile" middleware Django app

1. Install using pip:
    pip install django-ismobile

2. Include to your INSTALLED_APPS:
    INSTALLED_APPS = [
        ...
        'ismobile',
    ]

3. Include MobileControlMiddleware to your MIDDLEWARE:
    MIDDLEWARE_CLASSES = (
        ...
        'ismobile.middleware.MobileControlMiddleware',
    )