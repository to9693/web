from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=20)
    title_en = models.TextField()
    audience = models.TextField()
    open_date = models.TextField()
    genre = models.TextField()
    watch_grade = models.TextField()
    score = models.TextField()
    poster_url = models.TextField()
    description = models.TextField()

    def __str__(self): # 매직 메서드 (특수 목적)
        return f'{self.id} - {self.title}: {self.title_en} {self.audience}{self.open_date}{self.genre}{self.watch_grade}{self.score}{self.poster_url}{self.description}'
    # str(), print() 호출 시 출력되는 함수