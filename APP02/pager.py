# Time: 2019/3/19 12:40
# Author: MuYue
# File: pager.py


class Pagination(object):
    def __init__(self, totalCount, currentPage, perPageItemNum = 30, maxPageNum = 7):
        self.total_count = totalCount  # 所有数据的个数，是个数，不是所有的数据
        try:
            v = int(currentPage)
            if v <= 0:
                v = 1
            self.current_page = v  # 当前页
        except Exception as e:
            self.current_page = 1
        self.per_page_item_num = perPageItemNum  # 每页最多显示显示的数目（30条）
        self.max_page_num = maxPageNum  # 最多页面（7页）

    def start(self):
        return (self.current_page - 1) * self.per_page_item_num

    def end(self):
        return self.current_page * self.per_page_item_num

    @property
    def num_pages(self):  # 计算总页数，加上@property后就可以用self.num_pages代替self.num_pages()，方法后边的括号会自动添加
        a, b = divmod(self.total_count, self.per_page_item_num)
        if b == 0:
            return a
        return a + 1

    def pager_num_range(self):
        if self.num_pages < self.max_page_num:  # 总页数小于要显示的页数
            return range(1, self.num_pages + 1)
        part = int(self.max_page_num / 2)  # 中间页码
        if self.current_page <= part:
            return range(1, self.max_page_num + 1)
        if (self.current_page + part) > self.num_pages:
            return range(self.num_pages - self.max_page_num + 1, self.num_pages + 1)
        return range(self.current_page - part, self.current_page + part + 1)

    def page_str(self):
        page_list = []
        first_page = "<li><a href='/index2.html?p=1'>首页</a></li>"
        page_list.append(first_page)

        if self.current_page == 1:
            prev = "<li><a href='#'>上一页</a></li>"
        else:
            prev = "<li><a href='/index2.html?p=%s'>上一页</a></li>" % (self.current_page - 1)
        page_list.append(prev)

        for i in self.pager_num_range():
            if i == self.current_page:
                temp = "<li class='active'><a href='/index2.html?p=%s'>%s</a></li>" % (i, i)
            else:
                temp = "<li><a href='/index2.html?p=%s'>%s</a></li>" % (i, i)
            page_list.append(temp)

        if self.current_page == self.num_pages:
            nex = "<li><a href='#'>下一页</a></li>"
        else:
            nex = "<li><a href='/index2.html?p=%s'>下一页</a></li>" % (self.current_page + 1)
        page_list.append(nex)

        last_page = "<li><a href='/index2.html?p=%s'>尾页</a></li>" % (self.num_pages,)
        page_list.append(last_page)

        return ''.join(page_list)

