"""
URL configuration for Aakashvaani project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from AakashBlog import views

from django.contrib import admin

# Customize the admin site header, title, and index title
admin.site.site_header = "AakashVaani"   # Replace with your desired site header
admin.site.site_title = "AakashVaani"     # Replace with your desired site title
admin.site.index_title = "AakashVaani"   # Replace with your desired index title

urlpatterns = [
    path('admin/', admin.site.urls),
    # in place of "admin/" we use the choice url address that land on the demanded page by the user

    # ... other app URLs ...
    path('aboutus/', views.aboutus),
    
    path('course/', views.course),
    path('course/<courseId>', views.courseDetails),

    # path ("home",views.home),

    path ('',views.homepage),

    path ('login/',views.login),

    path('signup/',views.register),


]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', include("AakashBlog.urls"))
# ]
