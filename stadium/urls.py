from django.urls import path
from .views import (CreateFieldView,ListFieldView,DetailFieldView,UpdateFieldView,DeleteFieldsView,
                    CreateBronView,ListBronView,DetailBronView,UpdateBronView,DeleteBronView,UnbronTimeView)

urlpatterns = [
    # Field urls
    path('createField/<int:pk>/',CreateFieldView.as_view()),
    path('allField/',ListFieldView.as_view()),
    path('detailField/<int:pk>/',DetailFieldView.as_view()),
    path('updateField/<int:pk>/',UpdateFieldView.as_view()),
    path('deleteField/<int:pk>/',DeleteFieldsView.as_view()),
    # Bron urls
    path('createBron/<int:pk>/',CreateBronView.as_view()),
    path('allBron/',ListBronView.as_view()),
    path('detailBron/<int:pk>',DetailBronView.as_view()),
    path('updateBron/<int:pk>/',UpdateBronView.as_view()),
    path('deleteBron/<int:pk>/',DeleteBronView.as_view()),
    path('unbrontime/<int:pk>/',UnbronTimeView.as_view())
    
]