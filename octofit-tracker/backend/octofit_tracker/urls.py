"""octofit_tracker URL Configuration

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
import os
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from octofit_tracker import views

# Create a router and register viewsets
router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'activities', views.ActivityViewSet)
router.register(r'leaderboard', views.LeaderboardViewSet)
router.register(r'workouts', views.WorkoutViewSet)


@api_view(['GET'])
def api_root_codespace(request, format=None):
    """
    API root endpoint that returns full URLs for codespace environment.
    """
    codespace_name = os.environ.get('CODESPACE_NAME')
    
    if codespace_name:
        # Running in GitHub Codespaces
        base_url = f'https://{codespace_name}-8000.app.github.dev'
    else:
        # Running locally
        base_url = f'{request.scheme}://{request.get_host()}'
    
    return Response({
        'users': f'{base_url}/api/users/',
        'teams': f'{base_url}/api/teams/',
        'activities': f'{base_url}/api/activities/',
        'leaderboard': f'{base_url}/api/leaderboard/',
        'workouts': f'{base_url}/api/workouts/',
    })


urlpatterns = [
    path('', api_root_codespace, name='api-root'),
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
