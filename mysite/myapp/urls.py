from django.urls import path
from myapp.views import (
    # index,
    # indexItem,
    add_item,
    update_item,
    delete_item,
    about,
    contacts,
    ProductListView,
    ProductDetailView,
)

app_name = "myapp"  # namespace


urlpatterns = [
    # http://127.0.0.1:8000/myapp/
    # path("", index, name='index'),
    path("", ProductListView.as_view(), name="index"),
    # path("<int:my_id>/", indexItem, name="detail"),
    path("<int:pk>/", ProductDetailView.as_view(), name="detail"),
    # http://127.0.0.1:8000/myapp/
    path("additem/", add_item, name="add_item"),
    path("updateitem/<int:my_id>/", update_item, name="update_item"),
    path("deleteitem/<int:my_id>/", delete_item, name="delete_item"),
    path("about/", about, name="about"),
    path("contacts/", contacts, name="contacts"),
]
