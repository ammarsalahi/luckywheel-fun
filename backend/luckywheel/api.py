import random
from rest_framework import viewsets,views
from luckywheel.models import LuckyAward
from luckywheel.serializers import LuckyAwardSerializer
from rest_framework.decorators import api_view
from rest_framework import response,status

class LuckyAwardApi(viewsets.ModelViewSet):
    queryset=LuckyAward.objects.all()
    serializer_class=LuckyAwardSerializer
    lookup_field='text'

class RandomAwardApi(views.APIView):
    def get(self,request,format=None):
        try:
            obj=LuckyAward.objects.filter(active=True)
            newobj=random.choice(obj)
            data={
                'award':newobj.text
            }
            return response.Response(data=data,status=status.HTTP_200_OK)    
        except IndexError:
            return response.Response(status=status.HTTP_404_NOT_FOUND)
 