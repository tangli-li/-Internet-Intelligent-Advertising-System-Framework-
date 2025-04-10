import tkinter as tk
from page_class import login



class App:
    def __init__(self, root):
        self.root = root
        self.root.geometry("600x300")

        # 创建容器存放所有页面
        self.frames = {}
        self.create_newpage(login,ID=None)

    def show_frame(self, page_class):
        """切换页面"""
        frame = self.frames[page_class]
        frame.tkraise()  # 将目标页面提升到最上层
    def place_frame(self,Page0):
        frame = Page0(self.root, self)
        self.frames[Page0] = frame
        frame.grid(row=0, column=0, sticky="nsew")
    def create_newpage(self,Page0,ID):
        frame0 = Page0(self.root, self, ID=ID)
        frame0.grid(row=0, column=0, sticky="nsew")
        self.frames[Page0] = frame0
        frame0.tkraise()

# 设置整体样式


# 标题标签

# 主内容容器


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()