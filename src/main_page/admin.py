from django.contrib import admin

from src.main_page.models import MainPage


class MainPageAdmin(admin.ModelAdmin):
    list_display = (
        'about_center_title',
        'about_center_description',
        'video',
        'center_page'
    )


admin.site.register(MainPage, MainPageAdmin)
