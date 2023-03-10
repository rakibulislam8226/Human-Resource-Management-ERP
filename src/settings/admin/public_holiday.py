from django.contrib import admin
from settings.models import PublicHoliday, PublicHolidayDate

class PublicHolidayDateInline(admin.TabularInline):
    model = PublicHolidayDate
    extra = 1

@admin.register(PublicHoliday)
class PublicHolidayAdmin(admin.ModelAdmin):
    list_display = ['title', 'days']
    inlines = (PublicHolidayDateInline,)

    def days(self, obj):
        total_days = obj.public_holiday.count()
        date_list = [dt for dt in obj.public_holiday.values_list('date', flat=True)]
        print(date_list)
        return "({}) \n {}".format(total_days, date_list)

    


