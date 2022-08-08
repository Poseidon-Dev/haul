import requests, json

from flask import redirect, request, url_for
from flask_login import login_user, logout_user

from core.models import User, Profile
from core.settings.database import db
import core.settings.config as config

# OAuth 2 client setup
client = config.CLIENT
login_manager = config.LOGIN_MANAGER

def get_google_provider_cfg():
    return requests.get(config.GOOGLE_DISCOVERY_URL).json()

# Flask-Login helper to retrieve a user from our db
@login_manager.user_loader
def load_user(user_id):
    q = db.query(User)
    return q.filter(User.id==user_id).one()

def login():
    # Find out what URL to hit for Google login
    google_provider_cfg = get_google_provider_cfg()
    authorization_endpoint = google_provider_cfg["authorization_endpoint"]

    # Use library to construct the request for Google login and provide
    # scopes that let you retrieve user's profile from Google
    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"],
    )
    return redirect(request_uri)

def callback():
    # Get authorization code Google sent back to you
    code = request.args.get("code")
    # Find out what URL to hit to get tokens that allow you to ask for
    # things on behalf of a user
    google_provider_cfg = get_google_provider_cfg()
    token_endpoint = google_provider_cfg["token_endpoint"]

    # Prepare and send a request to get tokens
    token_url, headers, body = client.prepare_token_request(
        token_endpoint,
        authorization_response=request.url,
        redirect_url=request.base_url,
        code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(config.GOOGLE_CLIENT_ID, config.GOOGLE_CLIENT_SECRET),
    )

    # Parse the tokens
    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider_cfg["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = requests.get(uri, headers=headers, data=body)

    if userinfo_response.json().get("email_verified"):
        _id = userinfo_response.json()["sub"]
        email = userinfo_response.json()["email"]
        picture = userinfo_response.json()["picture"]
        first_name = userinfo_response.json()["given_name"]
        last_name = userinfo_response.json()["family_name"]
        domain = userinfo_response.json()["hd"]
        is_active = userinfo_response.json()["email_verified"]
    else:
        return "User email not available or not verified by Google.", 400

    try:
        user_query = db.query(User)
        u = user_query.filter(User.id==_id).one()
    except:
        u = User(_id, first_name, last_name, email, picture, domain, is_active)
        db.add(u)
        p = Profile(user_id=u.id)
        db.add(p)
        db.commit()

    login_user(u)
    return redirect(url_for(config.LOGIN_REDIRECT))

def logout():
    logout_user()
    return redirect(url_for(config.LOGOUT_REDIRECT))