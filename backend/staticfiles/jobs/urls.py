from django.urls import path
from .views import JobList
from . import views

urlpatterns = [
    path('', JobList.as_view(), name='job-list'),
    path('api/jobs/', JobList.as_view(), name='job-list'),
    path('job-requirements/', views.job_requirements, name='job-requirements'),
]
