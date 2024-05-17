from django import forms
from .models import Portfolio,Project


class PortfolioForm(forms.ModelForm):
    class Meta:
        model = Portfolio
        fields = ['title', 'description', 'project_showcase', 'work_experience', 'education', 'certifications']
class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields= ['title','description','image','github_link','demo_link']
