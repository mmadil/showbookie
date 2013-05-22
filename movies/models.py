from django.db import models
from django.template.defaultfilters import slugify

from django.contrib.comments.moderation import CommentModerator, moderator
from djangoratings.fields import RatingField

class Timing(models.Model):
    time = models.TimeField()

    def __unicode__(self):
        return str(self.time)


class Movie(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, blank=True, default='')
    photo = models.ImageField(upload_to="images/")
    description = models.TextField()
    published = models.BooleanField(default=True)
    seats = models.IntegerField(default=120)
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()
    timings = models.ManyToManyField(Timing)
    enable_comments = models.BooleanField(default=True)
    user_rating = RatingField(range=5, can_change_vote=True, allow_anonymous=False, use_cookies=True, allow_delete=True)
    anon_rating = RatingField(range=5, weight=10, can_change_vote=False, allow_anonymous=True, use_cookies=False)

    # To add ratings using Django Ratings.

    class Meta:
        ordering = ['-start_date','title']

    def __unicode__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slufigy(self.title)
        super(Movie, self).save(*args, **kwargs)

    @models.permalink
    def get_absolute_url(self):
        return("movies:detail", (), {"slug":self.slug})


class MovieCommentModerator(CommentModerator):
    email_notification = False
    auto_close_field = "start_date"
    close_after = 31

moderator.register(Movie, MovieCommentModerator)
