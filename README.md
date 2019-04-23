# django_tutorial
Offical demo to study django framework.

## Django简介

Django是一个由python编写的web应用框架，大而全，功能十分强大。

### web框架简介

具体介绍Django之前，必须先介绍WEB框架等概念。

web框架： 别人已经设定好的一个web网站模板，你学习它的规则，然后“填空”或“修改”成你自己需要的样子。

一般web框架的架构是这样的：

![image](https://raw.githubusercontent.com/zhusheng/blog/master/python/django01.png)

其它基于python的web框架，如tornado、flask、webpy都是在这个范围内进行增删裁剪的。
例如tornado用的是自己的异步非阻塞“wsgi”，flask则只提供了最精简和基本的框架。Django则是直接使用了WSGI，并实现了大部分功能。

### MVC和MTV简介

**MVC**

MVC百度百科：全名Model View Controller，是模型(model)－视图(view)－控制器(controller)的缩写，
一种软件设计典范，用一种业务逻辑、数据、界面显示分离的方法组织代码，将业务逻辑聚集到一个部件里面，
在改进和个性化定制界面及用户交互的同时，不需要重新编写业务逻辑。

通俗解释：一种文件的组织和管理形式！不要被缩写吓到了，这其实就是把不同类型的文件放到不同的目录下的一种方法，
然后取了个高大上的名字。当然，它带来的好处有很多，比如前后端分离，松耦合等等，就不详细说明了。　　　　　　　

- 模型(model)：定义数据库相关的内容，一般放在models.py文件中。
- 视图(view)：定义HTML等静态网页文件相关，也就是那些html、css、js等前端的东西。
- 控制器(controller)：定义业务逻辑相关，就是你的主要代码。　　

**MTV**

有些WEB框架觉得MVC的字面意思很别扭，就给它改了一下。view不再是HTML相关，而是主业务逻辑了，相当于控制器。
html被放在Templates中，称作模板，于是MVC就变成了MTV。这其实就是一个文字游戏，和MVC本质上是一样的，换了个名字和叫法而已，换汤不换药。

### Django的MTV模型组织

目录分开，就必须有机制将他们在内里进行耦合。在Django中，urls、orm、static、settings等起着重要的作用。一个典型的业务流程是如下图所示：

![image](https://raw.githubusercontent.com/zhusheng/blog/master/python/django02.png)

那么我们学Django学的是什么？

1. 目录结构规范
2. urls路由方式
3. settings配置
4. ORM操作
5. 模板渲染
6. 其它

## Django安装

安装
`pip install Django`

查看版本（bash）
`python -m django --version`

查看版本（python shell）
```
>>> import django
>>> print(django.get_version())
2.2
```

## 常用操作指令

- 创建项目
`django-admin startproject django_tutorial`

- 新建app,名称为polls,一个功能模块就是一个app
```bash
cd django_tutorial
python3 manage.py createapp polls
```

- 启动服务
`python3 manage.py runserver`

- 初始化数据库和更新数据库
```bash
python3 manage.py makemigrations  # 建立我们对model的操作档案
python3 manage.py migrate   # 应用我们的档案去操作数据库
```

- 删除数据库并重建数据库
```bash
rm -f db.sqlite3
rm -r polls/migrations
python manage.py makemigrations polls
python manage.py migrate
```

## 说明

1. 访问一个app的方式,127.0.0.1:8000/polls、 127.0.0.1:8000/admin
2. django给我们内置了很多app和功能模块，常用的就是admin，它是一个管理后台app。如果我们想要使用这个app，我们需要创建一个用户即可使用。创建用户的指令`python3 manage.py createsuperuser`.
3. admin app是可以操作数据库的，如果我们想要我们的amdin app可以操作某个app的数据库，我们需要在这个app下的admin.py文件中使用admin进行注册即可。
```python
from  .models import Question, Choice

admin.site.register(Question)
admin.site.register(Choice)
```
如果我们想要定义admin对model的操作和显示，我们可以在该文件中进行自定义，可以参考本项目的[admin.py](https://github.com/zhusheng/django_tutorial/blob/master/polls/admin.py)文件。
4. 连接SQLite3数据库。Django内置默认使用的是SQLite3数据库，而且也无需密码，我们可以使用Navicat连接数据库，操作如下：
![image](https://raw.githubusercontent.com/zhusheng/blog/master/django/01.png)
![image](https://raw.githubusercontent.com/zhusheng/blog/master/django/02.png)
5. 修改数据库
（1）SQLite3（Default）
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'mydatabase',
    }
}

```

（2）MySQL
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'snkey', # database name
        'USER': 'root', # username
        'PASSWORD': 'admin888', # password
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

（3）PostgreSQL
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'postgres', # database name
        'USER': 'postgres', # username
        'PASSWORD': '111111', # password
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

## 学习建议

作为python必须web框架的Django，它的功能强大，内容全面，但同时也意味着限制颇多，灵活性低，可修改性差，这就是鱼和熊掌不可兼得了。
我们学习Django，其实就是学习一个软件，要理解它的基本原理，把握它整体框架，牢记一些基本规则，剩下的就是不断深入细节，
然后熟能生巧、经验多少的问题了，不存在多高深的不可掌握技术。 

关于学习方法的建议：学习任何东西，不要直接扎入细节，应该先了解它的外围知识，看看它的整体架构，
再学习它的基本内容，然后才是深入学习，打磨技巧！ 
