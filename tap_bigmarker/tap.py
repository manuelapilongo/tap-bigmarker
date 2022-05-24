"""BigMarker tap class."""

from typing import List

from singer_sdk import Tap, Stream
from singer_sdk import typing as th  # JSON schema typing helpers

from tap_bigmarker.streams import (
    BigMarkerStream,
    ChannelsStream,
    ChannelsSubscribersStream,
    ChannelsAdminsStream,
    ConferencesStream,
    ConferencesAttendeesStream,
    ConferencesHandoutsStream,
    ConferencesSurveysStream,
    ConferencesPresentersStream,
    ConferencesRegistrantsStream,
    ConferencesAttendeesLiveStream,
    ConferencesAttendeesOnDemandStream,
    ConferencesRegistrationsNoShowsStream
)

STREAM_TYPES = [
    ChannelsStream,
    ChannelsSubscribersStream,
    ChannelsAdminsStream,
    ConferencesStream,
    ConferencesHandoutsStream,
    ConferencesSurveysStream,
    ConferencesPresentersStream,
    ConferencesAttendeesStream,
    ConferencesRegistrantsStream,
    ConferencesAttendeesLiveStream,
    ConferencesAttendeesOnDemandStream,
    ConferencesRegistrationsNoShowsStream
]

class TapBigMarker(Tap):
    """BigMarker tap class."""
    name = "tap-bigmarker"
    config_jsonschema = th.PropertiesList(
        th.Property(
            "api_key",
            th.StringType,
            required=True,
            description="The token to authenticate against the API service"
        ),
        th.Property(
            "api_url",
            th.StringType,
            required=True,
            description="The url for the API service"
        ),
        th.Property(
            "page_size",
            th.StringType,
            required=False,
            description="The page size for each request"
        ),
    ).to_dict()

    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]
