from gc import get_objects
from rest_framework import viewsets,generics
from luckywheel.models import Award, HideAward, SpacialAward
from luckywheel.serializers import AwardSerializer, HideAwardSerializer, SpacialAwardSerializer
from rest_framework.decorators import api_view
from rest_framework import response,status

class AwardApi(viewsets.ModelViewSet):
    queryset=Award.objects.all().order_by('-id')
    serializer_class=AwardSerializer
    lookup_field='text'
class SpacialAwardApi(viewsets.ModelViewSet):
    queryset=SpacialAward.objects.all()
    serializer_class=SpacialAwardSerializer
    lookup_field='count_number'

class HideAwardApi(viewsets.ModelViewSet):
    serializer_class=HideAwardSerializer
    queryset=HideAward.objects.all()

 