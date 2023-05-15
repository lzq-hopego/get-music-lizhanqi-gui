'''
作者: 李展旗
Date: 2023-05-15 08:21:40
文件最后编辑者: 李展旗
LastEditTime: 2023-05-15 18:27:15
'''

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtProperty
import cgitb

cgitb.enable(format='text')  # 解决pyqt5异常只要进入事件循环,程序就崩溃,而没有任何提示


class Rotation(QObject):
    def __init__(self,filename,img_type,QPixmap_type=False):
        super().__init__()
        if not QPixmap_type:
            pixmap=self.mask_image(filename,img_type)
        else:
            try:
                pixmap = QPixmap(filename)
            except:
                 print("封面无法加载!")
        scaledPixmap = pixmap.scaled(160, 160)  # 动画大小
        self.animation()
        self.pixmap_item = QGraphicsPixmapItem(scaledPixmap)
        self.pixmap_item.setTransformOriginPoint(80, 80)  # 设置中心为旋转

    def _set_rotation(self, degree):
        self.pixmap_item.setRotation(degree)  # 自身改变旋转度数

    def animation(self):
        self.anim = QPropertyAnimation(self, b'rotation')  # 动画类型
        self.anim.setDuration(2000)
        self.anim.setStartValue(0)  # 初始角度
        self.anim.setEndValue(360)
        self.anim.setLoopCount(-1)  # 设置循环旋转
    def mask_image(self,imgdata,imgtype, size = 256):
            # imgtype=imgdata.split(".")[-1]
            image = QImage(imgdata, imgtype)
            image.convertToFormat(QImage.Format_ARGB32)
            imgsize = min(image.width(), image.height())
            rect = QRect(
                (image.width() - imgsize) / 2,
                (image.height() - imgsize) / 2,
                imgsize,
                imgsize,
            )
            
            image = image.copy(rect)
            out_img = QImage(imgsize, imgsize, QImage.Format_ARGB32)
            out_img.fill(Qt.transparent)
            brush = QBrush(image)
            painter = QPainter(out_img)
            painter.setBrush(brush)
            painter.setPen(Qt.NoPen)
            painter.drawEllipse(0, 0, imgsize, imgsize)
            painter.end() 
            pr = QWindow().devicePixelRatio()
            pm = QPixmap.fromImage(out_img)
            pm.setDevicePixelRatio(pr)
            size *= pr
            pm = pm.scaled(size, size, Qt.KeepAspectRatio, 
                                    Qt.SmoothTransformation)
            return pm

    rotation = pyqtProperty(int, fset=_set_rotation)  # 属性动画改变自身数值