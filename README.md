Djangp分页设置
====
## 1、Django原生分页器
<br>在控制台输入python manager.py runserver 8000启动项目，在浏览器输入http://127.0.0.1:8000/index.html
<br>此页面采用时Django原生的分页组件编写，原生组件功能简单，不能设置分页数。
## 2、Django原生分页器扩展
<br>在浏览器输入http://127.0.0.1:8000/index1.html
<br>此页面通过继承原生分页器的类，对原生分页器进行了扩展，并添加一些方法，可以扩展一些功能。
## 3、通用分页器
<br>在浏览器输入http://127.0.0.1:8000/index2.html
<br>这是自定义的分页器，没有用到Django自己的分页器，通用性比较强，为了美观，采用了bootstrap的组件进行了美化。
