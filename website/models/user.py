# Models and Collections for users
from website.models.base import Collection, Model
from website.models.review import Review
from website.models.cart import Cart


reviews = Review()
carts = Cart()

''' Format for an insert would be:
    users.insert(username=...,password=...,is_owner=...)

    Other uses...
    users.cart_id = asdfasdf
    user.save()

    user.bio = asdfasdf
    user.save()
'''
class UserModel(Model):

    def __init__(self, db, fs, collection, obj):
        super(UserModel, self).__init__(db, fs, collection, obj)

    # Change password with authentication
    def change_password(self, oldpass, newpass, confirm):
        if oldpass == self.password:
            if newpass == confirm:
                self.password = newpass
                self.save()
                return True
        return False

    # Change password with authentication
    def change_username(self, password, newusr):
        if password == self.password and not self.collection.exists(newusr):
            self.username = newusr
            self.save()
            return True
        return False

    # Get blog reviews made by this user, and with other arguments
    def get_reviews(self, **kwargs):
        return reviews.find(user=self.username, **kwargs)

    # Get carts owned by the user if the user is registered as a cart owner
    def get_carts(self, **kwargs):
        if self.is_owner:
            return [carts.find_one(permit_number=license, **kwargs) for license
                in self.licenses if carts.find_one(permit_number=license,
                    **kwargs) is not None]

        return None


class User(Collection):

    def __init__(self):
        super(User, self).__init__(UserModel)

    def insert(self, **kwargs):
        return super(User, self).insert(**kwargs)

    # Checks if a specific user exists
    def exists(self, username):
        return self.find_one(username=username) is not None
