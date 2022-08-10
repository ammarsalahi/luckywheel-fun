from django.contrib import admin
from luckywheel.models import Award, HideAward, SpacialAward

class AwardAdmin(admin.ModelAdmin):
    list_display=('text','color','lucky_award','value')
    search_fields=('text','luck_award')

class SpacialAwardAdmin(admin.ModelAdmin):
    list_display=('count_number','lucky_award','value')

class HideAwardAdmin(admin.ModelAdmin):
    list_display=('lucky_award','value')


admin.site.register(Award,AwardAdmin)
admin.site.register(SpacialAward,SpacialAwardAdmin)
admin.site.register(HideAward,HideAwardAdmin)

