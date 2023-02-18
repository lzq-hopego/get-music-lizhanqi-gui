from PyQt5.Qt import *
from PyQt5.QtCore import QTimer, QUrl,QPoint
from PyQt5.QtMultimedia import QMediaPlayer,QMediaPlaylist, QMediaContent
from PyQt5.QtWidgets import QMenu,QAction,QMessageBox,QFileDialog
from PyQt5 import QtGui
import sys,os
from ui2 import Ui_MainWindow
import re
import cv2
from get_music import *
import numpy as np
import downloader
import pathlib
import random


class Window(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        
        self.music_path='./music'   #初始化本地歌单位置
        self.switch = False#窗体是否被拖动
        self.mixer=QMediaPlayer()
        self.timer=QTimer()
        self.timer2=QTimer()

        self.playlist=QMediaPlaylist()


          
        # self.init_widget_background()
        self.sys_argv_init=False #用户是否使用拖拽文件的方式打开了本程序
        self.init_gedan()  #初始化歌单
        
        


        self.soupage=False #用于搜索结果和歌词界面切换
        self.rotate=0 #记录封面旋转的角度
        self.music_speed=1.0 #定义音乐播放速度
        
        self.look_fengmian=False  #封面是否隐藏
        #封面是否旋转
        self.turn_fengmian=False
        self.init_play_back_mode()# 初始化播放模式
        self.init_volume()# 初始化音量条
        self.init_fengmian()# 初始化歌曲封面
        self.this_songtime(0)#初始化歌词歌曲时长
        self.ui.listWidget_2.setVisible(False)#初始化listwidget2为不显示状态
        # #初始化歌词显示
        self.init_lrc()

        self.diy_background=False  #当前是否背景自定义
        # self.widget_transparent=False   #窗体当前状态是否透明

        self.ui.horizontalSlider_2.valueChanged.connect(self.setvolume)
        self.ui.horizontalSlider.sliderMoved.connect(self.upgrade_value)  
        # self.ui.horizontalSlider.sliderReleased.connect(self.upgrade_value)
        self.ui.horizontalSlider.sliderReleased.connect(self.setvalue)
        self.ui.pushButton_2.clicked.connect(self.previous)
        self.ui.pushButton_3.clicked.connect(self.dianji)
        self.ui.pushButton.clicked.connect(self.dianji)
        self.ui.pushButton_4.clicked.connect(self.next)
        self.ui.pushButton_5.clicked.connect(self.set_play_back_mode)
        self.ui.pushButton_7.clicked.connect(self.set_volume_zero)
        self.playlist.currentIndexChanged.connect(self.init_fengmian)
        self.ui.listWidget.doubleClicked.connect(self.double_list)
        self.mixer.positionChanged.connect(self.this_songtime)
        self.ui.pushButton_11.clicked.connect(self.dis_one)
        self.ui.pushButton_12.clicked.connect(self.undis_one)
        self.ui.pushButton_6.clicked.connect(self.search)
        self.ui.listWidget_2.doubleClicked.connect(self.list_download)
        self.ui.pushButton_8.clicked.connect(self.fengmian)
        # self.ui.pushButton_13.clicked.connect(self.beisu)
        # self.ui.pushButton.doubleClicked.connect(self.fengmian)
        # self.ui.pushButton_3.clicked.connect(self.dis_one)
        # self.ui.pushButton_7.clicked.connect(self.undis_one)
        # self.ui.widget_4.setVisible(False)


        self.ui.listWidget.setContextMenuPolicy(3)
        self.ui.listWidget.customContextMenuRequested[QPoint].connect(self.rightMenuShow)

        self.ui.frame_19.setContextMenuPolicy(3)
        self.ui.frame_19.customContextMenuRequested[QPoint].connect(self.rightMenuShowFrame)

        self.ui.frame_15.setContextMenuPolicy(3)
        self.ui.frame_15.customContextMenuRequested[QPoint].connect(self.rightMenuShowFrame)

        self.ui.pushButton_8.setContextMenuPolicy(3)
        self.ui.pushButton_8.customContextMenuRequested[QPoint].connect(self.rightMenuShowbutton_8)

        
        #判断是否在播放时旋转封面，注意由于qt的限制我无法实现圆形封面旋转
        #采用的opencv圆形检测后并保存为test.jpg文件后再显示的，非常消耗内存，默认关闭
        self.timer.timeout.connect(self.r_fengmian)
        self.timer2.timeout.connect(self.init_widget_background)
        # self.timer2.start(10000)
        # self.un_background()

        #初始化搜索引擎
        self.song_name_list=[]
        self.singer_name_list=[]
        self.api={'酷狗音乐':kugou.kugou(),
       '网易云':netease.netease(),
       'QQ音乐':qq.qq(),
       '酷我音乐':kuwo.kuwo(),
       '咪咕音乐':migu.migu(),
       '千千静听':baidu.baidu(),
       '一听音乐':oneting.oneting(),
       '51原唱':fivesing.fivesing('yc'),
       '51翻唱':fivesing.fivesing('fc')
       }
        self.song_name_list=[]
        self.singer_name_list=[]
        self.song_id_list=[]
    def init_img_list(self):
        directory = QFileDialog.getExistingDirectory(None,"选取文件夹")
        # path=''
        if directory=='':
            return
        dirlist=os.listdir(directory)
        ls=[]
        for j in dirlist:
            if '.jpg' in j:
                p=pathlib.PureWindowsPath(directory+'\\'+j)
                r=str(p.as_posix())
                ls.append(r)
        self.img_list=ls
        self.img_num=0
        self.init_widget_background()
        self.timer2.start(5000)

    def un_background(self):
        self.ui.frame_15.setStyleSheet("background-color: transparent;")
        self.ui.frame_16.setStyleSheet("background-color: transparent;")
        self.ui.frame_19.setStyleSheet("#frame_19{background-color: transparent;border-bottom-left-radius:20px;}")
        self.ui.frame_18.setStyleSheet("background-color: transparent;")
        self.ui.frame_17.setStyleSheet("#frame_17{background-color: transparent;border-top-left-radius:20px;}")
        self.ui.frame.setStyleSheet("#frame{border-top-left-radius:22px;border-bottom-left-radius:22px;background-color: transparent;}")
        self.ui.frame_3.setStyleSheet("#frame_3{ border-top-right-radius:22px; background-color: transparent; }")
        self.ui.frame_13.setStyleSheet("background-color: transparent;")
        self.ui.frame_12.setStyleSheet("background-color: transparent;")
        self.ui.frame_14.setStyleSheet("background-color: transparent;border-top-right-radius:20px;")
#         self.ui.widget.setAttribute(Qt.WA_TranslucentBackground,True)
#         self.ui.widget.setAttribute(Qt.WA_NoSystemBackground,False)
#         self.ui.widget.setStyleSheet("#widget{background-color: transparent;\n"
# "border-radius:22px;}")

    def do_background(self):
        self.ui.frame_15.setStyleSheet("background-color: rgb(255, 144, 179);")
        self.ui.frame_16.setStyleSheet("background-color: rgb(203, 255, 194);")
        self.ui.frame_19.setStyleSheet("#frame_19{background-color: rgb(196, 209, 255);border-bottom-left-radius:20px;}")
        self.ui.frame_18.setStyleSheet("background-color: rgb(250, 176, 255);")
        self.ui.frame_17.setStyleSheet("#frame_17{background-color: rgb(255, 207, 192);border-top-left-radius:20px;}")
        self.ui.frame.setStyleSheet("#frame{border-top-left-radius:22px;border-bottom-left-radius:22px;background-color: rgb(255, 170, 0);}")
        self.ui.frame_3.setStyleSheet("#frame_3{ border-top-right-radius:22px; background-color: rgb(255, 0, 127); }")
        self.ui.frame_13.setStyleSheet("background-color: rgb(212, 255, 235);")
        self.ui.frame_12.setStyleSheet("background-color: rgb(255, 210, 254);")
        self.ui.frame_14.setStyleSheet("background-color: rgb(255, 245, 221);border-top-right-radius:20px;")
        self.timer2.stop()  #关闭定时器
        self.diy_background=False
        self.ui.widget.setStyleSheet("#widget{background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:1, stop:0.00515464 rgba(85, 170, 255, 255), stop:1 rgba(245, 134, 255, 255));\n"
"border-radius:22px;}")
        # self.init_widget_background()
    def init_widget_background(self):
        #初始化自定义封面文件夹中的.jpg文件,如果没检测到,配置不生效,如果只有一张图片,将在第三次不再随机轮播图片以免消耗内存
        if len(self.img_list)<1:
            self.do_background()
            self.diy_background=False
            self.timer2.stop()
            print('未检测到.jpg文件')
            return
        elif len(self.img_list)==1:
            self.un_background()
            self.diy_background=True
            self.timer2.stop()
        else:
            self.un_background()
            self.diy_background=True
        img_num=random.randint(0,len(self.img_list)-1)
        if img_num==self.img_num:
            self.img_num=img_num=random.randint(0,len(self.img_list)-1)
        else:
            self.img_num=img_num
        url=self.img_list[self.img_num]
        # print(url)
        self.ui.widget.setStyleSheet("#widget{border-radius:22px;\nborder-image: url("+url+");\n}")
        # self.ui.widget.setWindowOpacity(0.5)


    def rightMenuShowFrame(self):
        #在最左侧紫色区域或歌词区域右键弹出自定义背景或取消自定义背景,选择带有.jpg文件的文件夹
        menu=QMenu()
        menu.setStyleSheet("font: 12pt \"幼圆\";\n"
    "color: rgb(255, 128, 128);")
        if self.diy_background:
            menu.addAction(QAction(u'取消自定义背景', self,triggered=self.do_background)) #取消自定义背景
            menu.addAction(QAction(u'更改自定义背景', self,triggered=self.init_img_list))
        else:
            menu.addAction(QAction(u'自定义背景', self,triggered=self.init_img_list))  #自定义背景
        if self.soupage==False:
            if self.look_fengmian:
                menu.addAction(QAction(u'取消隐藏', self,triggered=self.look_true_pushButton_8)) #取消隐藏
            else:
                menu.addAction(QAction(u'隐藏封面', self,triggered=self.look_false_pushButton_8))  #隐藏封面

        menu.exec_(QtGui.QCursor.pos())
    def rightMenuShowbutton_8(self):
    
        menu=QMenu()
        menu.setStyleSheet("font: 12pt \"幼圆\";\n"
    "color: rgb(255, 128, 128);")
        if self.turn_fengmian:
            menu.addAction(QAction(u'取消旋转', self,triggered=self.fengmian)) #取消旋转
        else:
            menu.addAction(QAction(u'旋转封面', self,triggered=self.fengmian))  #旋转封面
        if self.look_fengmian==False:
        #     menu.addAction(QAction(u'取消隐藏', self,triggered=self.look_true_pushButton_8)) #取消隐藏
        # else:
            menu.addAction(QAction(u'隐藏封面', self,triggered=self.look_false_pushButton_8))  #隐藏封面

        menu.exec_(QtGui.QCursor.pos())
    def rightMenuShow(self):
        #歌单右键,在歌单只有一首歌的时候右键不会显示删除
        def shanchu():
            num=self.ui.listWidget.currentRow()
            songname=self.songnamelist[num].split('.')[0]
            a = QMessageBox.question(self, '删除', '你是否要删除本地文件？', QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
            if a==QMessageBox.Yes:
                if self.sys_argv_init:
                    os.remove(self.songnamelist[num])     #如果用户以拖拽文件的方式打开，就直接按照原路径删除
                else:
                    dirlist=os.listdir('./music')
                    for i in dirlist:
                        if i.split('.')[-1] in ['mp3','jpg','lrc','txt']:
                            # return   #删除保护，不删除其他同名但扩展名不同的文件
                            if i.split('.')[0]==songname:
                                os.remove('./music/'+i)
                                print('已删除：'+'./music/'+i)
            else:
                print('下次刷新将会重新显示！')
            self.songnamelist.pop(num)
            self.ui.listWidget.takeItem(num)
            if self.playlist.currentIndex()==num:
                self.init_fengmian()   #有可能删除的是正在播放的歌曲，所以在删除之后刷新一下封面和歌词信息
            self.playlist.removeMedia(num)
        def init_gedan():
                self.playlist.removeMedia(0,len(self.songnamelist)-1)
                self.ui.listWidget.clear()
                if os.path.exists('./music')==False:
                    os.mkdir('./music') 
                dirlist=os.listdir('./music')
                self.songnamelist=[]
                for i in dirlist:
                    if '.mp3' in i:
                        self.songnamelist.append(i)
                        self.playlist.addMedia(QMediaContent(QUrl("./music/{}".format(i))))
                if self.songnamelist==[]:
                    with open("./music/使用说明.txt",'w') as f:
                        f.write("[00:00.19]检测到music文件夹为空")
                        f.write("\r\n")
                        f.write("[00:01.11]所以请开始搜索下载吧")
                    self.songnamelist.append('使用说明-开发者.mp3')
                    self.playlist.addMedia(QMediaContent(QUrl("./使用说明-开发者.mp3")))
                self.songnum=0  # 用于控制当前播放的是哪一首音乐
                self.uptime=True #是否可以更新播放进度条，当用户拖动进度条时，不更新进度条，否则会造成当前播放进度显示出错
                self.state="stop" #定义播放器当前状态
                self.playlist.setCurrentIndex(self.songnum)
                self.mixer.setPlaylist(self.playlist) #加入歌单
                self.songtitle()#初始化左下角显示歌曲名
                self.init_list()#初始化列表


        menu=QMenu()
        menu.setStyleSheet("font: 12pt \"幼圆\";\n"
    "color: rgb(255, 128, 128);")

        menu.addAction(QAction(u'播放', self, triggered=self.double_list))  #播放当前选中的条目 
        if len(self.songnamelist)>1:
            menu.addAction(QAction(u'删除', self, triggered=shanchu))  #删除当前选中的条目
        menu.addAction(QAction(u'刷新', self, triggered=init_gedan))  #刷新歌单
        menu.exec_(QtGui.QCursor.pos())
    #初始化歌单
    def init_gedan(self):
        
        print(sys.argv)
        if len(sys.argv[1:])>=1:
            self.music_path='\\'.join(sys.argv[0].split('\\')[:-1])+"\\music"
            print(self.music_path)
            self.songnamelist=[]
            ls=sys.argv[1:]
            for i in ls:
                if '.mp3' in i:
                    p=pathlib.PureWindowsPath(i)
                    r=str(p.as_posix())
                    try:
                        self.playlist.addMedia(QMediaContent(QUrl(r)))
                        self.songnamelist.append(i)
                        print(i)
                    except:
                        print("本程序无法播放,所以不予加载:"+i)
                else:
                    print("本程序无法播放,所以不予加载:"+i)
            if len(self.songnamelist)>=1:
                self.songnum=0  # 用于控制当前播放的是哪一首音乐
                self.uptime=True #是否可以更新播放进度条，当用户拖动进度条时，不更新进度条，否则会造成当前播放进度显示出错
                self.state="stop" #定义播放器当前状态
                self.playlist.setCurrentIndex(self.songnum)
                self.mixer.setPlaylist(self.playlist) #加入歌单
                self.songtitle()#初始化左下角显示歌曲名
                self.init_list()#初始化列表
                self.sys_argv_init=True #用户使用拖拽文件的方式打开了本程序
                return
            # else:
            #     return
        if os.path.exists('./music')==False:
            os.mkdir('./music') 
        dirlist=os.listdir('./music')
        self.songnamelist=[]
        for i in dirlist:
            if '.mp3' in i:
                self.songnamelist.append(i)
                self.playlist.addMedia(QMediaContent(QUrl("./music/{}".format(i))))
        if self.songnamelist==[]:
            with open("./music/使用说明.txt",'w') as f:
                f.write("[00:00.19]检测到music文件夹为空")
                f.write("\r\n")
                f.write("[00:01.11]所以请开始搜索下载吧")
            self.songnamelist.append('使用说明-开发者.mp3')
            self.playlist.addMedia(QMediaContent(QUrl("./使用说明-开发者.mp3")))
        self.songnum=0  # 用于控制当前播放的是哪一首音乐
        self.uptime=True #是否可以更新播放进度条，当用户拖动进度条时，不更新进度条，否则会造成当前播放进度显示出错
        self.state="stop" #定义播放器当前状态
        self.playlist.setCurrentIndex(self.songnum)
        self.mixer.setPlaylist(self.playlist) #加入歌单
        self.songtitle()#初始化左下角显示歌曲名
        self.init_list()#初始化列表



    def look_true_pushButton_8(self):
        self.ui.pushButton_8.setVisible(True)
        self.look_fengmian=False
        self.timer.start(250)
    def look_false_pushButton_8(self):
        self.ui.pushButton_8.setVisible(False)
        self.look_fengmian=True
        self.timer.stop()
    #设置展示搜索列表,不展示歌词和大封面
    def undis_one(self):
        if self.soupage==False:
            self.ui.label_5.setVisible(False)
            self.ui.label_6.setVisible(False)
            self.ui.label_7.setVisible(False)
            self.ui.label_8.setVisible(False)
            self.ui.label_9.setVisible(False)
            self.ui.label_10.setVisible(False)
            self.ui.label_11.setVisible(False)
            self.ui.pushButton_8.setVisible(False)
            self.ui.listWidget_2.setVisible(True)
            self.soupage=True
    #设置不展示搜索列表,展示歌词和大封面
    def dis_one(self):
        if self.soupage:
            self.ui.label_5.setVisible(True)
            self.ui.label_6.setVisible(True)
            self.ui.label_7.setVisible(True)
            self.ui.label_8.setVisible(True)
            self.ui.label_9.setVisible(True)
            self.ui.label_10.setVisible(True)
            self.ui.label_11.setVisible(True)
            if self.look_fengmian==False:
                self.ui.pushButton_8.setVisible(True)
            self.ui.listWidget_2.setVisible(False)
            self.soupage=False
            # self.look_fengmian=False
    #搜索歌名,歌手,歌词
    def search(self):
        self.is_api=self.api[self.ui.comboBox.currentText()]
        text=self.ui.lineEdit.text()
        if text=='':
            print("没有输入内容")   #搜索保护
            return
        self.ui.listWidget_2.clear()

        #搜索,另开线程以免搜索的服务器长时间无反应导致界面假死
        self.my_thread = search_thread(text,self.is_api)
        self.my_thread.mysignal.connect(self.search_print)
        self.my_thread.start()
        self.ui.listWidget_2.addItem("正在搜索中....")
        
        
    def search_print(self,song):
        song_name_list=song[0]
        singer_name_list=song[1]
        song_id_list=song[-1]
        self.song_name_list,self.singer_name_list,self.song_id_list=song_name_list,singer_name_list,song_id_list
        self.ui.listWidget_2.clear()
        try:
            
            for i in range(min(len(song_name_list),len(singer_name_list))):
                name=song_name_list[i]+"\t"+singer_name_list[i]
                self.ui.listWidget_2.addItem(name)
        except:
            if self.song_name_list=='':
                self.ui.listWidget_2.addItem("搜索结果为空")
            else:
                self.ui.listWidget_2.addItem("接口失效,可以联系管理员进行修复，QQ邮箱：310197835@qq.com")
        self.ui.listWidget_2.setVisible(True)
        self.soupage=True

    #双击指定位置,下载其歌曲数据
    def list_download(self):
        num=self.ui.listWidget_2.currentRow()
        songname=self.song_name_list[num]
        singer=self.singer_name_list[num]
        name=songname+"-"+singer
        id=self.song_id_list[num]

        try:
            self.url=self.is_api.get_music_url(id)
        except:
            print("无法解析下载链接，无法下载")
            return

        
        img_url=self.is_api.get_music_pic(num,return_url=True)
        lrc_url=self.is_api.get_music_lrc(num,return_url=True)

        rstr = r"[\/\\\:\*\?\"\<\>\|\&\•\·]"  # '/ \ : * ? " < > |'
        self.name = re.sub(rstr, "_", name)  # 替换为下划线

        # print(img_url,self.url)
        # 使用rich官方给的代码进行下载，是支持同时下载的  命令行    downloader.py url name url2 name2   最大支持4个任务同时下载
        self.my_thread1 = mythread("./music/"+self.name+".jpg",img_url,"./music/"+self.name+".mp3",self.url)
        self.my_thread1.mysignal.connect(self.addmusic)
        self.my_thread1.start()
 
        try:
            if "http" in lrc_url:
                    download.download(lrc_url,"./music/"+self.name+".lrc",or_re=False)
            else:
                try:
                    with open("./music/"+self.name+".txt",'w') as f:
                        f.write(lrc_url)
                except:
                    with open("./music/"+self.name+".txt",'w',encoding="utf-8") as f:
                        f.write(lrc_url)
        except:
            print('无法获取歌词链接')

# #自动播放需要等到线程结束后再做，因为线程中直接自动播放会无法正常加载歌词和封面
    def addmusic(self,text):
        print(text)
        self.ui.listWidget.addItem(text[0]+".mp3")
        self.songnamelist.append(text[0]+".mp3")
        if self.state=="stop":
                    self.playlist.addMedia(QMediaContent(QUrl("./music/{}".format(self.songnamelist[-1]))))
                    self.playlist.setCurrentIndex(len(self.songnamelist)-1)
                    
                    self.dianji()
        else:
            self.playlist.addMedia(QMediaContent(QUrl("./music/{}".format(self.songnamelist[-1]))))
            self.playlist.setCurrentIndex(len(self.songnamelist)-1)
        # print(len(self.songnamelist)-1)

        
    #初始化本地歌单列表,以及歌单的双击事件
    def init_list(self):
        self.ui.listWidget.addItems(self.songnamelist)
    def double_list(self,index):
        num=self.ui.listWidget.currentRow()
        self.playlist.setCurrentIndex(num)
        if self.state=="stop":
            self.dianji()

    #歌曲的播放和暂停
    def dianji(self):
        if self.state=="start":
            self.state="stop"
            self.mixer.pause()
            self.ui.pushButton_3.setIcon(QIcon(":/image/image/播放_play.png"))
            self.timer.stop()
        elif self.state=="stop":
            self.state="start"
            self.mixer.play()
            self.ui.pushButton_3.setIcon(QIcon(":/image/image/暂停_pause-one.png"))
            self.timer.start(250)
    #下一首
    def next(self):
        if self.playlist.nextIndex()==-1:
            self.state="stop"
            self.dianji()
            self.dianji()
        self.playlist.next()
        self.this_songtime(0)
        
    #上一首
    def previous(self):
        if self.playlist.previousIndex()==-1:
            self.state="stop"
            self.dianji()
            self.dianji()
        self.playlist.previous()
        self.this_songtime(0)


    # 获取当前播放歌曲名
    def songtitle(self):
        name=self.songnamelist[self.playlist.currentIndex()]
        #防止因歌曲名字过长导致无法正常显示进度条

        ls=name.split('-')
        if len(ls)>2:
            songname='-'.join(ls[:-1])
            singer=ls[-1].split('.')[0]
        elif len(ls)<2:
            songname=name.split('.')[0]
            singer='未知歌手'
        else:
            songname,singer=name.split("-")[0],name.split("-")[-1].split(".")[0]
        if len(songname)>15:
            songname=songname[:15]+"..."
        elif len(singer)>15:
            singer=singer[:15]+"..."

        self.ui.label.setText(songname)
        self.ui.label_2.setText(singer)
    # 获取歌曲长度
    def init_songtime(self):
        time_long=self.mixer.duration()
        self.ui.horizontalSlider.setRange(0,time_long)
        self.ui.label_4.setText(str(int(time_long / 1000) // 60).zfill(2) + ':' + str(int(time_long / 1000) % 60).zfill(2))
    # 获取当前播放进度
    def this_songtime(self,index):
        if self.uptime:
            self.init_songtime()
            time_long=self.mixer.position()
            self.ui.horizontalSlider.setValue(time_long)
            self.ui.label_3.setText(str(int(time_long / 1000) // 60).zfill(2) + ':' + str(int(time_long / 1000) % 60).zfill(2))
        #刷新歌词
        if self.show_lrc==True:
            self.get_lrc_by_time(index)
    #滑动滑块调整歌曲进度
    def setvalue(self):
        value=self.ui.horizontalSlider.value()
        self.mixer.setPosition(value)
        self.uptime=True

    #拖动滑块，更新播放显示的时间
    def upgrade_value(self,value):
        self.uptime=False
        self.ui.label_3.setText(str(int(value / 1000) // 60).zfill(2) + ':' + str(int(value / 1000) % 60).zfill(2))
        
    # 初始化音量进度条及图标
    def init_volume(self):
        num=self.mixer.volume()
        self.ui.horizontalSlider_2.setRange(0,num)
        self.ui.horizontalSlider_2.setValue(self.mixer.volume())
        self.set_volume_ico()
    # 设置音量并设置图标
    def setvolume(self):
        value=self.ui.horizontalSlider_2.value()
        self.mixer.setVolume(value)
        self.set_volume_ico()
    #点击图标将音量置为0或80
    def set_volume_zero(self):
        if self.ui.horizontalSlider_2.value() >0:
            self.ui.horizontalSlider_2.setValue(0)
        else:
            self.ui.horizontalSlider_2.setValue(80)
        self.setvolume()
        self.set_volume_ico()
    #更新图标
    def set_volume_ico(self):
        value=self.ui.horizontalSlider_2.value()
        # print(value)
        if value >=80:
            self.ui.pushButton_7.setIcon(QIcon(":/image/image/bx-volume-full.png"))
        elif value >= 50:
            self.ui.pushButton_7.setIcon(QIcon(":/image/image/bx-volume-low.png"))            
        elif value >=10:
            self.ui.pushButton_7.setIcon(QIcon(":/image/image/bx-volume.png"))
        elif value ==0:
            self.ui.pushButton_7.setIcon(QIcon(":/image/image/bx-volume-mute.png"))
    #初始化播放模式
    def init_play_back_mode(self):
        self.playlist.setPlaybackMode(self.playlist.Loop)
    #设置播放模式，并修改图标
    def set_play_back_mode(self):
        ls=[self.playlist.CurrentItemInLoop,self.playlist.Loop,self.playlist.Random]
        mode=["单曲循环","列表循环","随机播放"]
        lt=[QIcon(":/image/image/cycle_one.png"),QIcon(":/image/image/cycle.png"),QIcon(":/image/image/random.png")]
        num=self.playlist.playbackMode()
        # print(num)
        if num==3:
            s=2
        elif num==4:
            s=0
        elif num==1:
            s=1
        self.playlist.setPlaybackMode(ls[s])
        self.ui.pushButton_5.setIcon(lt[s])
        print(mode[s])
    #初始化封面,内含初始化歌词、初始化封面旋转角度、初始化标题
    def init_fengmian(self):
        #更新当前播放的歌曲在列表中显示
        # print(self.self.playlist.currentIndex())
        if len(self.songnamelist)-1<=self.playlist.previousIndex():
            self.ui.listWidget.setCurrentRow(0)
        else:
            self.ui.listWidget.setCurrentRow(self.playlist.currentIndex())
        #更新标题和歌曲封面
        self.songtitle()
        dirlist=os.listdir('./music')
        ls=[]
        for i in dirlist:
            if self.songnamelist[self.playlist.currentIndex()].split(".")[0] in i:
                if '.jpg' in i:
                    ls.append(i)
        if len(ls)>=1:
            
            self.ui.pushButton.setStyleSheet("border-radius:40px;\n"
"border-image: url(./music/{});\n".format(ls[0]))
            self.img=self.init_cv_circle("./music/{}".format(ls[0]))
            self.ui.pushButton_8.setStyleSheet("border-radius:80px;\n"
"border-image: url(./music/{});\n".format(ls[0]))

        else:
            self.ui.pushButton_8.setStyleSheet("border-radius:80px;\n"
                "border-image: url(:/image/image/5.jpg);\n"
            )
            self.ui.pushButton.setStyleSheet("border-radius:40px;\n"
            "border-image: url(:/image/image/5.jpg);\n"
            )
            self.img=self.qtpixmap_to_cvimg(QPixmap(":/image/image/5.jpg"))
    
        #初始化封面
        
        self.slotRotate()

        self.show_lrc=True
        #初始化歌词显示
        self.init_lrc()
        
        self.time_list,self.lrc_dict=self.get_lrc()
        if self.time_list==None:
            self.show_lrc=False
            self.ui.label_8.setText("未找到该歌曲的歌词")
        else:
            self.get_lrc()
            #初始化1秒的时候的歌词，肉眼上歌词加载快了点
            self.get_lrc_by_time(1000)
        self.rotate=0  #初始化封面旋转角度

    #初始化歌词列表
    def get_lrc(self):
        dirlist=os.listdir('./music')
        songlrcname=[]
        for i in dirlist:
            if self.songnamelist[self.playlist.currentIndex()].split('.')[0] in i:
                if '.txt' in i:
                    songlrcname.append(i)
                elif ".lrc" in i:
                    songlrcname.append(i)
        if len(songlrcname)>0:
            try:
                with open('./music/'+songlrcname[0],'r',encoding='utf-8') as f:
                    s=f.read().split('\n')
            except:
                with open('./music/'+songlrcname[0],'r') as f:
                    s=f.read().split('\n')
        else:
            return None,None

        #定义一个空字典
        song_dict = {}
        #定义一个字典保存歌词信息
        lrc_dict = {}
        #按照换行进行切割

        str_list = s
        #遍历切割后的聂内容
        try:
            for string in str_list:
                #判断是否是歌词信息
                if '' != string:
                    if string[1].isdecimal():
                        #[02:11.55][01:50.60][00:22.63]穿过幽暗的岁月
                        #按照‘】’进行切割
                        lrc_list = string.split(']')
                        #提取歌词信息
                        lrc_info = lrc_list[-1]
                        #提取时间信息
                        time_info = lrc_list[:-1]
                        # print(time_info)
                        #便利处理每一个时间戳
                        for  time_str in time_info:
                            # print(time_str)
                            #[02:16.93
                            #去掉‘【’
                            time_str = time_str[1:]
                            # print(time_str)
                            # 02: 06.33
                            #按照冒号进行切割
                            time_info_list = time_str.split(':')
                            # print(time_info_list)
                            # ['02', '47.70']
                            #提取分钟
                            time_min = float(time_info_list[0])
                            #提取秒数
                            time_sec = float(time_info_list[1])
                            #合并时间
                            time = (time_min*60+time_sec)*1000
                            #保存歌词以及对应的时间戳
                            lrc_dict[time] = lrc_info
                    else:
                        #[ti:蓝莲花]
                        #去掉两边的【】
                        string = string[1:-1]
                        #按照‘：’进行切割
                        song_list = string.split(':')
                        #保存在字典中
                        if song_list[0] == 'ti':
                            song_dict['标题'] = song_list[1]
                        elif song_list[0] == 'ar':
                            song_dict['艺术家'] = song_list[1]
                        elif song_list[0] == 'al':
                            song_dict['专辑'] = song_list[1]
        except:
            for string in str_list:
                #判断是否是歌词信息
                if '' != string:
                    if '[' in string:
                        lrc_list=string.split("]")
                        
                        a=float(lrc_list[0].split("[")[-1])*1000
                        lrc_dict[a]=lrc_list[1]
        #提取所有的时间戳
        time_list = list(lrc_dict)
        #对时间戳进行排序,降序
        time_list.sort(reverse=True)
        return time_list,lrc_dict
    #显示歌词列表
    def get_lrc_by_time(self,time):
        if self.time_list==[]:
            self.ui.label_8.setText("未找到该歌曲的歌词")
            return
        for i,j in enumerate(self.time_list):
            
            if j <= time :
                # print(self.lrc_dict[i])
                try:
                    self.ui.label_11.setText(self.lrc_dict[self.time_list[i-3]])
                    self.ui.label_10.setText(self.lrc_dict[self.time_list[i-2]])
                    self.ui.label_9.setText(self.lrc_dict[self.time_list[i-1]])
                    self.ui.label_8.setText(self.lrc_dict[j])
                    self.ui.label_7.setText(self.lrc_dict[self.time_list[i+1]])
                    self.ui.label_6.setText(self.lrc_dict[self.time_list[i+2]])
                    self.ui.label_5.setText(self.lrc_dict[self.time_list[i+3]])
                except:
                    self.ui.label_8.setText(self.lrc_dict[j])
                break
    # 初始化歌词为空   
    def init_lrc(self):
        self.ui.label_11.setText("")
        self.ui.label_10.setText("")
        self.ui.label_9.setText("")
        self.ui.label_7.setText("")
        self.ui.label_6.setText("")
        self.ui.label_5.setText("")
    # 旋转封面
    def r_fengmian(self):
        self.slotRotate()
    
    def fengmian(self):
        if self.turn_fengmian:
            self.turn_fengmian=False
        else:
            self.turn_fengmian=True
    
    def slotRotate(self):
        if self.turn_fengmian==False:
            return
        # 效果不好,最后使用opencv做的旋转封面
        # image=self.cvimg_to_qtimg(self.img)
        # transform = QTransform()##需要用到pyqt5中QTransform函数
        # transform.rotate(90) ##设置旋转角度——顺时针旋转90°
        # self.image=image.transformed(transform)##对image进行旋转
        # self.ui.pushButton_8.setPixmap(QPixmap(self.image))
        rows, cols = self.img.shape[:2]
        c=cols/2
        r=rows/2
        
        M = cv2.getRotationMatrix2D((c, r),self.rotate , 1)
        #参数：原始图像 旋转参数 元素图像宽高
        rotated = cv2.warpAffine(self.img, M, (cols, rows))
        cv2.imwrite("./music/test.jpg",rotated)
        self.ui.pushButton_8.setStyleSheet("border-radius:80px;\n"
            "border-image: url(./music/test.jpg);\n")
        self.rotate-=5


    def init_cv_circle(self,img):
        image =cv2.imdecode(np.fromfile(img,dtype=np.uint8),-1)
        return image

    #pt格式的pixmap文件转opencv文件
    def qtpixmap_to_cvimg(self,qtpixmap):
        qimg = qtpixmap.toImage()
        temp_shape = (qimg.height(), qimg.bytesPerLine() * 8 // qimg.depth())
        temp_shape += (4,)
        ptr = qimg.bits()
        ptr.setsize(qimg.byteCount())
        result = np.array(ptr, dtype=np.uint8).reshape(temp_shape)
        result = result[..., :3]
        return result

    #窗体拖动
    def mousePressEvent(self, evt):
        if evt.button() == Qt.LeftButton:
            self.switch = True
        else:
            self.switch = False
        self.mouse_x = evt.globalX()
        self.mouse_y = evt.globalY()
        self.window_x = self.x()
        self.window_y = self.y()
    def mouseMoveEvent(self, evt):
        if self.switch:
            move_x = evt.globalX() - self.mouse_x
            move_y = evt.globalY() - self.mouse_y

            vector_x = self.window_x + move_x
            vector_y = self.window_y + move_y
            self.move(vector_x, vector_y)
#下载歌曲封面子线程
class mythread(QThread):  # 步骤1.创建一个线程实例
    mysignal = pyqtSignal(tuple)  # 创建一个自定义信号，元组参数

    def __init__(self, name,url,name1,url1):  #通过初始化赋值的方式实现UI主线程传递值给子线程
        super(mythread, self).__init__()
        self.name = name
        self.url=url
        self.name1=name1
        self.url1=url1
        self.mutex = QMutex()

    def run(self):
        if "http" in self.url:
            self.mutex.lock()
            print(self.url1)
            downloader.download([self.url,self.name,self.url1,self.name1])
            text=self.name.split("music/")[-1].split(".")[0]
            self.mysignal.emit((text,1))
            self.mutex.unlock()
#搜索歌曲子线程
class search_thread(QThread):  
    mysignal = pyqtSignal(tuple)  # 创建一个自定义信号，元组参数

    def __init__(self, name,api):  #通过初始化赋值的方式实现UI主线程传递值给子线程
        super(search_thread, self).__init__()
        self.name = name
        self.api=api
        self.mutex = QMutex()

    def run(self):
        self.mutex.lock()
        try:
            name,singer,id=self.api.search(self.name)
            self.mysignal.emit((name,singer,id))
        except:
            self.mysignal.emit(("搜索失败","无返回结果",""))
        self.mutex.unlock()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    window = Window()

    window.show()
    sys.exit(app.exec_())
