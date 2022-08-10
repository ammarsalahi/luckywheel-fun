from django.urls import path
from rest_framework import routers
from luckywheel.api import HideAwardApi, AwardApi, SpacialAwardApi
router=routers.DefaultRouter()

router.register('award',AwardApi,basename='award')
router.register('spacialaward',SpacialAwardApi,basename='spacialaward')
router.register('hideaward',HideAwardApi,basename='hideaward')

urlpatterns=router.urls