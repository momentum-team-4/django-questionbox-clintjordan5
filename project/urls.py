"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from os import name
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from questionbox import views as questionbox_views
# from questionbox.models import Question, Answer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')), # path for registration redux
    path('', questionbox_views.landingpage, name='landingpage'), # path for landing page

    # questions
    path('questionbox/question_list', questionbox_views.question_list, name='question_list'), # question list
    path('questionbox/question_create', questionbox_views.question_create, name='question_create'), # question create/ask
    path('questionbox/question_search', questionbox_views.question_search, name='question_search'), # question search

    # answers

    path('questionbox/answer_list', questionbox_views.answer_list, name='answer_list'), # answer list
    path('questionbox/answer_create', questionbox_views.answer_create, name='answer_create'), # answer create
    path('questionbox/answer_search', questionbox_views.answer_search, name='answer_search'), # answer search

    # should login path go to http://127.0.0.1:8000/accounts/login/?


]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
