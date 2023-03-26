from django.contrib import admin

from src.assistance.models import Job, ReportType, Report


class JobAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ReportTypeAdmin(admin.ModelAdmin):
    list_display = (
        'name',
    )


class ReportAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'file',
        'reporttype_id'
    )


admin.site.register(Job, JobAdmin)
admin.site.register(ReportType, ReportTypeAdmin)
admin.site.register(Report, ReportAdmin)
