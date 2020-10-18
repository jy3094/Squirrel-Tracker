from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):
    # Latitude #
    X = models.FloatField(
        max_length=10,
        help_text=_('Latitude'),
    )

    # Longitude #
    Y = models.FloatField(
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
        help_text=_('Shift'),
        choices=SHIFT_CHOICES,
        blank=True,
    )
    
    # Date #
    Date = models.DateField(
        help_text=_('Date'),
        blank=True,
    )
    
    # Age #
    Adult = 'Adult'
    Juvenile = 'Juvenile'

    AGE_CHOICES = [
        (Adult,_('Adult')),
        (Juvenile,_('Juvenile')),
    ]

    Age = models.CharField(
        max_length=15,
        help_text=_('Age'),
        choices=AGE_CHOICES,
        blank=True,
        null=True,
    )
    
    # Primary Fur Color #
    Gray = 'Gray'
    Cinnamon = 'Cinnamom'
    Black = 'Black'
    
    COLOR_CHOICES = [
        (Gray,_('Gray')),
        (Cinnamon,_('Cinnamom')),
        (Black,_('Black')),
    ]

    Primary_Fur_Color = models.CharField(
        max_length=100,
        help_text=_('Primary Fur Color'),
        choices=COLOR_CHOICES,
        blank=True,
        null=True,
    )
    
    # Location #
    Above_Ground = 'Above Ground'
    Ground_Plane = 'Ground_Plane'

    LOCATION_CHOICES = [
        (Above_Ground,_('Above Ground')),
        (Ground_Plane,_('Ground Plane')),
    ]

    Location = models.CharField(
        max_length=100,
        help_text=_('Location'),
        choices=LOCATION_CHOICES,
        blank=True,
        null=True,
    )
    
    # Specific Location #
    Specific_Location = models.CharField(
        max_length=100,
        help_text=_('Specific Location'),
        blank=True,
        null=True,
    )
    
    # Running #
    Running = models.BooleanField(
        help_text=_('Whether or not squirrel is running'),
        null=True,
    )
    
    # Chasing #
    Chasing = models.BooleanField(
        help_text=_('Whether or not squirrel is chasing'),
        null=True,
    )
    
    # Climbing #
    Climbing = models.BooleanField(
        help_text=_('Whether or not squirrel is climbing'),
        null=True,
    )
    
    # Eating #
    Eating = models.BooleanField(
        help_text=_('Whether or not squirrel is eating'),
        null=True,
    )
    
    # Foraging #
    Foraging = models.BooleanField(
        help_text=_('Whether or not squirrel is foraging'),
        null=True,
    )
    
    # Other Activities #
    Other_Activities = models.CharField(
        max_length=100,
        help_text=_('Other Activities'),
        blank=True,
        null=True,
    )
    
    # Kuks #
    Kuks = models.BooleanField(
        help_text=_('Kuks'),
        null=True,
    )
    
    # Quaas #
    Quaas = models.BooleanField(
        help_text=_('Quaas'),
        null=True,
    )
    
    # Moans #
    Moans = models.BooleanField(
        help_text=_('Moans'),
        null=True,
    )
    
    # Tail_Flags #
    Tail_Flags = models.BooleanField(
        help_text=_("Whether or not squirrel's tail flag"),
        null=True,
    )
    
    # Tail_Twitches #
    Tail_Twitches = models.BooleanField(
        help_text=_("Whether or not squirrel's tail twitch"),
        null=True,
    )
    
    # Approaches #
    Approaches = models.BooleanField(
        help_text=_('Whether or not squirrel approaches'),
        null=True,
    )
    
    # Indifferent #
    Indifferent = models.BooleanField(
        help_text=_('Whether or not squirrel is indifferent'),
        null=True,
    )
    
    # Runs From #
    Runs_From = models.BooleanField(
        help_text=_('Where the squirrel is running from'),
        null=True,
    )

    def __str__(self):
        return self.Squirrel_ID


