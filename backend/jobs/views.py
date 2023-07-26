from django.shortcuts import render, redirect
from rest_framework import generics
from .models import Job
from .serializers import JobSerializer
from .forms import JobRequirementsForm

class JobList(generics.ListAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer

def job_requirements(request):
    if request.method == 'POST':
        form = JobRequirementsForm(request.POST)
        
        if form.is_valid():
            # Process the form data and perform matching algorithm here
            job_title = form.cleaned_data['job_title']
            skills = form.cleaned_data['skills']
            location = form.cleaned_data['location']
            experience = form.cleaned_data['experience']
            
            # Perform your matching algorithm here and retrieve matching profiles
            # For demonstration purposes, let's assume we have a matching_profiles list
            # with dictionaries containing the profiles' information.
            matching_profiles = [
                {
                    'name': 'John Doe',
                    'linkedin_url': 'https://www.linkedin.com/in/johndoe/',
                },
                # Add other matching profiles here
            ]

            # Render the search results template with the matching profiles
            return render(request, 'jobs/search_results.html', {'matching_profiles': matching_profiles})
    else:
        form = JobRequirementsForm()

    return render(request, 'jobs/job_requirements_form.html', {'form': form})