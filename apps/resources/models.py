from django.db import models
from apps.core.models import CreatedModifiedDateTimeBase
from apps.resources import validators


class Tag(CreatedModifiedDateTimeBase):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Category(CreatedModifiedDateTimeBase):
    cat = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.cat


class Resources(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey(
        "user.User", null=True, on_delete=models.SET_NULL)
    cat_id = models.ForeignKey(
        "resources.Category", default=1, on_delete=models.SET_DEFAULT)
    title = models.CharField(max_length=200, null=True, blank=True)
    description = models.TextField()
    link = models.URLField(max_length=500)
    tags = models.ManyToManyField("resources.Tag", through="ResourcesTag")
    # rate = ArrayField(base_field=models.IntegerField())

    class Meta:
        verbose_name_plural = "Recources"

    def __str__(self):
        return f"{self.user_id.username} - {self.title}"

    @property
    def user_title(self):
        return self.user_id.title


class ResourcesTag(CreatedModifiedDateTimeBase):
    modified_at = None
    resources_id = models.ForeignKey(
        "resources.Resources", on_delete=models.CASCADE)
    tag_id = models.ForeignKey("resources.Tag", on_delete=models.CASCADE)


class Review(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey(
        "user.User", null=True, on_delete=models.SET_NULL)
    resources_id = models.ForeignKey(
        "resources.Resources", on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return f"{self.user_id.username} - {self.resources_id.title}"


class Rating(CreatedModifiedDateTimeBase):
    user_id = models.ForeignKey(
        "user.User", null=True, on_delete=models.SET_NULL)
    resources_id = models.ForeignKey(
        "resources.Resources", on_delete=models.CASCADE)
    rate = models.IntegerField(validators=[validators.check_rating_range])

    def __str__(self):
        return self.rate
