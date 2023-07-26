from django import forms

class JobRequirementsForm(forms.Form):
    job_title = forms.CharField(label='Job Title', max_length=100)
    skills = forms.CharField(label='Skills', max_length=200)
    location = forms.CharField(label='Location', max_length=100)
    experience = forms.CharField(label='Experience (in years)', max_length=50)  # You can use IntegerField if experience is numeric
