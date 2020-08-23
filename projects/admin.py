from django.contrib import admin
from .models import Developer, Project
from django.contrib.auth.models import Group
from django.urls import path
from django.http import HttpResponseRedirect

class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('surname', 'othernames', 'email', 'role',)
    list_filter = ('surname','othernames','projects',)
    ordering = ('surname',)
    search_fields = ('surname',) 
  


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'link', 'date_released','about','is_published')
    list_filter = ('title', 'date_released',)
    ordering = ('-date_released',)
    search_fields = ('title',)
    actions = ('publish_projects',)
    change_list_template = 'admin/projects/projects_change_list.html'


    """collects all the urls for this model and append the new url created
        It thus returns the customized urls
    """
    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('defaultabout/<str:about_project>/', self.change_about_empty_project),
        ]
        return custom_urls + urls

    def publish_projects(self, request, queryset):
        queryset.update(is_published = True)

        """Collects all projects with empty about page and give the about_project value collected
            via the input box
        """
    def change_about_empty_project(self, request, about_project):
        empty_about_projects = self.model.objects.filter(about = "")
        empty_about_projects.update(about = about_project)
        self.message_user(request, "Empty about projects set successfully")
        return HttpResponseRedirect("../")


    # Give description names to methods
    publish_projects.short_description = "Publish Selected Projects"


# Register your models here.
admin.site.register(Developer,DeveloperAdmin)
admin.site.register(Project, ProjectAdmin)

admin.site.unregister(Group)

admin.site.site_header = "eBayo's Corner"