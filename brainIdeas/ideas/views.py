from .models import Idea, Vote
from rest_framework import viewsets #widoki w formie albo poj. funkcji lub widok z parametrami
from .serializer import IdeaSerializer, VoteSerializer

class IdeaViewSet(viewsets.ModelViewSet):
    queryset = Idea.objects.all()
    serializer_class = IdeaSerializer

class VoteViewSet(viewsets.ModelViewSet):
    queryset = Vote.objects.all()
    serializer_class = VoteSerializer