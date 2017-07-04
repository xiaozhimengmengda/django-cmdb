from django.db import models

class Asset(models.Model):
     username = models.CharField(max_length=256)
     mac = models.CharField(max_length=128)
     os_system = models.CharField(max_length=128)
     create_time = models.DateTimeField()
     modify_time = models.DateTimeField()

     def __str__(self):
         return "{}, {}, {}, {}, {}".format(self.username, self.mac, self.os_system, self.create_time, self.modify_time)

