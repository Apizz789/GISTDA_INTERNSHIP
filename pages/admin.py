from django.contrib.gis import admin

from .models import polygon
# Register your models here.

@admin.register(polygon)
class MarkerAdmin(admin.OSMGeoAdmin):
    """Marker admin."""

    list_display = ["notam"]