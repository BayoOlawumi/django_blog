from django.urls import path
from . import views

urlpatterns = [
    path('', views.index , name = 'boot'),
    path('real', views.real_index , name = 'ebayo'),
    path('list/', views.project_list, name ='projects'),
    path('new/', views.new_project, name = 'new-projects'),
    path('<int:id>/', views.find_project, name ='edit-projects'),
    path('list/search/', views.search_project, name = 'search-project')
]