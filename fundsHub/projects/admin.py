from django.contrib import admin

from fundsHub.projects.models import Project, Category, ProjectCompleteness


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name", "short_description", "funding_goal", "project_end_date")


class ProjectCompletenessAdmin(admin.ModelAdmin):
    list_display = ("min_percentage", "max_percentage", "description")


admin.site.register(Project, ProjectAdmin)
admin.site.register(Category)
admin.site.register(ProjectCompleteness, ProjectCompletenessAdmin)
