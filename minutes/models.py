from django.db import models

# Create your models here.
class User(models.Model):
    userName = models.CharField(max_length=40) # name # HTML: 'user_name'
    password = models.CharField(max_length=40) # password # HTML: 'user_pwd'
    email = models.EmailField() # HTML: 'user_email'
    phoneNumber = models.CharField(max_length=40) # phone #HTML: 'user_phone'
    # !!! (backlog) orgAffilitaions = models.
    def __unicode__(self):
        return self.userName

class MtgMinutes(models.Model):
    ## constant declaring options for different types of meetings
    SPECIAL = 'SP'
    GENERAL = 'GN'
    AGM = 'AG'
    MEETING_TYPES = ((SPECIAL, 'Special'),
                    (GENERAL, 'General'),
                    (AGM, 'Annual general Meeting'))
    date = models.DateField() # Date of MtgMinutes (ISO-8001) # HTML: 'mtgminutes_date'
    startTime = models.TimeField() # Begin Time (ISO-8001) # HTML: 'mtgminutes_starttime'
    endTime = models.DateTimeField() # End Time (ISO-8001) # HTML: 'mtgminutes_endtime'
    # usersAttended = models.ManyToManyField(User)
    # usersAbsent = models.ManyToManyField(User)
    noteTaker = models.ForeignKey(User) # HTML: 'mtgminutes_notetaker'
    meetingType = models.CharField(max_length=2,
                                    choices = MEETING_TYPES,
                                    default = GENERAL) #HTML: 'mtgminutes_meetingtype' (see above for constants)
    # !!! (backlog) Seen by

    def __unicode__(self):
        return self.date


class Organization(models.Model):
    users = models.ManyToManyField(User) # Foreignkey(user) # HTML: 'organization_user'
    name = models.CharField(max_length=100, verbose_name="The Full Name of the Organization, Committee, Team, or other Unit") # HTML: 'organization_name'
    minutes = models.ManyToManyField(MtgMinutes) # HTML: 'organization_minutes'
    def __unicode__(self):
        return self.name


class MtgMinutesItem(models.Model):
    MtgMinutes = models.ForeignKey(MtgMinutes)
    number = models.PositiveSmallIntegerField(verbose_name="Ordinal Ranking of Item on the MtgMinutes it belongs to") # HTML: 'mtgminutesitem_number'
    title = models.CharField(max_length=100) # HTML: 'mtgminutesitem_title'
    detail = models.TextField() # HTML: 'mtgminutesitem_detail'
    # !!! (backlog) TinyMCE / Markdown (Python-Markdown)?

    def __unicode__(self):
        return self.title

# class Topic(models.Model)
    # !!! (backlog)


# class Agenda(models.Model)
    #!!! (backlog)
