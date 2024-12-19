import re

from django.conf import settings


def identify_service(link):

    link_patterns = settings.LINK_PATTERNS

    for service, pattern in link_patterns.items():
        if re.match(pattern, link, re.IGNORECASE):
            return service

    return "unknown"