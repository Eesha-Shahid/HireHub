from django.urls import path
from .views import JobList
from . import views

urlpatterns = [
    path('', views.job_requirements, name='job-requirements'),
    path('api/jobs/', JobList.as_view(), name='job-list'),
    path('job-requirements/', views.job_requirements, name='job-requirements'),
]
