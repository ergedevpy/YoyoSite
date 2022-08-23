from django.db import models


class Category(models.Model):
    title = models.CharField(max_length=255)
    slag = models.SlugField(max_length=255, verbose_name="URL", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Tag(models.Model):
    title = models.CharField(max_length=50)
    slag = models.SlugField(max_length=50, verbose_name="URL", unique=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["title"]


class Post(models.Model):
    title = models.CharField(max_length=255)
    slag = models.SlugField(max_length=255, verbose_name="URL", unique=True)
    author = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Published")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", blank=True)
    views = models.IntegerField(default=0, verbose_name="Count of views")
    category = models.ForeignKey(Category, on_delete=models.PROTECT, related_name="posts")
    tags = models.ManyToManyField(Tag, related_name="tags", blank=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_at"]
