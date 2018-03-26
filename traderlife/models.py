from django.db import models

# Create your models here.

class Game(models.Model):
    player = models.CharField(max_length=100)
    gameround = models.BigIntegerField()
    gameid = models.BigIntegerField()
    cash = models.DecimalField(max_digits=24, decimal_places=2)
    balance = models.DecimalField(max_digits=24, decimal_places=2)
    flag = models.CharField(max_length=1)
    create_time = models.DateTimeField(auto_now=True)
    extend1 = models.CharField(max_length=300,blank=True)
    extend2 = models.CharField(max_length=300,blank=True)


class Market_good(models.Model):
    name = models.CharField(max_length=100)
    base = models.DecimalField(max_digits=24, decimal_places=2) # 不是实际价格， 而是最低价格。
    quality = models.IntegerField()
    count = models.IntegerField()
    status = models.BooleanField()
    offset = models.DecimalField(max_digits=24, decimal_places=2) # 价格区间。最大24位， 保留两位小数。 实际价格应该在 (base, base+offset)之间
    flag = models.CharField(max_length=1)
    create_time = models.DateTimeField(auto_now=True)
    image_url = models.CharField(max_length=200)
    price = models.DecimalField(max_digits=24, decimal_places=2)
    extend1 = models.CharField(max_length=300,blank=True)
    extend2 = models.CharField(max_length=300,blank=True)
    def __str__(self):
        return self.name

class Market_good_history(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=24, decimal_places=2)  # 不是实际价格， 而是最低价格。
    count = models.IntegerField()
    flag = models.CharField(max_length=1)
    status = models.BooleanField()
    create_time = models.DateTimeField(auto_now=True)
    image_url = models.CharField(max_length=200)
    gameid = models.BigIntegerField()  # 游戏场次的id
    gameround = models.BigIntegerField()   # 该场次，游戏回合的id
    index = models.IntegerField(default=0)
    extend1 = models.CharField(max_length=300,blank=True)
    extend2 = models.CharField(max_length=300,blank=True)
    def __str__(self):
        return self.name


# 当前回合的结果
class My_good(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=24, decimal_places=2)
    quality = models.IntegerField()
    count = models.IntegerField()
    total = models.DecimalField(max_digits=24, decimal_places=2)
    status = models.BooleanField()
    username = models.CharField(max_length=100)
    flag = models.CharField(max_length=1)
    create_time = models.DateTimeField(auto_now=True)
    image_url = models.CharField(max_length=200)
    gameid = models.BigIntegerField()  # 游戏场次的id
    gameround = models.BigIntegerField()   # 该场次，游戏回合的id
    extend1 = models.CharField(max_length=300,blank=True)
    extend2 = models.CharField(max_length=300,blank=True)

# 数据记录
class My_good_history(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=24, decimal_places=2)
    quality = models.IntegerField()
    count = models.IntegerField()
    total = models.DecimalField(max_digits=24, decimal_places=2)
    status = models.BooleanField()
    username = models.CharField(max_length=100)
    flag = models.CharField(max_length=1)
    create_time = models.DateTimeField(auto_now=True)
    image_url = models.CharField(max_length=200)
    gameid = models.BigIntegerField() # 游戏场次的id
    gameround = models.BigIntegerField()   # 该场次，游戏回合的id
    extend1 = models.CharField(max_length=300,blank=True)
    extend2 = models.CharField(max_length=300,blank=True)

class Event(models.Model):
    name = models.CharField(max_length=100)
    comment = models.CharField(max_length=1000)
    type = models.CharField(max_length=1)
    status = models.BooleanField()
    flag = models.CharField(max_length=1)
    create_time = models.DateTimeField(auto_now=True)
    extend1 = models.CharField(max_length=300,blank=True)
    extend2 = models.CharField(max_length=300,blank=True)

class meta:
    unique_together = ()

