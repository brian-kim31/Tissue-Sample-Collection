from django.urls import path
from .views import SignUpView, ProfileView, CollectionListView, CollectionDetailView, SampleCreateView, CollectionCreateView

urlpatterns = [
    path('dashboard/', CollectionListView.as_view(), name='home'),
    path("signup/", SignUpView.as_view(), name="signup"),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('collection/<int:pk>/', CollectionDetailView.as_view(), name='collection_details'),
    path('collection/<int:collection_id>/add_sample/', SampleCreateView.as_view(), name='add_sample'),
    path('create_collection/', CollectionCreateView.as_view(), name='create_collection'),
]
