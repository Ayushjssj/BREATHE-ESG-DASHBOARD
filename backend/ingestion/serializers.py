from rest_framework import serializers
from .models import Tenant, Facility, DataSource, RawUpload, NormalizedActivity, AuditLog


class TenantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tenant
        fields = "__all__"


class FacilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Facility
        fields = "__all__"


class DataSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = DataSource
        fields = "__all__"


class RawUploadSerializer(serializers.ModelSerializer):
    class Meta:
        model = RawUpload
        fields = "__all__"


class NormalizedActivitySerializer(serializers.ModelSerializer):
    tenant_name = serializers.CharField(source="tenant.name", read_only=True)
    source_name = serializers.CharField(source="source.name", read_only=True)
    facility_name = serializers.CharField(source="facility.name", read_only=True)

    class Meta:
        model = NormalizedActivity
        fields = "__all__"


class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = "__all__"