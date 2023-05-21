from django.db import models


class User(models.Model):
    """
    This is a class representing User in a Database

    ...

    Attributes
    ----------
    user_id: charField
        unique id of a user in the database
    date_subscribed: dateField
        date when user has subscribed to the newsletter
    is_subscriber: booleanField
        determines if user has subscribed to the newsletter
    """

    GENDER = [("M", "Male"),
              ("F", "Female")]

    user_id: models.CharField(max_length=10, primary_key=True)
    date_subscribed: models.DateField()
    is_subscriber: models.BooleanField()

    def __str__(self) -> str:
        return f"User_id: {self.user_id}\n" \
               f"Subscribed since: {self.date_subscribed}\n" \
               f"Subscription is active: {self.is_subscriber}"

    def __repr__(self) -> str:
        return f"User({self.city}, {self.country}, {self.email}, {self.gender}," \
               f"{self.is_subscriber}, {self.name}, {self.user_id}"

    @property
    def city(self) -> str:
        return self.city

    @property
    def country(self) -> str:
        return self.country

    @property
    def email(self) -> str:
        return self.email

    @property
    def gender(self) -> str:
        return self.gender

    @property
    def is_subscriber(self) -> bool:
        return self.is_subscriber

    @property
    def name(self) -> str:
        return self.name

    @property
    def user_id(self) -> str:
        return self.user_id

    @is_subscriber.setter
    def is_subscriber(self, is_subscriber):
        self._is_subscriber = is_subscriber

    @country.setter
    def country(self, value):
        self._country = value

    @city.setter
    def city(self, value):
        self._city = value

    @gender.setter
    def gender(self, value):
        self._gender = value

    @email.setter
    def email(self, value):
        self._email = value

    @name.setter
    def name(self, value):
        self._name = value

    @user_id.setter
    def user_id(self, value):
        self._user_id = value
