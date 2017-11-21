from django.db import models

class Ment(models.Model):

    sn = models.CharField(verbose_name='sn码', max_length=64, default="")
    ip = models.CharField(verbose_name='ip地址', max_length=64, default="")
    hostname = models.CharField(verbose_name='主机名字', max_length=64, default="")
    mac = models.CharField(verbose_name='mac地址',  max_length=64, default="")
    addr = models.CharField(verbose_name='网卡地址', max_length=64, default="")
    admin = models.CharField(verbose_name='管理员', max_length=64, default="")
    user =  models.CharField(verbose_name='用户名', max_length=64, default="")
    time = models.DateTimeField(verbose_name="创建时间", auto_now_add=True)
    # auto_now_add 第一次创建修改
    # auto_now 每次修改model，都会自动更新
    mem = models.IntegerField(verbose_name="内存",default=0)
    update_time = models.DateTimeField(verbose_name="修改时间", auto_now=True)

    def __str__(self):
        return 'sn:{},ip:{},hostname:{},mac:{},addr:{},admin:{},user:{},time:{},mem:{}'.format(self.sn,
                                                                                               self.ip, self.hostname,
                                                                                               self.mac, self.addr,
                                                                                               self.admin, self.user,
                                                                                               self.user, self.time,
                                                                                               self.mem)

    class Meta:
        verbose_name = "资源表"
        verbose_name_plural = "资源表"

    # 把一个类转化成字典
    def as_dict(self):
        return self.__dict__


