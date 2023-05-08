import tkinter as tk
from searchcourse import SearchCourse

# 创建一个窗体
root = tk.Tk()
root.title('Search Course')

# 添加 Label 和 Entry，用于输入 GitHub 访问令牌和搜索关键字
tk.Label(root, text='GitHub Token: ').grid(row=0, column=0)
token_entry = tk.Entry(root, show='*')
token_entry.grid(row=0, column=1)

tk.Label(root, text='Search Key: ').grid(row=1, column=0)
key_entry = tk.Entry(root)
key_entry.grid(row=1, column=1)

result_text = tk.Text(root)
result_text.grid(row=2, column=0, columnspan=2)

# 添加 Button，用于启动搜索课程操作
def search():
    search_course = SearchCourse(token_entry.get())
    url_list = search_course.search_course(key_entry.get())
    result_text.delete('1.0', tk.END) # 清空原有的输出内容
    for url in url_list:
        result_text.insert(tk.END, url + '\n')

search_button = tk.Button(root, text='Search', command=search)
search_button.grid(row=3, column=0, columnspan=2)

# 进入主循环
root.mainloop()