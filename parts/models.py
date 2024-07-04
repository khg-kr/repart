from django.db import models


class Part(models.Model):
    category_code = models.CharField(max_length=10)
    part_code = models.CharField(max_length=20)
    part_name = models.CharField(max_length=100)
    part_price = models.CharField(max_length=20)
#   part_price = models.DecimalField(max_digits=10, decimal_places=2)
#   retail_price = models.IntegerField()  # 권장소비자가격 정수형으로 저장

 #   def save(self, *args, **kwargs):
        # 실제 가격이 있을 경우 권장소비자가격은 실제 가격을 정수로 저장
  #      if self.part_price:
  #          self.retail_price = int(self.part_price)
  #      super().save(*args, **kwargs)

    def __str__(self):
        return self.part_name

