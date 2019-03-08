from django.contrib.auth.mixins import UserPassesTestMixin


class UserIsOwnerMixin(UserPassesTestMixin):
    def test_func(self):
        return self.request.user == self.get_object().owner
