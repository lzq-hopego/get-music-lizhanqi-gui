from PyQt5.Qt import *
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtMultimedia import QMediaPlayer,QMediaPlaylist, QMediaContent
from PyQt5.QtWidgets import QFileDialog
import sys,os
from ui2 import Ui_MainWindow
import re
import cv2
from get_music import *
import numpy as np

class Window(QMainWindow):
    def __init__(self, parent=None, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.switch = False#窗体是否被拖动
        self.mixer=QMediaPlayer()
        self.timer=QTimer()

        self.playlist=QMediaPlaylist()
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
        self.state="stop" #定义播放器当前状态
        self.playlist.setCurrentIndex(self.songnum)
        self.mixer.setPlaylist(self.playlist) #加入歌单
        self.songtitle()#初始化左下角显示歌曲名
        self.init_list()#初始化列表

        self.soupage=False
        self.rotate=0 #记录封面旋转的角度
        
        #封面是否旋转
        self.turn_fengmian=False
        self.init_play_back_mode()# 初始化播放模式
        self.init_volume()# 初始化音量条
        self.init_fengmian()# 初始化歌曲封面
        self.this_songtime(0)#初始化歌词歌曲时长
        self.ui.listWidget_2.setVisible(False)#初始化listwidget2为不显示状态
        # #初始化歌词显示
        self.init_lrc()

        self.ui.horizontalSlider_2.valueChanged.connect(self.setvolume)
        self.ui.horizontalSlider.sliderReleased.connect(self.getvalue)
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
        # self.ui.pushButton.doubleClicked.connect(self.fengmian)
        # self.ui.pushButton_3.clicked.connect(self.dis_one)
        # self.ui.pushButton_7.clicked.connect(self.undis_one)
        # self.ui.widget_4.setVisible(False)
        
        #判断是否在播放时旋转封面，注意由于qt的限制我无法实现圆形封面旋转
        #采用的opencv圆形检测后并保存为test.jpg文件后再显示的，非常消耗内存，默认关闭
        self.timer.timeout.connect(self.r_fengmian)
        
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
       '51翻唱':fivesing.fivesing('fc')}
        self.song_name_list=[]
        self.singer_name_list=[]
        self.song_id_list=[]


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
    def dis_one(self):
        if self.soupage:
            self.ui.label_5.setVisible(True)
            self.ui.label_6.setVisible(True)
            self.ui.label_7.setVisible(True)
            self.ui.label_8.setVisible(True)
            self.ui.label_9.setVisible(True)
            self.ui.label_10.setVisible(True)
            self.ui.label_11.setVisible(True)
            self.ui.pushButton_8.setVisible(True)
            self.ui.listWidget_2.setVisible(False)
            self.soupage=False

    def search(self):
        self.is_api=self.api[self.ui.comboBox.currentText()]
        text=self.ui.lineEdit.text()
        if text=='':
            print("没有输入内容")
            return
        self.ui.listWidget_2.clear()
        try:
            self.song_name_list,self.singer_name_list,self.song_id_list=self.is_api.search(text)
            for i in range(min(len(self.song_name_list),len(self.singer_name_list))):
                name=self.song_name_list[i]+"\t"+self.singer_name_list[i]
                self.ui.listWidget_2.addItem(name)
        except:
            if self.song_name_list=='':
                self.ui.listWidget_2.addItem("搜索结果为空")
            else:
                self.ui.listWidget_2.addItem("接口失效,可以联系管理员进行修复，QQ邮箱：310197835@qq.com")
        self.ui.listWidget_2.setVisible(True)
        self.soupage=True
    def list_download(self):
        num=self.ui.listWidget_2.currentRow()
        songname=self.song_name_list[num]
        singer=self.singer_name_list[num]
        name=songname+"-"+singer
        id=self.song_id_list[num]
        url=self.is_api.get_music_url(id)
        # print(url)
        img_url=self.is_api.get_music_pic(num,return_url=True)
        lrc_url=self.is_api.get_music_lrc(num,return_url=True)
        

        rstr = r"[\/\\\:\*\?\"\<\>\|\&]"  # '/ \ : * ? " < > |'
        name = re.sub(rstr, "_", name)  # 替换为下划线
        try:
            download.download(url,"./music/"+name+".mp3",or_re=False)
            down=True
        except:
            down=False
        try:
            download.download(img_url,"./music/"+name+".jpg",or_re=False)
        except:
            if 'http' in img_url :
                html=requests.get(img_url)
                with open("./music/"+name+".jpg",'wb') as f:
                    f.write(html.content)
            else:
                print("无法下载该歌曲的封面")
        try:
            if "http" in lrc_url:
                download.download(lrc_url,"./music/"+name+".lrc",or_re=False)
            else:
                try:
                    with open("./music/"+name+".txt",'w') as f:
                        f.write(lrc_url)
                except:
                    with open("./music/"+name+".txt",'w',encoding="utf-8") as f:
                        f.write(lrc_url)
        except:
            print("无法下载该歌曲的歌词")
        #有的歌曲可能无法下载其封面，有的无法下载其歌词，有的甚至都不能下载
        if down:
            self.ui.listWidget.addItem(name+".mp3")
            self.playlist.addMedia(QMediaContent(QUrl("./music/{}.mp3".format(name))))
            self.songnamelist.append(name+".mp3")
            self.playlist.setCurrentIndex(len(self.songnamelist)-1)
            if self.state=="stop":
                self.dianji()

    def init_list(self):
        self.ui.listWidget.addItems(self.songnamelist)
    def double_list(self,index):
        # print(self.ui.listWidget.item(self.ui.listWidget.row(index)).text())
        # print(index)
        num=self.ui.listWidget.currentRow()
        self.playlist.setCurrentIndex(num)
        if self.state=="stop":
            self.dianji()
        # self.state="start"

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
    def next(self):
        if self.playlist.nextIndex()==-1:
            name=self.songnamelist[self.playlist.nextIndex()+1]
            self.state="stop"
            self.dianji()
            self.dianji()
            
        print(self.playlist.nextIndex(),self.state)
        self.playlist.next()
        self.this_songtime(0)
        
 
        
    def previous(self):
        if self.playlist.previousIndex()==-1:
            name=self.songnamelist[self.playlist.previousIndex()+1]
            self.state="stop"
            self.dianji()
            self.dianji()
        
        print(self.playlist.previousIndex(),self.state)
        self.playlist.previous()
        self.this_songtime(0)
        

    # 获取当前播放歌曲名
    def songtitle(self):
        name=self.songnamelist[self.playlist.currentIndex()]
        self.ui.label.setText(name.split("-")[0])
        self.ui.label_2.setText(name.split("-")[-1].split(".")[0])
    # 获取歌曲长度
    def init_songtime(self):
        time_long=self.mixer.duration()
        self.ui.horizontalSlider.setRange(0,time_long)
        self.ui.label_4.setText(str(int(time_long / 1000) // 60).zfill(2) + ':' + str(int(time_long / 1000) % 60).zfill(2))
    # 获取当前播放进度
    def this_songtime(self,index):
        # print(index)
        self.init_songtime()
        time_long=self.mixer.position()
        self.ui.horizontalSlider.setValue(time_long)
        self.ui.label_3.setText(str(int(time_long / 1000) // 60).zfill(2) + ':' + str(int(time_long / 1000) % 60).zfill(2))
        #刷新歌词
        if self.show_lrc==True:
            self.get_lrc_by_time(index)
    #滑动滑块调整歌曲进度
    def getvalue(self):
        value=self.ui.horizontalSlider.value()
        self.mixer.setPosition(value)
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
        lt=[QIcon(":/image/image/cycle_one.png"),QIcon(":/image/image/cycle.png"),QIcon(":/image/image/random.png")]
        num=self.playlist.playbackMode()
        if num==3:
            s=2
            print('随机播放')
        elif num==4:
            s=0
            print("列表循环")
        elif num==1:
            s=1
            print("单曲循环")
        self.playlist.setPlaybackMode(ls[s])
        self.ui.pushButton_5.setIcon(lt[s])
    def init_fengmian(self):
        #更新当前播放的歌曲在列表中显示
        if len(self.songnamelist)-1<=self.playlist.previousIndex():
            self.ui.listWidget.setCurrentRow(0)
        else:
            self.ui.listWidget.setCurrentRow(self.playlist.previousIndex()+1)
        #更新标题和歌曲封面
        self.songtitle()
        dirlist=os.listdir('./music')
        ls=[]
        for i in dirlist:
            if self.songnamelist[self.playlist.currentIndex()].split("-")[0] in i:
                if '.jpg' in i:
                    ls.append(i)
        if len(ls)>=1:
            
            self.ui.pushButton.setStyleSheet("border-radius:40px;\n"
"border-image: url(./music/{});\n".format(ls[0]))
            # self.ui.pushButton_8.setStyleSheet("border-radius:80px;\n"
            # "border-image: url(./music/{});\n".format(ls[0]))
            
            self.img=self.init_cv_circle("./music/{}".format(ls[0]))
            
            
            self.ui.pushButton_8.setStyleSheet("border-radius:80px;\n"
"border-image: url(./music/{});\n".format(ls[0]))

        else:
        #     self.ui.pushButton.setIcon(QIcon(":/image/image/5.jpg"))
        #     # self.ui.pushButton_8.setIcon(QIcon(":/image/image/5.jpg"))
            self.ui.pushButton_8.setStyleSheet("border-radius:80px;\n"
                "border-image: url(:/image/image/5.jpg);\n"
            )
            self.ui.pushButton.setStyleSheet("border-radius:40px;\n"
            "border-image: url(:/image/image/5.jpg);\n"
            )
            # img=QPixmap(":/image/image/5.jpg")
            self.img=self.qtpixmap_to_cvimg(QPixmap(":/image/image/5.jpg"))
            # self.img=self.init_cv_circle("./image/5.jpg")
            


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
            
    def init_lrc(self):
        self.ui.label_11.setText("")
        self.ui.label_10.setText("")
        self.ui.label_9.setText("")
        self.ui.label_7.setText("")
        self.ui.label_6.setText("")
        self.ui.label_5.setText("")
        # print(self.lrc_dict[self.time_list[-1]])
        #         return self.lrc_dict[i]
        # return  self.lrc_dict[self.time_list[-1]]
        
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

if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = Window()

    window.show()
    sys.exit(app.exec_())
