from django.urls import path
from rest_framework import routers
from luckywheel.api import LuckyAwardApi, RandomAwardApi
router=routers.DefaultRouter()

router.register('luckyaward',LuckyAwardApi,basename='award')

urlpatterns=[
    path('award/',RandomAwardApi.as_view()),
]
urlpatterns+=router.urls