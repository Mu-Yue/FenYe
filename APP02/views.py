from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from APP02.pager import Pagination

USER_LIST = []
for i in range(1, 666):
    temp = {'Name': 'ROOT' + str(i), 'Age': i}
    USER_LIST.append(temp)


class CustomPainator(Paginator):
    def __init__(self, current_page, per_page_num, *args, **kwargs):
        self.current_page = current_page  # 当前页
        self.per_page_num = per_page_num  # 最多显示的页码数量
        super(CustomPainator, self).__init__(*args, **kwargs)

    def pager_num_range(self):
        if self.num_pages < self.per_page_num:  # 总页数小于要显示的页数
            return range(1, self.num_pages + 1)
        part = int(self.per_page_num / 2)  # 中间页码
        if int(self.current_page) <= part:
            return range(1, self.per_page_num + 1)
        if (int(self.current_page) + part) > self.num_pages:
            return range(int(self.num_pages) - self.per_page_num, int(self.num_pages) + 1)
        return range(int(self.current_page) - part, int(self.current_page) + part + 1)


# Django原生分页组件
def index(request):
    per_page_count = 10
    current_page = request.GET.get('p')
    current_page = int(current_page)

    start = (current_page - 1) * per_page_count
    end = current_page * per_page_count
    data = USER_LIST[start:end]

    prev_pager = current_page - 1
    next_pager = current_page + 1
    return render(request, 'index.html', {'user_list': data, 'prev_pager': prev_pager, 'next_pager': next_pager})


# 在Django原生分页组件扩展自定制，只适用于Django
def index1(request):
    current_page = request.GET.get('p')
    paginator = CustomPainator(current_page, 7, USER_LIST, 10)
    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger:
        posts = paginator.page(1)  # 非数字，非法参数
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)  # 传入空页情况处理
    return render(request, 'index1.html', {'posts': posts})


# 自定义分页组件
def index2(request):
    current_page = request.GET.get('p')
    page_obj = Pagination(666, current_page)

    data_list = USER_LIST[page_obj.start():page_obj.end()]
    return render(request, 'index2.html', {'data': data_list, 'page_obj': page_obj})
