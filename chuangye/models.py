from django.db import models
class Cygsdetails(models.Model):
    name = models.CharField("公司名",max_length=200)
    lianjie = models.CharField("公司名链接",max_length=300)
    cltime = models.CharField("成立时间", max_length=50)
    place = models.CharField("地点", max_length=50)
    industry = models.CharField("行业", max_length=50)
    lunci = models.CharField("轮次", max_length=100)
    rzsum = models.CharField("融资总额", max_length=10)

    class Meta:
        verbose_name = "公司详情"
        verbose_name_plural = verbose_name
# Create your models here.
