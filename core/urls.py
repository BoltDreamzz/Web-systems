from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.home, name="home"),
    path("projects/", views.all_projects, name="projects"),
    path("project-detail/<project_id>/", views.project_detail, name="project_detail"),
    path("edit-comment/<int:pk>/", views.edit_comment, name="edit_comment"),
    # path("splash/", views.splash, name="splash"),
]






