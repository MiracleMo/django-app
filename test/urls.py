from django.urls import path

from . import views

app_name = "test"
urlpatterns = [
    path("", views.ListListView.as_view(), name="index"),
    path("list/<int:list_id>/", views.ItemListView.as_view(), name="list"),
    
    # CRUD patterns for ToDoLists
    path("list/add/", views.ListCreate.as_view(), name="list-add"),
    # CRUD patterns for ToDoItems
    path(
        "list/<int:list_id>/item/add/",
        views.ItemCreate.as_view(),
        name="item-add",
    ),
    path(
        "list/<int:list_id>/item/<int:pk>/",
        
        views.ItemUpdate.as_view(),
        name="item-update",
    ),

    #path("", views.home, name="home"),
    
    #path("<id:id_todo_task"),

    # settings von "<int:account"> vllt
    #path("", views.settings, name="settings"),

    #path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #path("<int:pk>/results/", views.ResultsView.as_view(), name="results"),
    #path("<int:question_id>/vote/", views.vote, name="vote"),
]