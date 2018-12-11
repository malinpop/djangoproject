from django.db import models


class Defect(models.Model):
    bug_state_choice = (('New', '新建'), ('Open', '打开'),
                        ('Fixed', '已修复'), ('Closed', '已关闭'),)
    bug_code = models.CharField(max_length=10, unique=True, verbose_name="缺陷编号")
    bug_name = models.CharField(max_length=50, verbose_name="缺陷标题")
    bug_desc = models.CharField(null=True, max_length=500, verbose_name="缺陷描述")
    bug_priority = models.IntegerField(null=True, verbose_name="缺陷优先级", default=1)
    bug_state = models.CharField(max_length=10, default="New",
                                 choices=bug_state_choice, verbose_name="缺陷状态")

    class Meta:
        verbose_name = '缺陷报告'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.bug_name
