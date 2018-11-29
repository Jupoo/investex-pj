import datetime

from celery.schedules import crontab
from celery.task import periodic_task
from django.utils import timezone

from apps.tracking.models import PerDayTracking
from conf import settings


@periodic_task(run_every=crontab(**settings.UPDATE_PER_DAY_STATS))
def update_per_day_tracking_summary(start_at=None, end_at=None):
    start_at = start_at or (timezone.now() - datetime.timedelta(days=1)).date()
    end_at = end_at or (start_at + datetime.timedelta(days=1))

    report_data = ()

    if not report_data:
        return

    create_fields = ('user_id', 'date', 'campaign_id', 'action', 'hits', 'uniques', 'event_value', 'revenue',
                     'updated_at')

    report_data_flat = []

    for report_data_item in report_data:
        report_data_flat.append(
            [report_data_item[create_field] for create_field in create_fields]
        )

    PerDayTracking.objects._bulk_insert_on_duplicate(
        create_fields=create_fields,
        update_fields=('hits', 'uniques', 'event_value', 'revenue', 'updated_at'),
        values=report_data_flat
    )
