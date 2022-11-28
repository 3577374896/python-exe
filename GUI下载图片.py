#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2022-11-24 16:15:46
# @Author  : Your Name (you@example.org)
# @Link    : http://example.org
# @Version : $Id$


import requests
from bs4 import BeautifulSoup
import os
import tkinter as tk    # GUI
import concurrent.futures
import threading



def get_content(url):
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    response = requests.get(url,headers)
    response.encoding = response.apparent_encoding  # 自动转码
    if response.status_code == 200:
        return response.text


def get_data(response):
    soup = BeautifulSoup(response,'lxml')
    all_li = soup.find(class_="list").find('ul')
    for i in all_li.find_all('li'):
        if i.find('b') is not None:
            title = i.find('b').text
        else:
            title = 'NOT'
        images = i.find('a').find('img').get('src')
        save_images(title,images)



def save_csv():
    pass

def save_images(title,images):
    if not os.path.exists('img'):   # 创建文件夹
        os.mkdir('img')
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'}
    images_data = requests.get(url=images,headers=headers).content
    with open('img\\' + title + '.jpg', mode='wb')as f:
        f.write(images_data)
        print('正在保存===>: ',title)

    # GUI文本框输入
    qq.insert(tk.INSERT,"正在保存图片:" + title + '\n')
    qq.yview_moveto(1)
    qq.update()



def main():
    print('===================已经点击按钮===========================')
    for i in range(2,11):
        url = f'http://www.netbian.com/index_{i}.htm'  # 循环
        qq.insert(tk.INSERT,f'==========================正在保存第{i}页的图片=========================='+ '\n')
        qq.update()
        print(f'============================正在保存第{i}页的数据内容========================')
        response = get_content(url)
        get_data(response)
    qq.insert(tk.INSERT,'=================================保存结束================================')



# 多线程 防止GUI卡死
def process_it():
    it = threading.Thread(target=main)
    it.setDaemon(True)
    it.start()




if __name__ == '__main__':
    # 设置GUI图形界面
    windoms = tk.Tk()

    windoms.iconbitmap()

    windoms.title('图片')
    windoms.geometry('500x500+650+300')

    # labal
    text = tk.Label(windoms,text='图片小程序',font=('华文新魏',20))
    text.place(x=170,y=10)

    # 按钮
    button = tk.Button(windoms,text='开始下载',font=(20),width=30,height=4,fg='Violet',bd=8,command=process_it)   # 开始下载
    button.place(x=140,y=80)
    button1 = tk.Button(windoms,text='退出',font=(20),width=30,fg='Violet',height=4,bd=8,command=windoms.quit)  # 退出
    button1.place(x=140, y=180)
    # 文本框
    qq = tk.Text(windoms,state='normal',bg='light cyan',fg='DeepPink')
    qq.place(rely=0.6,relheight=0.4)
    # 显示窗口
    tk.mainloop()