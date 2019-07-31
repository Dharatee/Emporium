from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls'), name="index"),
   # path('', include('user.urls'), name ="user"),
   path('user/', include('user.urls'), name = "user")
]
