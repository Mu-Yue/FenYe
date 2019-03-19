# FenYe
Djangp分页设置
在控制台输入python manager.py runserver 8000启动项目，在浏览器输入http://127.0.0.1:8000/index.html?p=2，此时显示的Django原生的分页组件。
由于Django原生分页组件功能有限，可以通过继承其类，并添加一些方法设置，可以扩展一些功能，在浏览器输入http://127.0.0.1:8000/index1.html?p=2进行查看。
在浏览器输入http://127.0.0.1:8000/index3.html?p=2，这是自定义的分页器，没有用到Django自己的分页器，通用性比较强，为了美观，采用了bootstrap的组件进行了部分美化
