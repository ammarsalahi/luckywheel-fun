from django.contrib import admin
from luckywheel.models import LuckyAward

class LuckyAwardAdmin(admin.ModelAdmin):
    list_display=('text','color','lucky_award','value','active')
    search_fields=('text','luck_award','value')



admin.site.register(LuckyAward,LuckyAwardAdmin)


