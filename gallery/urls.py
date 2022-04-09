from django.urls import path
from . import views

app_name = 'gallery'

urlpatterns = [
    path('', views.gallery_list, name='gallery_list'),
    # path('gallery2/<int:pk>', views.gallery_view, name="gallery_view"),
    # path('', views.GalleryListView.as_view(), name='gallery_list'),
    path('add_event/', views.add_gallery_event, name='add_event'),
    path('<int:id>/<name>/', views.gallery_detail, name='gallery_detail')

]

