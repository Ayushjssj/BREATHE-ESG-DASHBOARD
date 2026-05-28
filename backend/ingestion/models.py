from django.db import models
from django.contrib.auth.models import User


class Tenant(models.Model):
    name = models.CharField(max_length=255)
    industry = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.name


class Facility(models.Model):
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE, related_name="facilities")
    name = models.CharField(max_length=255)
    plant_code = models.CharField(max_length=50, blank=True, null=True)
    location = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.name


class DataSource(models.Model):
    SOURCE_CHOICES = [
        ("SAP", "SAP"),
        ("UTILITY", "Utility"),
        ("TRAVEL", "Travel"),
    ]

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    source_type = models.CharField(max_length=20, choices=SOURCE_CHOICES)
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.source_type} - {self.name}"


class RawUpload(models.Model):
    STATUS_CHOICES = [
        ("UPLOADED", "Uploaded"),
        ("PROCESSED", "Processed"),
        ("FAILED", "Failed"),
    ]

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    file = models.FileField(upload_to="uploads/")
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="UPLOADED")
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.source.source_type} upload {self.id}"


class NormalizedActivity(models.Model):
    STATUS_CHOICES = [
        ("PENDING", "Pending Review"),
        ("FLAGGED", "Flagged"),
        ("APPROVED", "Approved"),
        ("LOCKED", "Locked for Audit"),
    ]

    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)
    facility = models.ForeignKey(Facility, on_delete=models.SET_NULL, null=True, blank=True)
    source = models.ForeignKey(DataSource, on_delete=models.CASCADE)
    raw_upload = models.ForeignKey(RawUpload, on_delete=models.CASCADE, null=True, blank=True)

    source_type = models.CharField(max_length=20)
    scope = models.CharField(max_length=20)

    activity_type = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    quantity = models.FloatField()
    original_unit = models.CharField(max_length=50)

    normalized_quantity = models.FloatField()
    normalized_unit = models.CharField(max_length=50)

    period_start = models.DateField()
    period_end = models.DateField()

    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default="PENDING")
    suspicious_reason = models.TextField(blank=True, null=True)

    source_row_number = models.IntegerField(null=True, blank=True)
    source_reference = models.CharField(max_length=255, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    approved_at = models.DateTimeField(null=True, blank=True)
    locked_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.activity_type} - {self.normalized_quantity} {self.normalized_unit}"


class AuditLog(models.Model):
    activity = models.ForeignKey(NormalizedActivity, on_delete=models.CASCADE, related_name="audit_logs")
    action = models.CharField(max_length=100)
    old_status = models.CharField(max_length=50, blank=True, null=True)
    new_status = models.CharField(max_length=50, blank=True, null=True)
    note = models.TextField(blank=True, null=True)
    changed_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    changed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.action} - Activity {self.activity.id}"