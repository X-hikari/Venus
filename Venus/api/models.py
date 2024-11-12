from django.db import models

class Article(models.Model):
    # id字段是自动生成的主键，不需要手动定义
    title = models.CharField(max_length=255)  # 与 VARCHAR(255) 类似
    content = models.TextField()  # 与 TEXT 类似
    created_at = models.DateTimeField(auto_now_add=True)  # 创建时间，默认当前时间
    updated_at = models.DateTimeField(auto_now=True)  # 更新时间，记录更新时的时间

    def __str__(self):
        return self.title  # 返回文章标题，便于管理后台显示
