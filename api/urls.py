from django.urls import path
from . import views

urlpatterns = [
    path("keys/", views.KeyList.as_view(), name="key_list"),
    path("add/", views.AddKey.as_view(), name="add_key"),
    path("update/<str:key>/", views.UpDelKey.as_view(), name="update_key"),
    path("delete/<str:key>/", views.UpDelKey.as_view(), name="delete_key"),
]
