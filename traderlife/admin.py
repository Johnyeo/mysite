from django.contrib import admin

# Register your models here.
from traderlife.models import Market_good, My_good, Event


class MarketGoodAdmin(admin.ModelAdmin):
    list_display = ['name','base','count','status','flag','create_time','offset']

class MyGoodAdmin(admin.ModelAdmin):
    list_display = ['name', 'price', 'count', 'status','flag','username','create_time']

class EventAdmin(admin.ModelAdmin):
    list_display = ['name','comment','type','status','flag','create_time']

admin.site.register(Market_good, MarketGoodAdmin)
admin.site.register(My_good, MyGoodAdmin)
admin.site.register(Event, EventAdmin)