import tkinter as tk
from searchcourse import SearchCourse

# 创建一个窗体
root = tk.Tk()
root.title('Search Course')

# 添加 Label 和 Entry，用于输入 GitHub 访问令牌
tk.Label(root, text='GitHub Token: ').grid(row=0, column=0)
token_entry = tk.Entry(root, show='*')
token_entry.grid(row=0, column=1)

# 添加 Button，用于启动搜索课程操作
def search():
    search_course = SearchCourse(token_entry.get())
    url_list = search_course.search_course()
    for url in url_list:
        print(url)

search_button = tk.Button(root, text='Search', command=search)
search_button.grid(row=1, column=0, columnspan=2)

# 进入主循环
root.mainloop()