import os
from flask_login import (
    LoginManager,
)
from oauthlib.oauth2 import WebApplicationClient

SECRET_KEY = os.environ.get("SECRET_KEY") or os.urandom(24)

LOGIN_REDIRECT='index'
LOGOUT_REDIRECT='index'

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)
GOOGLE_DISCOVERY_URL = (
    "https://accounts.google.com/.well-known/openid-configuration"
)

CLIENT = WebApplicationClient(GOOGLE_CLIENT_ID)

LOGIN_MANAGER = LoginManager()

DIVISIONS = {0: 'Corporate', 1: 'Tucson', 2: 'Phoneix', 3: 'Hesperia', 4: 'Corona', 5: 'Vegas', 6: 'Pipeline', 7: 'Reno', 8: 'Carson', 9: 'Pacific', 10: 'Bullhead', 11: 'Inland', 12: 'Drip', 99: 'General'}
POSITIONS = {0: 'Admin', 1: 'Owner', 2: 'Executive', 3: 'Vice President', 4: 'Director', 5: 'Manager', 6: 'Coordinator', 7: 'Superintendent', 8: 'Shop', 9: 'Mechanic', 10: 'Foreman', 99: 'General'}