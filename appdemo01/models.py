from django.db import models


class Cars(models.Model):
    car_name = models.CharField(null=False, max_length=50, verbose_name="名称")
    car_type = models.CharField(null=False, max_length=50, verbose_name="类型")
    car_color = models.CharField(max_length=40, verbose_name="颜色")
    car_count = models.IntegerField(default=0, verbose_name="数量")

    class Meta:
        verbose_name = '汽车信息'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.car_name
