"""Stream type classes for tap-mindstamp."""

from pathlib import Path
from typing import Optional

from tap_bigmarker.client import BigMarkerStream

SCHEMAS_DIR = Path(__file__).parent / Path("./schemas")


class ChannelsStream(BigMarkerStream):
    name = "channels"
    path = "/channels"
    records_jsonpath = "$.channels[*]"
    primary_keys = ["channel_id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    schema_filepath = SCHEMAS_DIR / "channels.json"
    has_pagination = False

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {"channel_id": record["channel_id"]}


class ChannelsSubscribersStream(BigMarkerStream):
    name = "channels_subscribers"
    path = "/channels/{channel_id}/subscribers"
    records_jsonpath = "$.subscribers[*]"
    primary_keys = ["bmid"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    schema_filepath = SCHEMAS_DIR / "channels_subscribers.json"
    parent_stream_type = ChannelsStream
    ignore_parent_replication_keys = True
    has_pagination = False


class ChannelsAdminsStream(BigMarkerStream):
    name = "channels_admins"
    path = "/channel_admins/{channel_id}"
    records_jsonpath = "$[*]"
    primary_keys = ["admin_id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    schema_filepath = SCHEMAS_DIR / "channels_admins.json"
    parent_stream_type = ChannelsStream
    ignore_parent_replication_keys = True
    has_pagination = False


class ConferencesStream(BigMarkerStream):
    name = "conferences"
    path = "/conferences"
    records_jsonpath = "$.conferences[*]"
    primary_keys = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    schema_filepath = SCHEMAS_DIR / "conferences.json"

    def get_child_context(self, record: dict, context: Optional[dict]) -> dict:
        """Return a context dictionary for child streams."""
        return {"conference_id": record["id"]}

class ConferencesHandoutsStream(BigMarkerStream):
    name = "conferences_handouts"
    path = "/conferences/{conference_id}/handouts"
    records_jsonpath = "$[*]"
    primary_keys = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    schema_filepath = SCHEMAS_DIR / "conferences_handouts.json"
    parent_stream_type = ConferencesStream
    ignore_parent_replication_keys = True
    has_pagination = False

class ConferencesSurveysStream(BigMarkerStream):
    name = "conferences_surveys"
    path = "/conferences/survey/{conference_id}"
    records_jsonpath = "$.survey[*]"
    primary_keys = ["question_title", "answer_type"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    schema_filepath = SCHEMAS_DIR / "conferences_surveys.json"
    parent_stream_type = ConferencesStream
    ignore_parent_replication_keys = True
    has_pagination = False

class ConferencesPresentersStream(BigMarkerStream):
    name = "conferences_presenters"
    path = "/conferences/{conference_id}/presenters"
    records_jsonpath = "$.presenters[*]"
    primary_keys = ["presenter_id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    schema_filepath = SCHEMAS_DIR / "conferences_presenters.json"
    parent_stream_type = ConferencesStream
    ignore_parent_replication_keys = True
    has_pagination = False

class ConferencesAttendeesStream(BigMarkerStream):
    name = "conferences_attendees"
    path = "/conferences/{conference_id}/attendees"
    page_key = "current_page"
    records_jsonpath = "$.attendees[*]"
    primary_keys = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    schema_filepath = SCHEMAS_DIR / "conferences_attendees.json"
    parent_stream_type = ConferencesStream
    ignore_parent_replication_keys = True

class ConferencesRegistrantsStream(BigMarkerStream):
    name = "conferences_registrants"
    path = "/conferences/registrations_with_fields/{conference_id}"
    records_jsonpath = "$.registrations[*]"
    primary_keys = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    schema_filepath = SCHEMAS_DIR / "conferences_registrants.json"
    parent_stream_type = ConferencesStream
    ignore_parent_replication_keys = True

class ConferencesAttendeesLiveStream(BigMarkerStream):
    name = "conferences_attendees_live"
    path = "/reporting/conferences/live_attendees/{conference_id}"
    page_key = "current_page"
    records_jsonpath = "$.attendees[*]"
    primary_keys = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    schema_filepath = SCHEMAS_DIR / "conferences_attendees_live.json"
    parent_stream_type = ConferencesStream
    ignore_parent_replication_keys = True

class ConferencesRegistrationsNoShowsStream(BigMarkerStream):
    name = "conferences_registrations_no_shows"
    path = "/reporting/conferences/no_shows/{conference_id}"
    page_key = "current_page"
    records_jsonpath = "$.registrations[*]"
    primary_keys = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    schema_filepath = SCHEMAS_DIR / "conferences_registrations_no_shows.json"
    parent_stream_type = ConferencesStream
    ignore_parent_replication_keys = True

class ConferencesAttendeesOnDemandStream(BigMarkerStream):
    name = "conferences_attendees_on_demand"
    path = "/reporting/conferences/on_demand_attendees/{conference_id}"
    page_key = "current_page"
    records_jsonpath = "$.attendees[*]"
    primary_keys = ["id"]
    replication_method = "FULL_TABLE"
    replication_keys = []
    schema_filepath = SCHEMAS_DIR / "conferences_attendees_on_demand.json"
    parent_stream_type = ConferencesStream
    ignore_parent_replication_keys = True