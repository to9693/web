from django.db import models
from imagekit.models import ProcessedImageField
from imagekit.processors import Thumbnail, ResizeToFill, ResizeToFit
from django.conf import settings
# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length = 50)
    description = models.TextField()
    poster = ProcessedImageField(
        blank = True,
        upload_to ='movies/image', # 업로드 위치
        processors = [Thumbnail(300,300)], # 처리할 작업 목록
        format = 'jpeg', # 저장 포맷 - jph.png 등 사용 가능
        options = {
            'quality' : 90, # 옵션
        },
    )
    created_at = models.DateTimeField(auto_now_add=True) # 데이터가 생성된 시간을 자동으로 저장
    updated_at = models.DateTimeField(auto_now=True) # auto_now_add = 생성될때 한번만 , auto_now = 수정될때마다 현재 시간 기록
     # 1:N (User:Article)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete = models.CASCADE)

class Rating(models.Model):
    score = models.FloatField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True) # 데이터가 생성된 시간을 자동으로 저장
    updated_at = models.DateTimeField(auto_now=True) # auto_now_add = 생성될때 한번만 , auto_now = 수정될때마다 현재 시간 기록
    user = models.ForeignKey(Movie, on_delete=models.CASCADE)