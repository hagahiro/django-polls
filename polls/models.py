from django.db import models
import datetime
from django.utils import timezone

# Create your models here.

# each field is represented as a instance of the Field class.
# Classes such as CharField and DataTimeField teach django what data types each field should store.
# the class variables here represent the fields in the model database.
class Question(models.Model):
    question_text=models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published")
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    # relationships are defined using foreignkeys.
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes=models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text
