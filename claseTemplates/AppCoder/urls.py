"""
URL configuration for claseTemplates project.

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

from django.urls import path
from AppCoder.views import CreateTrekking , TrekkingDetail  , TrekkingList, search_trekking, search_trekking_title, AboutMe, comment, edit_trekking_image

urlpatterns = [
    path('trekking/list/', TrekkingList.as_view(), name="TrekkingList"),
    path('create_trekking/', CreateTrekking.as_view(), name="CreateTrekking"),
    path('trekking/<int:pk>', TrekkingDetail.as_view(), name="TrekkingDetail"),
    path('edit_trekking/<int:trekking_id>', edit_trekking_image, name="EditTrekking"),
    path('trekking/comment', comment, name="TrekkingComment"),
    path('search_trekking/', search_trekking, name="SearchTrekking"),
    path('search_trekking_title/', search_trekking_title, name="SearchTrekkingTitle"),
    path('about_me/', AboutMe.as_view(), name="AboutMe")
]

    
















