from rest_framework.generics import ListAPIView
from mainapp.models.profile import PersonData

from .serializers import PersonDataSerializer
from rest_framework.filters import SearchFilter


class MainAPIListAPIView(ListAPIView):
    queryset = PersonData.objects.all()
    serializer_class = PersonDataSerializer

    filter_backends = [SearchFilter]
    search_fields = ['first_name', ] # add fields to include in search
