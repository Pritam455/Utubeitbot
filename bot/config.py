import os


class Config:

    BOT_TOKEN = os.environ.get("5898724572:AAGMQ89xl-ocLpv0AL8_TL0N8okOLpF0fVQ")

    SESSION_NAME = ":memory:"

    API_ID = int(os.environ.get("28887209"))

    API_HASH = os.environ.get("529adb50a7952a18c036537ec3c79536")

    CLIENT_ID = os.environ.get("12122836868-bvjv5up5afbgpvk0j8kmcjccsopla9ad.apps.googleusercontent.com")

    CLIENT_SECRET = os.environ.get("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")

    BOT_OWNER = int(os.environ.get("@Masoom_boy5"))

    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")

    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )

    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace("<", "").replace(">", "")
    )

    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get("VIDEO_CATEGORY") else 0
    )

    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")

    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")

    DEBUG = bool(os.environ.get("DEBUG"))

    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    CRED_FILE = "auth_token.txt"
