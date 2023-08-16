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


class ProjectEditForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ('name', 'short_description')
        labels = {'name': 'Name:',
                  'short_description': 'Short Description:',
                  }

        widgets = {
            'username': forms.TextInput(attrs={'readonly': 'readonly'}),
        }
