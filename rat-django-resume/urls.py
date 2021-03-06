"""rat-django-resume URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from django.views.generic import RedirectView

from django_rat import views

urlpatterns = (
    path('admin/', admin.site.urls),
    path('resume/', views.HomeIndex.as_view()),
    path('', RedirectView.as_view(url='/resume/')),
    path('resume/project-<str:pk>/', views.ProjectDetailView.as_view()),
    path('add/', views.AddProjectFormView.as_view()),
    path('resume/project-<str:pk>/edit/', views.EditProjectFormView.as_view()),

    path('resume/project-<str:pk>/delete/', views.ProjectDeleteView.as_view()),
    path('resume/thesis/', views.ThesisPdfView.as_view()),
    path('nltk/<str:text>/', views.nltk)
)
