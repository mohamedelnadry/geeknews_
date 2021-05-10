from django.urls import path
from .views import SearchAPIView,details,AuthorDetails,AuthorDetailsByName

app_name = "myapp"

urlpatterns = [
    path('', SearchAPIView.as_view(), name = 'SearchAPIView'),
    path('details/<int:post_id>', details.as_view(), name = 'details'),
    path('AuthorDetails/<int:author_id>', AuthorDetails.as_view(), name = 'AuthorDetails'),
    path('AuthorDetailsByName/<str:author_name>', AuthorDetailsByName.as_view(), name = 'AuthorDetailsByName')


]
