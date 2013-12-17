from django.db import models


class CalendarEvent(models.Model):
    title = models.CharField('Title', blank=True, max_length=200)
    start = models.DateTimeField('Start')
    end = models.DateTimeField('End')
    all_day = models.BooleanField('All day', default=False)

    def __unicode__(self):
        return self.title
