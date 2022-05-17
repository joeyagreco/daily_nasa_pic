import datetime
from dataclasses import dataclass
from typing import Optional


@dataclass(frozen=True, kw_only=True)
class ApodResponse:
    copyright: Optional[str]
    date: datetime
    explanation: str
    hdUrl: str
    mediaType: str  # TODO: make enum
    serviceVersion: str
    title: str
    url: str
