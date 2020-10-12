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
from questionbox.views import answer_delete
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from questionbox import views as questionbox_views
# from questionbox.models import Question, Answer


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')), # path for registration redux
    path('', questionbox_views.landingpage, name='landingpage'), # path for landing page
    path('accounts/profile', questionbox_views.landingpage, name='landingpage'),

    # questions
    path('questionbox/question_list', questionbox_views.question_list, name='question_list'), # question list
    path('questionbox/question_create', questionbox_views.question_create, name='question_create'), # question create/ask
    path('questionbox/question_search', questionbox_views.question_search, name='question_search'), # question search
    path('questionbox/question_detail/<int:question_pk>', questionbox_views.question_detail, name='question_detail'), # question detail
    path('questionbox/question_delete/<int:pk>', questionbox_views.question_delete, name='question_delete'), # question delete

    # answers

    path('questionbox/answer_list', questionbox_views.answer_list, name='answer_list'), # answer list
    path('questionbox/answer_create', questionbox_views.answer_create, name='answer_create'), # answer create
    path('questionbox/answer_search', questionbox_views.answer_search, name='answer_search'), # answer search
    path('questionbox/answer_detail', questionbox_views.answer_detail, name='answer_detail'), # answer detail
    path('questionbox/answer_delete/<int:answer_pk>', questionbox_views.answer_delete, name="answer_delete"), # answer delete

   


]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
