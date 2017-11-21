# django第一天
* 使用django新建一个项目  django-admin startproject xxx
* 新建一个app文件 python manager.py startapp xxx
## 修改全局配置文件--settings
* 修改 ALLOWED_HOSTS 
* 修改 INSTALLED_APPS
* 修改 TEMPLATES
* 修改 DATABASES
* 最后面新增 STATICFILES_DIRS = [
            os.path.join(BASE_DIR, 'static')
        ]
## urls.py
```from django.conf.urls import url, include
   from django.contrib import admin
   
   urlpatterns = [
       url(r'^admin/', admin.site.urls),
       url(r'^ams/', include("ams.urls", namespace="ams")),
   ]

```

## 到app里面添加url.py
```from django.conf.urls import url
   from .views import index, commands
   
   urlpatterns = [
       url(r'^$', view=index, name="index"),
       url(r'^commands/$', view=commands, name="commands"),
   ]
```
## 到app里面编写view.py
``from django.shortcuts import render
  from django.http import HttpResponse
  # Create your views here.
  import os
  
  def index(request):
      return render(request,"index.html")
  
  def commands(request):
      command  = [line.strip("\n") for line in os.popen("ls").readlines()]
      result = {'result':command}
      return render(request,"command``
      
## 模板和静态文件
* http://www.bootcss.com/  下载静态文件
* tempplates里面田间html模板 index.html 和commands.html

#第二天
## dajngo的models
* Ment---> 数据库中的表名

* Ment的属性对应 --> Ment这个表里的字段
* models.CharField ---> 字符 数据类型
* 还有很多的类型 到官网查看
* python manage.py makemigrations 生成描述文件
* python manage.py migrate 同步数据库
## orm的使用
* python manage.py shell 调用django 自带的shell
* 导入models 模块 from ams.model import Ment
### 增 
* ment = Ment(sn="xxx", ip="xxx", hostname="xxxxx",....)
*  ment.save()
### 查:
* 查询所有 Ment.objects.all()
* 精确 查询 filter :Ment.objects.filter(id=xxx)
* 精确 查询 get :Ment.objects.get(id=xxx)
* filter查询一个不存在的时候 不会报错
* get 查询一个不存在的时候 会报错
### 删除
* Ment.objects.filter(id=xxx).delete()

### 改
*  filter :Ment.objects.filter(id=xxx).update(sn='xxxx'').update()
* M = Ment.objects.get(id=1)
   M.sn = 2
* get :* Ment.objects.get(id=xxxx).save()

# form

# admin

# js
* http://www.w3school.com.cn/b.asp
# http://www.datatables.club/manual/install.html
# http://mishengqiang.com/sweetalert/