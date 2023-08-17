from datetime import date, timedelta
from django import forms
from .models import Project


class CreateProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ('user', 'donated')
        labels = {'name': 'Name:',
                  'short_description': 'Short Description:',
                  'picture': 'Picture:',
                  'funding_goal': 'Funding Goal:',
                  'long_description': 'Long Description:',
                  'project_end_date': 'Project End Date:',
                  }

        widgets = {
            'project_end_date': forms.DateInput(attrs={'type': 'date'}),
        }

    def clean_project_end_date(self):
        project_end_date = self.cleaned_data.get('project_end_date')
        tomorrow = date.today() + timedelta(days=1)
        if project_end_date and project_end_date < tomorrow:
            raise forms.ValidationError("The project end date should be at least tomorrow.")
        return project_end_date


class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'short_description', 'long_description', 'picture')
        labels = {'name': 'Name:',
                  'short_description': 'Short Description:',
                  'long_description': 'Long Description',
                  'picture': 'Picture',
                  }

