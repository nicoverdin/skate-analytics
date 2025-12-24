from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField


class Level(models.IntegerChoices):
    NO_LEVEL = 0, 'No level'
    BASE = 1, 'Base'
    ONE = 2, '1'
    TWO = 3, '2'
    THREE = 4, '3'
    FOUR = 5, '4'


class ElementCode(models.TextChoices):
    TRAVELING = 'Tr', 'Traveling'
    ARTISTIC = 'ASq', 'Art Seq'
    DANCE = 'DSSq', 'Dance Step Seq'
    FOOTWORK = 'FoSq', 'Foot Seq'
    CLUSTER = 'ClSq', 'Cluster Sequence'
    ONE_SET_CLUSTER = '1SClSq', 'One Set Cluster Seq'
    CHOREO_STEP = 'ChStS', 'Choreo Step Seq'
    ITALIAN_FOXTROT_2 = 'IF2', 'Italian Foxtrot Section 2'
    SWEET_TANGO = 'SWT1', 'Sweet Tango'
    TERENZI_WALTZ_1 = 'TW1', 'Terenzi Waltz Section 1'


class Element(models.Model):
    code = models.CharField(max_length=10, unique=True)

    name = models.CharField(
        max_length=50, choices=ElementCode.choices, null=True
    )

    level = models.IntegerField(choices=Level.choices, default=Level.NO_LEVEL)
    base_score = models.DecimalField(max_digits=4, decimal_places=1, default=0)

    extra_points = models.DecimalField(
        max_digits=4, decimal_places=1, default=0
    )

    class Meta:
        ordering = ['code']
        verbose_name = "Element"
        verbose_name_plural = "Elements"

    def __str__(self):
        return f"{self.get_name_display()} (Lvl {self.level})"


class Skater(models.Model):
    name = models.CharField(max_length=100)

    elements = models.ManyToManyField(
        'Element', through='Result', blank=True, related_name='skaters'
    )

    free_elements = ArrayField(
        models.CharField(max_length=20),
        default=list,
        blank=True,
        help_text='List of element codes/names for Free program'
    )
    style_elements = ArrayField(
        models.CharField(max_length=20),
        default=list,
        blank=True,
        help_text='List of element codes/names for Style program'
    )

    class Meta:
        ordering = ['name', 'id']

    def __str__(self):
        return self.name


class Result(models.Model):
    skater = models.ForeignKey(
        Skater, on_delete=models.CASCADE, related_name='results'
    )

    element = models.ForeignKey(
        Element, on_delete=models.CASCADE, related_name='results'
    )

    date = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)
    is_program = models.BooleanField(default=False)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return f"{self.skater.name} - {self.element.code} - {self.date.date()}"
