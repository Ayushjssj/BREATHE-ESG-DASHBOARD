from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import (
    Tenant,
    DataSource,
    Facility,
    NormalizedActivity
)
from .serializers import NormalizedActivitySerializer

import pandas as pd


@api_view(["POST"])
def upload_csv(request):

    try:
        tenant_id = request.POST.get("tenant_id")
        source_id = request.POST.get("source_id")
        file = request.FILES.get("file")

        if not tenant_id or not source_id or not file:
            return Response(
                {"error": "tenant_id, source_id and file are required"},
                status=status.HTTP_400_BAD_REQUEST
            )

        tenant = Tenant.objects.get(id=tenant_id)
        source = DataSource.objects.get(id=source_id)

        df = pd.read_csv(file)

        created_rows = 0
        failed_rows = []

        for index, row in df.iterrows():

            try:
                facility = Facility.objects.get(
                    plant_code=row["facility_code"]
                )

                NormalizedActivity.objects.create(
    tenant=tenant,
    source=source,
    facility=facility,

    source_type=source.source_type,
    scope="SCOPE_1" if source.source_type == "SAP" else "SCOPE_2" if source.source_type == "UTILITY" else "SCOPE_3",

    activity_type=row["activity_type"],
    description=row["description"],

    quantity=float(row["quantity"]),
    original_unit=row["unit"],

    normalized_quantity=float(row["quantity"]),
    normalized_unit=row["unit"],

    period_start=row["period_start"],
    period_end=row["period_end"],

    status="PENDING",
    source_reference=row["reference"],
)

                created_rows += 1

            except Exception as e:
                failed_rows.append({
                    "row": index,
                    "error": str(e)
                })

        return Response({
            "message": "CSV processed",
            "created_rows": created_rows,
            "failed_rows": failed_rows
        })

    except Exception as e:
        return Response(
            {"error": str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["GET"])
def activity_list(request):

    activities = NormalizedActivity.objects.all().order_by("-created_at")

    serializer = NormalizedActivitySerializer(
        activities,
        many=True
    )

    return Response(serializer.data)

@api_view(["POST"])
def approve_activity(request, activity_id):

    try:

        activity = NormalizedActivity.objects.get(id=activity_id)

        activity.status = "APPROVED"

        activity.save()

        return Response({
            "message": "Activity approved"
        })

    except Exception as e:

        return Response({
            "error": str(e)
        })


@api_view(["POST"])
def lock_activity(request, activity_id):

    try:

        activity = NormalizedActivity.objects.get(id=activity_id)

        activity.status = "LOCKED"

        activity.save()

        return Response({
            "message": "Activity locked"
        })

    except Exception as e:

        return Response({
            "error": str(e)
        })