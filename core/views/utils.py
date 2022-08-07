from core.models import User, _user, _users, Profile, _profile, _profiles


class CurrentUser:

    def __init__(self, id, is_authenticated=True):
        self.id = id
        self._is_authenticated = is_authenticated

    @property
    def _user(self):
        return User.query.filter(User.id==self.id).one()

    @property
    def user(self):
        return _user.dump(self._user)

    @property
    def _profile(self):
        return Profile.query.filter(Profile.user_id==self._user.id).one()

    @property
    def profile(self):
        return _profile.dump(self._profile)
