import datetime

from django.db import models


class User(models.Model):
    """
    This is a class representing User in a Database

    ...

    Attributes
    ----------
    user_id: str
        unique id of a user in the database
    date_subscribed: datetime
        date when user has subscribed to the newsletter
    name: str
        user's first name
    email: str
        user's e-mail address
    gender: str
        user's gender
    city: str
        user's city of living
    country: str
        user's country of living
    is_subscriber: bool
        determines if user has subscribed to the newsletter
    """

    GENDER = [("M", "Male"),
              ("F", "Female")]

    user_id: models.CharField(max_length=10, primary_key=True)
    name: models.CharField(max_length=20)
    email: models.CharField(max_length=40)
    gender: models.CharField(max_length=6, choices=GENDER)
    city: models.CharField(max_length=40)
    country: models.CharField(max_length=20)
    is_subscriber: models.BooleanField()
    date_subscribed: models.DateField()

    # def __int__(self,
    #             user_id: str,
    #             name: str,
    #             email: str,
    #             gender: str,
    #             city: str,
    #             country: str,
    #             is_subscriber: bool) -> None:
    #     self.user_id = user_id
    #     self.name = name
    #     self.email = email
    #     self.gender = gender
    #     self.city = city
    #     self.country = country
    #     self.is_subscriber = is_subscriber
    #     self.date_subscribed = datetime.date.today()

    def __str__(self) -> str:
        """
        The __str__ function is a special function in Python that defines the behavior of the str() function.
        :param self: Represent the instance of the class
        :return: A string representation of the object
        """
        return f"Name: {self.name}\nUser_id: {self.user_id}\n" \
               f"Gender: {self.gender}\nSubscribed since: {self.date_subscribed}\n" \
               f"email: {self.email}\nCity: {self.city}\n" \
               f"Country: {self.country}\n Subscribed: {self.is_subscriber}"

    def __repr__(self) -> str:
        """
        The __repr__ function is used to compute the &quot;official&quot; string representation of an object.
        The goal of __repr__ is to be unambiguous.

        :param self: Represent the instance of the class
        :return: A string representation of the object
        """
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
