from django.db import models


class ApprovalCookies(models.Model):
    approval_uid = models.CharField(
        max_length=255,
        unique=True,
    )
    approval_at = models.DateTimeField(
        auto_now_add=True,
    )
    user_agent = models.CharField(
        max_length=255,
    )
