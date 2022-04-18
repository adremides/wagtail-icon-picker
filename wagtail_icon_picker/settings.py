from functools import lru_cache

from django.conf import settings

WAGTAIL_ICON_PICKER_DEFAULTS = {
    "BOOTSTRAP_ICONS_URL": "https://cdn.jsdelivr.net/npm/bootstrap-icons@latest/font/bootstrap-icons.css",
    "FONTAWESOME_ICONS_URL": "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css",
    "BOXICONS_ICONS_URL": "https://unpkg.com/boxicons@2.0.9/css/boxicons.min.css",
}


@lru_cache()
def get_config():
    """Read a setting."""
    # Start with a copy of default settings
    CONFIG = WAGTAIL_ICON_PICKER_DEFAULTS.copy()

    # Override with user settings from settings.py
    CONFIG.update(getattr(settings, "WAGTAIL_ICON_PICKER", {}))

    return CONFIG
