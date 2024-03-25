from django.urls import path
from to_do_app.views import (
    HomeView,
    TaskCompleteActionView,
    TaskCompletedView,
    TaskDeleteView,
    TaskFormView,
    TaskUpdateView,
)


urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("complete-tasks", TaskCompletedView.as_view(), name="complete_tasks"),
    path("complete-tasks/<int:pk>", TaskCompleteActionView.as_view(), name="done_task"),
    path("add-task/", TaskFormView.as_view(), name="add_task"),
    path("edit-task/<int:pk>", TaskUpdateView.as_view(), name="edit_task"),
    path("delete-task/<int:pk>", TaskDeleteView.as_view(), name="delete_task"),
]
