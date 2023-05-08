import tkinter as tk
import webbrowser
from searchcourse import SearchCourse
from tkinter import ttk, scrolledtext


# Create a window
root = tk.Tk()
root.geometry('600x500')
root.title('Search Course')

# Create a Frame for the GitHub token entry box and label
token_frame = ttk.Frame(root, padding='10 10 10 0')
token_frame.pack(fill='x')
ttk.Label(token_frame, text='GitHub Token: ').grid(row=0, column=0, sticky='w')
token_entry = ttk.Entry(token_frame, show='*')
token_entry.grid(row=0, column=1, sticky='we')
token_entry.focus()

# Create a Frame for the search keyword entry box and label
keys_frame = ttk.Frame(root, padding='10 10 10 0')
keys_frame.pack(fill='x')
ttk.Label(keys_frame, text='Search Keys: ').grid(row=0, column=0, sticky='w')
keys_entry = ttk.Entry(keys_frame)
keys_entry.grid(row=0, column=1, sticky='we')

# Create a Frame for the search result Text and scrollbar
result_frame = ttk.Frame(root, padding='10 0 10 10')
result_frame.pack(fill='both', expand=True)
ttk.Label(result_frame, text='Search Result: ').pack(side='top', anchor='w')
scrollbar = ttk.Scrollbar(result_frame)
scrollbar.pack(side='right', fill='y')
output_text = scrolledtext.ScrolledText(result_frame, wrap='word', yscrollcommand=scrollbar.set)
output_text.pack(side='left', fill='both', expand=True)
scrollbar.config(command=output_text.yview)

# Create a Frame for the search button
button_frame = ttk.Frame(root, padding='0 10 0 10')
button_frame.pack()
search_button = ttk.Button(button_frame, text='Search', command=lambda: search_course())
search_button.pack()

# Define the search course operation function
def search_course():
    # Clear the search result
    output_text.delete('1.0', tk.END)

    token = token_entry.get()
    keys = keys_entry.get().split(',')
    sc = SearchCourse(token)
    sc.set_keys(keys)
    url_list = sc.search()
    for url in url_list:
        output_text.insert(tk.END, url + '\n')
        text_start = output_text.search(url, tk.END, backwards=False)
        text_end = f'{text_start} + {len(url)} char'
        output_text.tag_add(url, text_start, text_end)
        output_text.tag_config(url, foreground='blue', underline=True)
        output_text.tag_bind(url, '<Enter>', on_enter)
        output_text.tag_bind(url, '<Leave>', on_leave)
        output_text.tag_bind(url, '<Button-1>', on_click)


def on_enter(e):
    output_text.config(cursor='hand2')


def on_leave(e):
    output_text.config(cursor='arrow')


def on_click(e):
    webbrowser.open_new_tab(e.widget.get('current linestart', 'current lineend')) 


# Set the theme style
style = ttk.Style()
style.theme_use('clam')

# Enter the main loop
root.mainloop()
