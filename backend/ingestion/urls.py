from django.urls import path
from . import views

urlpatterns = [
    path("upload/", views.upload_csv),
    path("activities/", views.activity_list),

    path(
        "activities/<int:activity_id>/approve/",
        views.approve_activity
    ),

    path(
        "activities/<int:activity_id>/lock/",
        views.lock_activity
    ),
]