from django.db import models

# Create your models here.
class Article(models.Model):
    # id = models.AutoField(priamry_key = Ture)
    title = models.CharField(max_length=10)
    content = models.TextField()
    created_at = models.DatatimeField(auto_now_add=True)
    uapdated_at = models.DataTimeField(auto_now= True)

    def __str__(self): #매직 매서드 (특수 목정)
        return f'{self.id}번글 - {self.title} : {self.content}'
    # str(article), print(article)

