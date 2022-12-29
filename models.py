"""
mx_random Models.
"""
from pyplanet.core.db.model import TimedModel
from peewee import *
class UserPoints(TimedModel):
    login = CharField(
        max_length=100,
        null=False,
        unique=True,
        help_text="User login"
    )

    name = CharField(
        max_length=255,
        null=False,
        help_text="Username"
    )

    points = FloatField(
        default=0.0, help_text="Points associated with login"
    )