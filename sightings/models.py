from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):
    # Latitude #
    Latitude = models.FloatField(
        max_length=10,
        help_text=_('Latitude'),
    )

    # Longitude #
    Longitude = models.FloatField(
        max_length=10,
        help_text=_('Longitude'),
    )

    # Unique Squirrel ID #
    Squirrel_ID = models.CharField(
        max_length=100,
        help_text=_('Unique Squirrel ID'),
        primary_key=True,
        default = None,
    )
    
    # Shift #
    AM = 'AM'
    PM = 'PM'
    
    SHIFT_CHOICES = [
        (AM,_('AM')),
        (PM,_('PM')),
    ]

    Shift = models.CharField(
        max_length=100,
        help_text=('Shift'),
        choices=SHIFT_CHOICES,
        blank=True,
    )

    Date = models.DateField(
        help_text=_('Date'),
        blank=True,
    )

    Age = models.CharField(
        max_length=15,
        help_text=_('Age'),
        blank=True,
        null=True,
    )

    Fur_Color = models.CharField(
        max_length=100,
        help_text=_('Primary Fur Color'),
        blank=True,
        null=True,
    )

    Location = models.CharField(
        max_length=100,
        help_text=_('Location'),
        blank=True,
        null=True,
    )

    Specific_Location = models.CharField(
        max_length=100,
        help_text=_('Specific Location'),
        blank=True,
        null=True,
    )

    Running = models.BooleanField(
        help_text=_('Whether or not squirrel is running'),
        null=True,
    )

    Chasing = models.BooleanField(
        help_text=_('Whether or not squirrel is chasing'),
        null=True,
    )

    Climbing = models.BooleanField(
        help_text=_('Whether or not squirrel is climbing'),
        null=True,
    )

    Eating = models.BooleanField(
        help_text=_('Whether or not squirrel is eating'),
        null=True,
    )

    Foraging = models.BooleanField(
        help_text=_('Whether or not squirrel is foraging'),
        null=True,
    )

    Other_Activities = models.CharField(
        max_length=100,
        help_text=_('Other Activities'),
        blank=True,
        null=True,
    )
    
    Kuks = models.BooleanField(
        help_text=_('Kuks'),
        null=True,
    )

    Quaas = models.BooleanField(
        help_text=_('Quaas'),
        null=True,
    )

    Moans = models.BooleanField(
        help_text=_('Moans'),
        null=True,
    )

    Tail_Flags = models.BooleanField(
        help_text=_("Whether or not squirrel's tail flag"),
        null=True,
    )
    
    Tail_Twitches = models.BooleanField(
        help_text=_("Whether or not squirrel's tail twitch"),
        null=True,
    )

    Approaches = models.BooleanField(
        help_text=_('Whether or not squirrel approaches'),
        null=True,
    )

    Indifferent = models.BooleanField(
        help_text=_('Whether or not squirrel is indifferent'),
        null=True,
    )

    Runs_From = models.CharField(
        max_length=100,
        help_text=_('Where the squirrel is running from'),
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.Squirrel_ID


