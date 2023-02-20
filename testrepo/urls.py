"""testrepo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.urls import path

from strawberry.django.views import AsyncGraphQLView
from .schema import schema

class CustomAsyncGraphQLView(AsyncGraphQLView):
    async def process_result(
      self, request, result
  ):
      return await super().process_result(request, result)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', CustomAsyncGraphQLView.as_view(schema=schema))
]
