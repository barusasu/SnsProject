from django.db import models
from mdeditor.fields import MDTextField

# Create your models here.
TITLE_CHOICES = (
    ('danger', '重要'),
    ('warning', '連絡'),
    ('info', 'イベント'),
    ('success', 'その他'),
)

class ArticleModel(models.Model):
    name = models.CharField(max_length=70)
    tag = models.CharField(max_length=50, choices=TITLE_CHOICES)
    title = models.CharField(max_length=100)

    content = MDTextField()
    image = models.ImageField(upload_to='')
    created_at = models.DateField(verbose_name='作成日', auto_now=True)

    def __str__(self):
        return self.title