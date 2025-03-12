from django.urls import include,path
from rest_framework import routers #do automatycznego generowania tras URL dla widoków opartych na widokach zestawów (ViewSets), bez recznego ustawiania
from .views import VoteViewSet,IdeaViewSet

router = routers.DefaultRouter()
router.register(r'ideas', IdeaViewSet)
router.register(r'votes', VoteViewSet)

urlpatterns = [
    path('api/',include(router.urls)),
    path('api-auth/',include('rest_framework.urls', namespace='rest_framework')),
]
#namespace to taki prefix

