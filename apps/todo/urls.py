from django.urls import path
from apps.todo.views import CreateTaskAPIView, TaskViewSet, RetrieveTaskAPIView, UpdateTaskAPIView, DeleteTaskAPIView

urlpatterns = [
    path('', TaskViewSet.as_view(), name="api_news"),
    path('create/', CreateTaskAPIView.as_view(), name="api_news_create"),
    path('<int:pk>/', RetrieveTaskAPIView.as_view(), name="api_news_detail"),
    path('update/<int:pk>/', UpdateTaskAPIView.as_view(), name="api_news_update"),
    path('destroy/<int:pk>/', DeleteTaskAPIView.as_view(), name="api_news_destroy"),
]