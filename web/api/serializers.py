from rest_framework import serializers
from web.datasets.models import (
    CityCouncilAgenda,
    CityCouncilAttendanceList,
    CityCouncilMinute,
    CityHallBid,
    CityHallBidEvent,
    File,
    Gazette,
    GazetteEvent,
)


class CityCouncilAgendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityCouncilAgenda
        fields = "__all__"


class CityCouncilAttendanceListSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityCouncilAttendanceList
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["url"]


class GazetteEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GazetteEvent
        fields = ["title", "secretariat", "summary", "published_on"]


class GazetteSerializer(serializers.ModelSerializer):
    events = GazetteEventSerializer(many=True)
    files = FileSerializer(many=True, required=False)

    class Meta:
        model = Gazette
        fields = [
            "crawled_from",
            "date",
            "power",
            "year_and_edition",
            "events",
            "files",
        ]


class CityCouncilMinuteSerializer(serializers.ModelSerializer):
    files = FileSerializer(many=True)

    class Meta:
        model = CityCouncilMinute
        fields = "__all__"


class CityHallBidEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = CityHallBidEvent
        fields = "__all__"


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = File
        fields = ["url"]


class CityHallBidSerializer(serializers.ModelSerializer):

    events = CityHallBidEventSerializer(many=True, read_only=True)
    files = FileSerializer(many=True, read_only=True)

    class Meta:
        model = CityHallBid
        fields = "__all__"
