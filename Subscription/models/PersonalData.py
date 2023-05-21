from django.db import models
from .User import User


class PersonalData(models.Model):

    """
    This is a class representing data of single user

    ---
    user_id: charField
        unique id of a user (foreign key to User)
    name: charField
        user's first name
    email: charField
        user's e-mail address
    gender: charField
        user's gender
    city: charField
        user's city of living
    country: charField
        user's country of living
    """

    GENDER = [("M", "Male"),
              ("F", "Female")]

    user_id: models.ForeignKey(User, on_delete=models.CASCADE)
    name: models.CharField(max_length=20)
    email: models.CharField(max_length=40)
    gender: models.CharField(max_length=6, choices=GENDER)
    city: models.CharField(max_length=40)
    country: models.CharField(max_length=40)

    def __str__(self):
        return \
            f"user_id: {self.user_id}\nname: {self.name}" \
            f"email: {self.email}\ngender: {self.gender}" \
            f"city: {self.city}\nCountry: {self.country}"

    def __repr__(self):
        return \
            f"PersonalData({self.user_id}, {self.name}, {self.email}, {self.gender}, {self.city}, {self.country})"
