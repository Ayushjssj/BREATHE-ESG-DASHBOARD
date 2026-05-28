from django.contrib import admin
from .models import Tenant, Facility, DataSource, RawUpload, NormalizedActivity, AuditLog

admin.site.register(Tenant)
admin.site.register(Facility)
admin.site.register(DataSource)
admin.site.register(RawUpload)
admin.site.register(NormalizedActivity)
admin.site.register(AuditLog)