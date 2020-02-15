from django.db import models
from model_utils import Choices



class Posts(models.Model):
    id = models.AutoField(primary_key=True)
    slug = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    postdesc = models.CharField(max_length=500, default="Nothing")
    mainimage = models.ImageField(upload_to="images")
    relatedlink = models.CharField(max_length=100)
    relatedtext = models.CharField(max_length=100)
    desc = models.TextField(max_length=5000)
    tags = models.TextField(max_length=500,default="Nothing")
    postimage = models.ImageField(upload_to="images", default="no imahe")
    postimage1 = models.ImageField(upload_to="images", default="no image")
    postviews = models.IntegerField(default=0)
    pub_date = models.DateField()

    STATUS =(
        ("PakistaniNews","Pakistani News"),
        ("Opinions","Opinions"),
        ("InternationalNews", "International News"),
    )
    # [..]
    Category = models.CharField(
        max_length=32,
        choices=STATUS,
        default="PakistaniNews",
    )

    def __str__(self):
        return self.title

class Cardetail(models.Model):
    id = models.AutoField(primary_key=True)
    company = models.CharField(max_length=100)
    slug = models.CharField(max_length=100)
    carname = models.CharField(max_length=100)
    carvariant = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    carprice = models.CharField(max_length=100)
    mainimage = models.ImageField(upload_to="images")
    postimage = models.ImageField(upload_to="images")
    postimage1 = models.ImageField(upload_to="images")
    engine = models.IntegerField(default=0)
    mileage = models.IntegerField(default=0)
    transmission = (
        ("Manual", "Manual"),
        ("Automatic", "Automatic"),
    )
    # [..]
    Transmission = models.CharField(
        max_length=32,
        choices=transmission,
        default="Manual",
    )
    power = models.IntegerField(default=0)
    seats = models.IntegerField(default=0)
    enginetype = (
        ("Petrol","Petrol"),
        ("Diesel", "Diesel"),
    )
    # [..]
    EngineType = models.CharField(
        max_length=32,
        choices=enginetype,
        default="Petrol",
    )
    carintro = models.TextField(max_length=500, default="Nothing")
    carexterior = models.TextField(max_length=500)
    carinterior = models.TextField(max_length=500)
    carengine = models.TextField(max_length=500)
    carmileage = models.TextField(max_length=500)
    carcompetitor = models.TextField(max_length=500)
    cartags = models.TextField(max_length=500,default="Nothing")
    postviews = models.IntegerField(default=0)
    airbags =(
        ("Yes","Yes"),
        ("No","No"),
    )
    # [..]
    Airbags = models.CharField(
        max_length=32,
        choices=airbags,
        default="No",
    )
    abs = (
        ("&#9989;", "Yes"),
        ("&#10060;", "No"),
    )
    # [..]
    ABS = models.CharField(
        max_length=32,
        choices=abs,
        default="No",
    )
    alloywheels = (
        ("&#9989;", "Yes"),
        ("&#10060;", "No"),
    )
    # [..]
    AlloyWheels = models.CharField(
        max_length=32,
        choices=alloywheels,
        default="No",
    )
    ac = (
        ("&#9989;", "Yes"),
        ("&#10060;", "No"),
    )
    # [..]
    AC = models.CharField(
        max_length=32,
        choices=ac,
        default="No",
    )
    lcd = (
        ("&#9989;", "Yes"),
        ("&#10060;", "No"),
    )
    # [..]
    LcdScreen = models.CharField(
        max_length=32,
        choices=lcd,
        default="No",
    )
    powerwindows = (
        ("&#9989;", "Yes"),
        ("&#10060;", "No"),
    )
    # [..]
    PowerWindows = models.CharField(
        max_length=32,
        choices=powerwindows,
        default="No",
    )
    powersteering = (
        ("&#9989;", "Yes"),
        ("&#10060;", "No"),
    )
    # [..]
    PowerSteering = models.CharField(
        max_length=32,
        choices=powersteering,
        default="No",
    )
    foglights = (
        ("&#9989;", "Yes"),
        ("&#10060;", "No"),
    )
    # [..]
    FogLights = models.CharField(
        max_length=32,
        choices=foglights,
        default="No",
    )
    Keylessentry = (
        ("&#9989;", "Yes"),
        ("&#10060;", "No"),
    )
    # [..]
    KeylessEntry = models.CharField(
        max_length=32,
        choices=Keylessentry,
        default="No",
    )
    dvd = (
        ("&#9989;", "Yes"),
        ("&#10060;", "No"),
    )
    # [..]
    DvdPlayer = models.CharField(
        max_length=32,
        choices=dvd,
        default="No",
    )

    def __str__(self):
        return self.carname