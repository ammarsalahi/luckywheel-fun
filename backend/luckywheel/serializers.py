from cgitb import text
from rest_framework import serializers
from luckywheel.models import Award, HideAward, SpacialAward


class AwardSerializer(serializers.ModelSerializer):
    award=serializers.CharField(read_only=True,source='get_award')    
    class Meta:
        model=Award
        fields=('id','text','color','award')


class SpacialAwardSerializer(serializers.ModelSerializer):
    award=serializers.CharField(read_only=True,source="get_award")
    class Meta:
        model=SpacialAward
        fields=('count_number','award','id')     


class HideAwardSerializer(serializers.ModelSerializer):
    award=serializers.CharField(read_only=True,source="get_award")
    class Meta:
        model=HideAward
        fields=('award','id') 