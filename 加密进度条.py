#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-11-24 16:14:17
# @Author  : 李泽源(QQ：3577374896)
# @Link    : http://example.org
# @Version : 292278229&：

import os
import  tkinter
from tkinter import messagebox
from time import sleep
from tkinter import ttk
root=tkinter.Tk()
root.title('进度条')
root['height']=200
root['width']=400
def Pro_Bar(root):
    #标签
    label=tkinter.Label(root,text='加密进度:',font=('黑体', 12))
    label.place(x=10,y=60)
    progressbar=ttk.Progressbar(root)
    progressbar.place(x=80,y=60)
    progressbar['maximum']=100
    progressbar['length']=300
    def Value_Bar():
        for i in range(101):
            progressbar['value']=i+1
            sleep(0.06)
            # print(i)

            bal=tkinter.Label(root,text=(i))
            bal.place(x=300,y=130)
            bal.pack
            bal1=tkinter.Label(root,text="%")
            bal1.place(x=325,y=130)
            bal1.pack
            
            sleep(0.01)
            root.update()
            if i>=100:
                tkinter.messagebox.askyesno("提示","加密完成，即将关闭！！！")
                sleep(1.0)
                exit()
            elif():
                root.update()
    btn=tkinter.Button(root,text='启动',font=('黑体', 14),cursor='hand2',command=Value_Bar)
    btn.place(x=180,y=130)


if __name__=='__main__':
    Pro_Bar(root)
    root.mainloop()