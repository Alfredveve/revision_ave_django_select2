from django.db import models

class BlogArticles(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=300)
    image = models.ImageField(upload_to = 'images/', blank=True)
    datapub = models.DateTimeField()
    slug = models.SlugField(max_length=10)

    class Meta:
        verbose_name = 'BlogArticle'
        verbose_name_plural = 'BlogArticles'

        def __str__(self):
            return self.title


