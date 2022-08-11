from cgitb import text
from rest_framework import serializers
from luckywheel.models import LuckyAward
import random

class LuckyAwardSerializer(serializers.ModelSerializer):
    award=serializers.CharField(read_only=True,source='get_award')   
    class Meta:
        model=LuckyAward
        fields=('id','text','color','award','active')


