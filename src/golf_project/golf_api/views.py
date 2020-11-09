from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import viewsets
from . import serializers, models

# Create your views here.

class UserProfileViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating profiles."""

    serializer_class = serializers.UserProfileSerializer
    queryset = models.UserProfile.objects.all()


class CourseViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating golf courses."""

    serializer_class = serializers.CourseSerializer
    queryset = models.Course.objects.all()


class HoleViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating holes in courses."""

    serializer_class = serializers.HoleSerializer
    queryset = models.Hole.objects.all()


class MatchStrikeViewSet(viewsets.ModelViewSet):
    """Handles creating, reading and updating match strikes."""

    serializer_class = serializers.MatchStrikeSerializer
    queryset = models.MatchStrike.objects.all()
