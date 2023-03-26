from django.contrib import admin

from .models import School, Workshops, Kindergarten, Eis, Volunteer, \
    CenterPage, SpecialistsPage, Specialist, EducationalSite


class SchoolAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'image'
    )


class WorkshopsAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'image'
    )


class KindergartenAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'image'
    )


class EisAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'image'
    )


class VolunteersAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'middle_name',
        'image',
        'email',
        'phone',
        'job',
        'filing_date'
    )


class CenterPageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'image',
        'opening_year',
        'children_number',
        'families_number',
    )


class SpecialistsPageAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'image',
    )


class SpecialistsAdmin(admin.ModelAdmin):
    list_display = (
        'last_name',
        'first_name',
        'middle_name',
        'image',
        'position',
        'info',
    )
    prepopulated_fields = {"slug": ("last_name", "first_name", "middle_name")}


class EducationalSiteAdmin(admin.ModelAdmin):
    list_display = (
        'url',
    )


admin.site.register(School, SchoolAdmin)
admin.site.register(Workshops, WorkshopsAdmin)
admin.site.register(Kindergarten, KindergartenAdmin)
admin.site.register(Eis, EisAdmin)
admin.site.register(Volunteer, VolunteersAdmin)
admin.site.register(CenterPage, CenterPageAdmin)
admin.site.register(SpecialistsPage, SpecialistsPageAdmin)
admin.site.register(Specialist, SpecialistsAdmin)
admin.site.register(EducationalSite, EducationalSiteAdmin)
