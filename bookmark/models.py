from django.db import models
from django.urls import reverse

# Create your models here.
# 모델 : 데이터베이스를 SQl 없이 다루려고 모델을 사용
# 모델 = 테이블
# 모들의 필드 = 테이블의 컬럼(열)
# 인스턴스 = 테이블의 레코드(행)
# 필드의 값(인스턴스의 필드값) = 레코드의 컬럼 데이터 값

class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')

    def __str__(self):
        return '이름 : '+ self.site_name+', 주소 : '+ self.url

    def get_absolute_url(self):
        return reverse('detail', args=[self.id])
