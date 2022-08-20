# -*- coding: utf-8 -*-
"""
-------------------------------------------------
  File Name：   GUI_connect
  Author :    WangJingyao
  date：     2021/9/25
-------------------------------------------------
  Change Activity:
          2021/9/25:
-------------------------------------------------
"""
__author__ = 'WangJingyao'

import cv2
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QLabel

# import imutils
# import cv2
# import time
# import dlib
#
# from parameters import NETWORK, DATASET, VIDEO_PREDICTOR
# from model import build_model
# from predict import load_model, predict

# from childA_GUI import ChildUi_A
# from childB_GUI import ChildUi_B
# from childC_GUI import ChildUi_C
# from childD_GUI import ChildUi_D


'''------------------------------------------主界面---------------------------------------------------'''


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowTitle('基于多模态情感分析的个性化健康导航研究——王婧瑶')

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("情感分析")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("健康导航")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("联系与帮助")
        self.left_label_3.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.music', color='white'), "情感监测")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.sellsy', color='white'), "心理调查")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.film', color='white'), "情感分析")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.home', color='white'), "健康反馈")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.download', color='white'), "调节指南")
        self.left_button_5.setObjectName('left_button')
        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.heart', color='white'), "生成报告")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "反馈建议")
        self.left_button_7.setObjectName('left_button')
        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "关注我们")
        self.left_button_8.setObjectName('left_button')
        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "遇到问题")
        self.left_button_9.setObjectName('left_button')
        self.left_xxx = QtWidgets.QPushButton(" ")

        # 控件布局
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_2, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 6, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_label_3, 9, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 12, 0, 1, 3)

        self.right_bar_widget = QtWidgets.QWidget()  # 右侧顶部搜索框部件
        self.right_bar_layout = QtWidgets.QGridLayout()  # 右侧顶部搜索框网格布局
        self.right_bar_widget.setLayout(self.right_bar_layout)
        self.search_icon = QtWidgets.QLabel(chr(0xf002) + ' ' + '搜索  ')
        self.search_icon.setFont(qtawesome.font('fa', 16))
        self.right_bar_widget_search_input = QtWidgets.QLineEdit()
        self.right_bar_widget_search_input.setPlaceholderText("输入心理问题、健康困扰或情感困惑，回车进行搜索")

        self.right_bar_layout.addWidget(self.search_icon, 0, 0, 1, 1)
        self.right_bar_layout.addWidget(self.right_bar_widget_search_input, 0, 1, 1, 8)

        self.right_layout.addWidget(self.right_bar_widget, 0, 0, 1, 9)

        self.right_recommend_label = QtWidgets.QLabel("提供服务")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.recommend_button_1 = QtWidgets.QToolButton()
        self.recommend_button_1.setText("情感监测")  # 设置按钮文本
        self.recommend_button_1.setIcon(QtGui.QIcon('./提供服务/情感监测.png'))  # 设置按钮图标
        self.recommend_button_1.setIconSize(QtCore.QSize(100, 100))  # 设置图标大小
        self.recommend_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)  # 设置按钮形式为上图下文
        # self.recommend_button_1.clicked.connect(self.qingganjiance)

        self.recommend_button_2 = QtWidgets.QToolButton()
        self.recommend_button_2.setText("语音问答")
        self.recommend_button_2.setIcon(QtGui.QIcon('./提供服务/语音问答.png'))
        self.recommend_button_2.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.recommend_button_2.clicked.connect(self.yuyinwenda)

        self.recommend_button_3 = QtWidgets.QToolButton()
        self.recommend_button_3.setText("疑问解答")
        self.recommend_button_3.setIcon(QtGui.QIcon('./提供服务/疑问解答.png'))
        self.recommend_button_3.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.recommend_button_3.clicked.connect(self.yiwenjieda)

        self.recommend_button_4 = QtWidgets.QToolButton()
        self.recommend_button_4.setText("联系专家")
        self.recommend_button_4.setIcon(QtGui.QIcon('./提供服务/联系专家.png'))
        self.recommend_button_4.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.recommend_button_4.clicked.connect(self.lianxizhuanjia)

        self.recommend_button_5 = QtWidgets.QToolButton()
        self.recommend_button_5.setText("建议与意见")
        self.recommend_button_5.setIcon(QtGui.QIcon('./提供服务/意见与建议.png'))
        self.recommend_button_5.setIconSize(QtCore.QSize(100, 100))
        self.recommend_button_5.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.recommend_button_5.clicked.connect(self.yijianyujianyi)

        self.right_recommend_layout.addWidget(self.recommend_button_1, 0, 0)
        self.right_recommend_layout.addWidget(self.recommend_button_2, 0, 1)
        self.right_recommend_layout.addWidget(self.recommend_button_3, 0, 2)
        self.right_recommend_layout.addWidget(self.recommend_button_4, 0, 3)
        self.right_recommend_layout.addWidget(self.recommend_button_5, 0, 4)

        self.right_layout.addWidget(self.right_recommend_label, 1, 0, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 2, 0, 2, 9)

        self.right_newsong_lable = QtWidgets.QLabel("健康问答自测（随机选择下列选项）")
        self.right_newsong_lable.setObjectName('right_lable')

        self.right_playlist_lable = QtWidgets.QLabel("常见健康问题")
        self.right_playlist_lable.setObjectName('right_lable')

        self.right_newsong_widget = QtWidgets.QWidget()  # 最新歌曲部件
        self.right_newsong_layout = QtWidgets.QGridLayout()  # 最新歌曲部件网格布局
        self.right_newsong_widget.setLayout(self.right_newsong_layout)

        self.newsong_button_1 = QtWidgets.QPushButton("问答1        抑郁倾向测试               10min   ")
        self.newsong_button_2 = QtWidgets.QPushButton("问答2        狂躁倾向测试               12min   ")
        self.newsong_button_3 = QtWidgets.QPushButton("问答3        人格障碍倾向测试           10min   ")
        self.newsong_button_4 = QtWidgets.QPushButton("问答4        焦虑倾向测试               20min   ")
        self.newsong_button_5 = QtWidgets.QPushButton("问答5        强迫症倾向测试             13min   ")
        # self.newsong_button_6 = QtWidgets.QPushButton("问答6      陈慧娴      永远的朋友      03::29")
        self.right_newsong_layout.addWidget(self.newsong_button_1, 0, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_2, 1, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_3, 2, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_4, 3, 1, )
        self.right_newsong_layout.addWidget(self.newsong_button_5, 4, 1, )
        # self.right_newsong_layout.addWidget(self.newsong_button_6, 5, 1, )

        # 添加心理测试控件
        self.newsong_button_1.clicked.connect(self.test_yiyuzheng)
        self.newsong_button_2.clicked.connect(self.test_kuangzao)
        self.newsong_button_3.clicked.connect(self.test_rengezhangai)
        self.newsong_button_4.clicked.connect(self.test_jiaolv)
        self.newsong_button_5.clicked.connect(self.test_qiangpo)

        self.right_playlist_widget = QtWidgets.QWidget()  # 播放歌单部件
        self.right_playlist_layout = QtWidgets.QGridLayout()  # 播放歌单网格布局
        self.right_playlist_widget.setLayout(self.right_playlist_layout)

        self.playlist_button_1 = QtWidgets.QToolButton()
        self.playlist_button_1.setText("抑郁症")
        self.playlist_button_1.setIcon(QtGui.QIcon('./症状图片/抑郁症.png'))
        self.playlist_button_1.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_1.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.playlist_button_1.clicked.connect(self.yiyuzheng)

        self.playlist_button_2 = QtWidgets.QToolButton()
        self.playlist_button_2.setText("狂躁症")
        self.playlist_button_2.setIcon(QtGui.QIcon('./症状图片/狂躁症.png'))
        self.playlist_button_2.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_2.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.playlist_button_2.clicked.connect(self.kuangzaozheng)

        self.playlist_button_3 = QtWidgets.QToolButton()
        self.playlist_button_3.setText("神经衰弱")
        self.playlist_button_3.setIcon(QtGui.QIcon('./症状图片/神经衰弱.png'))
        self.playlist_button_3.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_3.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.playlist_button_3.clicked.connect(self.shenjingshuairuo)

        self.playlist_button_4 = QtWidgets.QToolButton()
        self.playlist_button_4.setText("焦虑症")
        self.playlist_button_4.setIcon(QtGui.QIcon('./症状图片/焦虑症.png'))
        self.playlist_button_4.setIconSize(QtCore.QSize(100, 100))
        self.playlist_button_4.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.playlist_button_4.clicked.connect(self.jiaolvzheng)

        self.right_playlist_layout.addWidget(self.playlist_button_1, 0, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_2, 0, 1)
        self.right_playlist_layout.addWidget(self.playlist_button_3, 1, 0)
        self.right_playlist_layout.addWidget(self.playlist_button_4, 1, 1)

        self.right_layout.addWidget(self.right_newsong_lable, 4, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_lable, 4, 5, 1, 4)
        self.right_layout.addWidget(self.right_newsong_widget, 5, 0, 1, 5)
        self.right_layout.addWidget(self.right_playlist_widget, 5, 5, 1, 4)

        # 顶部按钮（绿黄红）
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_bar_widget_search_input.setStyleSheet(
            '''QLineEdit{
                    border:1px solid gray;
                    width:300px;
                    border-radius:10px;
                    padding:2px 4px;
            }''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.right_recommend_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')
        self.right_playlist_widget.setStyleSheet(
            '''
                QToolButton{border:none;}
                QToolButton:hover{border-bottom:2px solid #F76677;}
            ''')

        self.right_newsong_widget.setStyleSheet('''
            QPushButton{
                border:none;
                color:gray;
                font-size:12px;
                height:40px;
                padding-left:5px;
                padding-right:10px;
                text-align:left;
            }
            QPushButton:hover{
                color:black;
                border:1px solid #F3F3F5;
                border-radius:10px;
                background:LightGray;
            }
        ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        #
        self.main_layout.setSpacing(0)

    # “常见心理疾病” 部分跳转界面
    windowList = []

    def yiyuzheng(self):
        # self.app = QtWidgets.QApplication(sys.argv)
        # self.gui = ChildUi_A()
        # self.windowList.append(self.gui)
        # self.gui.show()
        # sys.exit(self.app.exec_())
        the_window = ChildUi_A()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # self.close()
        the_window.show()

    def kuangzaozheng(self):
        the_window = ChildUi_B()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # self.close()
        the_window.show()

    def shenjingshuairuo(self):
        the_window = ChildUi_C()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # self.close()
        the_window.show()

    def jiaolvzheng(self):
        the_window = ChildUi_D()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # self.close()
        the_window.show()

    # “心理测试” 部分跳转界面
    def test_yiyuzheng(self):
        the_window = ChildUi_E()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # self.close()
        the_window.show()

    def test_kuangzao(self):
        the_window = ChildUi_F()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # self.close()
        the_window.show()

    def test_rengezhangai(self):
        the_window = ChildUi_G()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # self.close()
        the_window.show()

    def test_jiaolv(self):
        the_window = ChildUi_H()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # self.close()
        the_window.show()

    def test_qiangpo(self):
        the_window = ChildUi_I()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # self.close()
        the_window.show()



    #提供服务跳转界面
    #不是很懂为什么还没有按下Button，这个函数就已经开始运行
    # def qingganjiance(self):
        # the_window = EmotionRecognizer()
        # self.r = EmotionRecognizer()
        # self.r.recognize_emotions()
        # print("---------------情感监测结束---------------")
        # self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # self.close()
        # the_window.show()


    def yuyinwenda(self):
        the_window = ChildUi_K()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # self.close()
        the_window.show()

    def yiwenjieda(self):
        the_window = ChildUi_L()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # self.close()
        the_window.show()

    def lianxizhuanjia(self):
        the_window = ChildUi_M()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # self.close()
        the_window.show()

    def yijianyujianyi(self):
        the_window = ChildUi_N()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # self.close()
        the_window.show()

########################################常见心理疾病模块#############################################


'''-------------------------------------副界面：抑郁症---------------------------------------------------'''
class ChildUi_A(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowTitle('抑郁症')

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("抑郁症")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("治疗方法")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("操作")
        self.left_label_3.setObjectName('left_label')

        # self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "返回")
        # self.left_button_1.setObjectName('left_button')
        # self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "跳转到")
        # self.left_button_2.setObjectName('left_button')
        # self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "进入测试")
        # self.left_button_3.setObjectName('left_button')

        self.left_xxx = QtWidgets.QPushButton(" ")

        # 控件布局
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_2, 6, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_3, 10, 0, 1, 3)

        # 主界面
        # 标题
        self.right_recommend_label = QtWidgets.QLabel("抑郁症")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.right_layout.addWidget(self.right_recommend_label, 0, 1, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 3, 0, 6, 9)

        # 文本内容
        # 在窗口w中，新建另一个label，名字叫做l2
        # 在窗口w中，新建一个lable，名字叫做l1
        pix = QPixmap('./文本图片/resize/1.png')

        lb1 = QLabel(self)
        lb1.setGeometry(200, 60, 800, 600)
        lb1.setPixmap(pix)

        # 顶部按钮（绿黄红）
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        #
        self.main_layout.setSpacing(0)

    # 回到第一个界面
    windowList = []

    def close_event(self, event):
        the_window = MainUi()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # the_window.show()
        event.accept()


'''-------------------------------------副界面：狂躁症---------------------------------------------------'''
class ChildUi_B(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowTitle('狂躁症')

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("狂躁症")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("治疗方法")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("操作")
        self.left_label_3.setObjectName('left_label')

        # self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "返回")
        # self.left_button_1.setObjectName('left_button')
        # self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "跳转到")
        # self.left_button_2.setObjectName('left_button')
        # self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "进入测试")
        # self.left_button_3.setObjectName('left_button')

        self.left_xxx = QtWidgets.QPushButton(" ")

        # 控件布局
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_2, 6, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_3, 10, 0, 1, 3)

        # 主界面
        # 标题
        self.right_recommend_label = QtWidgets.QLabel("狂躁症")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.right_layout.addWidget(self.right_recommend_label, 0, 1, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 3, 0, 6, 9)

        # 文本内容
        # 在窗口w中，新建另一个label，名字叫做l2
        # 在窗口w中，新建一个lable，名字叫做l1
        pix = QPixmap('./文本图片/resize/2.png')

        lb1 = QLabel(self)
        lb1.setGeometry(200, 0, 800, 600)
        lb1.setPixmap(pix)

        # 顶部按钮（绿黄红）
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        #
        self.main_layout.setSpacing(0)

    # 回到第一个界面
    windowList = []

    def close_event(self, event):
        the_window = MainUi()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # the_window.show()
        event.accept()


'''-------------------------------------副界面：神经衰弱---------------------------------------------------'''
class ChildUi_C(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowTitle('神经衰弱')

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("神经衰弱")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("治疗方法")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("操作")
        self.left_label_3.setObjectName('left_label')

        # self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "返回")
        # self.left_button_1.setObjectName('left_button')
        # self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "跳转到")
        # self.left_button_2.setObjectName('left_button')
        # self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "进入测试")
        # self.left_button_3.setObjectName('left_button')

        self.left_xxx = QtWidgets.QPushButton(" ")

        # 控件布局
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_2, 6, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_3, 10, 0, 1, 3)

        # 主界面
        # 标题
        self.right_recommend_label = QtWidgets.QLabel("神经衰弱")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.right_layout.addWidget(self.right_recommend_label, 0, 1, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 3, 0, 6, 9)

        # 文本内容
        # 在窗口w中，新建另一个label，名字叫做l2
        # 在窗口w中，新建一个lable，名字叫做l1
        pix = QPixmap('./文本图片/resize/3.png')

        lb1 = QLabel(self)
        lb1.setGeometry(200, 60, 800, 600)
        lb1.setPixmap(pix)

        # 顶部按钮（绿黄红）
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        #
        self.main_layout.setSpacing(0)

    # 回到第一个界面
    windowList = []

    def close_event(self, event):
        the_window = MainUi()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # the_window.show()
        event.accept()


'''-------------------------------------副界面：焦虑症---------------------------------------------------'''
class ChildUi_D(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowTitle('焦虑症')

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("焦虑症")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("治疗方法")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("操作")
        self.left_label_3.setObjectName('left_label')

        # self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "返回")
        # self.left_button_1.setObjectName('left_button')
        # self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "跳转到")
        # self.left_button_2.setObjectName('left_button')
        # self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "进入测试")
        # self.left_button_3.setObjectName('left_button')

        self.left_xxx = QtWidgets.QPushButton(" ")

        # 控件布局
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_2, 6, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_3, 10, 0, 1, 3)

        # 主界面
        # 标题
        self.right_recommend_label = QtWidgets.QLabel("焦虑症")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.right_layout.addWidget(self.right_recommend_label, 0, 1, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 3, 0, 6, 9)

        # 文本内容
        # 在窗口w中，新建另一个label，名字叫做l2
        # 在窗口w中，新建一个lable，名字叫做l1
        pix = QPixmap('./文本图片/resize/4.png')

        lb1 = QLabel(self)
        lb1.setGeometry(200, 60, 800, 600)
        lb1.setPixmap(pix)

        # 顶部按钮（绿黄红）
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        #
        self.main_layout.setSpacing(0)

    # 回到第一个界面
    windowList = []

    def close_event(self, event):
        the_window = MainUi()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # the_window.show()
        event.accept()


##########################################心理测试###################################################

'''-------------------------------------心理测试：抑郁---------------------------------------------------'''
class ChildUi_E(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowTitle('抑郁倾向测试')

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮
        #
        self.left_label_1 = QtWidgets.QPushButton("抑郁倾向测试")
        self.left_label_1.setObjectName('left_label')

        self.left_xxx = QtWidgets.QPushButton(" ")

        # 控件布局
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)

        # 主界面
        # 标题
        self.right_recommend_label = QtWidgets.QLabel("抑郁倾向测试")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.right_layout.addWidget(self.right_recommend_label, 0, 1, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 3, 0, 6, 9)

        # 文本内容
        # 在窗口w中，新建另一个label，名字叫做l2
        # 在窗口w中，新建一个lable，名字叫做l1
        pix = QPixmap('./文本图片/test/resize/1.png')

        lb1 = QLabel(self)
        lb1.setGeometry(200, 0, 800, 600)
        lb1.setPixmap(pix)

        # 顶部按钮（绿黄红）
        self.left_close.setFixedSize(15, 15)  # 设置关闭+按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        #
        self.main_layout.setSpacing(0)

    # 回到第一个界面
    windowList = []

    def close_event(self, event):
        the_window = MainUi()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # the_window.show()
        event.accept()

'''-------------------------------------心理测试：狂躁---------------------------------------------------'''
class ChildUi_F(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowTitle('狂躁倾向测试')

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("狂躁倾向测试")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("治疗方法")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("操作")
        self.left_label_3.setObjectName('left_label')

        # self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "返回")
        # self.left_button_1.setObjectName('left_button')
        # self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "跳转到")
        # self.left_button_2.setObjectName('left_button')
        # self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "进入测试")
        # self.left_button_3.setObjectName('left_button')

        self.left_xxx = QtWidgets.QPushButton(" ")

        # 控件布局
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_2, 6, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_3, 10, 0, 1, 3)

        # 主界面
        # 标题
        self.right_recommend_label = QtWidgets.QLabel("狂躁倾向测试")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.right_layout.addWidget(self.right_recommend_label, 0, 1, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 3, 0, 6, 9)

        # 文本内容
        # 在窗口w中，新建另一个label，名字叫做l2
        # 在窗口w中，新建一个lable，名字叫做l1
        pix = QPixmap('./文本图片/test/resize/2.png')

        lb1 = QLabel(self)
        lb1.setGeometry(200, 60, 800, 600)
        lb1.setPixmap(pix)

        # 顶部按钮（绿黄红）
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        #
        self.main_layout.setSpacing(0)

    # 回到第一个界面
    windowList = []

    def close_event(self, event):
        the_window = MainUi()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # the_window.show()
        event.accept()

'''-------------------------------------心理测试：人格障碍---------------------------------------------------'''
class ChildUi_G(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowTitle('人格障碍倾向测试')

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("人格障碍倾向测试")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("治疗方法")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("操作")
        self.left_label_3.setObjectName('left_label')

        # self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "返回")
        # self.left_button_1.setObjectName('left_button')
        # self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "跳转到")
        # self.left_button_2.setObjectName('left_button')
        # self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "进入测试")
        # self.left_button_3.setObjectName('left_button')

        self.left_xxx = QtWidgets.QPushButton(" ")

        # 控件布局
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_2, 6, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_3, 10, 0, 1, 3)

        # 主界面
        # 标题
        self.right_recommend_label = QtWidgets.QLabel("人格障碍倾向测试")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.right_layout.addWidget(self.right_recommend_label, 0, 1, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 3, 0, 6, 9)

        # 文本内容
        # 在窗口w中，新建另一个label，名字叫做l2
        # 在窗口w中，新建一个lable，名字叫做l1
        pix = QPixmap('./文本图片/test/resize/3.png')

        lb1 = QLabel(self)
        lb1.setGeometry(200, 60, 800, 600)
        lb1.setPixmap(pix)

        # 顶部按钮（绿黄红）
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        #
        self.main_layout.setSpacing(0)

    # 回到第一个界面
    windowList = []

    def close_event(self, event):
        the_window = MainUi()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # the_window.show()
        event.accept()

'''-------------------------------------心理测试：焦虑倾向---------------------------------------------------'''
class ChildUi_H(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowTitle('焦虑倾向测试')

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("焦虑倾向测试")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("治疗方法")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("操作")
        self.left_label_3.setObjectName('left_label')

        # self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "返回")
        # self.left_button_1.setObjectName('left_button')
        # self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "跳转到")
        # self.left_button_2.setObjectName('left_button')
        # self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "进入测试")
        # self.left_button_3.setObjectName('left_button')

        self.left_xxx = QtWidgets.QPushButton(" ")

        # 控件布局
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_2, 6, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_3, 10, 0, 1, 3)

        # 主界面
        # 标题
        self.right_recommend_label = QtWidgets.QLabel("焦虑倾向测试")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.right_layout.addWidget(self.right_recommend_label, 0, 1, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 3, 0, 6, 9)

        # 文本内容
        # 在窗口w中，新建另一个label，名字叫做l2
        # 在窗口w中，新建一个lable，名字叫做l1
        pix = QPixmap('./文本图片/test/resize/4.png')

        lb1 = QLabel(self)
        lb1.setGeometry(200, 60, 800, 600)
        lb1.setPixmap(pix)

        # 顶部按钮（绿黄红）
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        #
        self.main_layout.setSpacing(0)

    # 回到第一个界面
    windowList = []

    def close_event(self, event):
        the_window = MainUi()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # the_window.show()
        event.accept()

'''-------------------------------------心理测试：强迫症---------------------------------------------------'''
class ChildUi_I(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowTitle('强迫倾向测试')

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("强迫倾向测试")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("治疗方法")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("操作")
        self.left_label_3.setObjectName('left_label')

        # self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "返回")
        # self.left_button_1.setObjectName('left_button')
        # self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "跳转到")
        # self.left_button_2.setObjectName('left_button')
        # self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "进入测试")
        # self.left_button_3.setObjectName('left_button')

        self.left_xxx = QtWidgets.QPushButton(" ")

        # 控件布局
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_2, 6, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_3, 10, 0, 1, 3)

        # 主界面
        # 标题
        self.right_recommend_label = QtWidgets.QLabel("强迫倾向测试")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.right_layout.addWidget(self.right_recommend_label, 0, 1, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 3, 0, 6, 9)

        # 文本内容
        # 在窗口w中，新建另一个label，名字叫做l2
        # 在窗口w中，新建一个lable，名字叫做l1
        pix = QPixmap('./文本图片/test/resize/5.png')

        lb1 = QLabel(self)
        lb1.setGeometry(190, 80, 800, 600)
        lb1.setPixmap(pix)

        # 顶部按钮（绿黄红）
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        #
        self.main_layout.setSpacing(0)

    # 回到第一个界面
    windowList = []

    def close_event(self, event):
        the_window = MainUi()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # the_window.show()
        event.accept()


##########################################提供服务###################################################

'''-------------------------------------情感监测---------------------------------------------------'''
# class EmotionRecognizer(QtWidgets.QMainWindow):
#     BOX_COLOR = (0, 255, 0)
#     TEXT_COLOR = (0, 255, 0)
#     print("---------------情感监测开始---------------")
#     def __init__(self):
#
#         # initializebevideo stream
#         self.video_stream = cv2.VideoCapture(VIDEO_PREDICTOR.camera_source)
#
#         self.face_detector = cv2.CascadeClassifier(VIDEO_PREDICTOR.face_detection_classifier)
#
#         self.shape_predictor = None
#         if NETWORK.use_landmarks:
#             self.shape_predictor = dlib.shape_predictor(DATASET.shape_predictor_path)
#
#         self.model = load_model()
#         self.last_predicted_time = 0
#         self.last_predicted_confidence = 0
#         self.last_predicted_emotion = ""
#
#     print("---------------开始预测---------------")
#     def predict_emotion(self, image):
#         image.resize([NETWORK.input_size, NETWORK.input_size], refcheck=False)
#         emotion, confidence = predict(image, self.model, self.shape_predictor)
#         return emotion, confidence
#
#     print("---------------辨别情感---------------")
#     def recognize_emotions(self):
#         failedFramesCount = 0
#         detected_faces = []
#         time_last_sent = 0
#         while True:
#             grabbed, frame = self.video_stream.read()
#
#             if grabbed:
#                 # detection phase
#                 frame = imutils.resize(frame, width=600)
#                 gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#
#                 # detect faces
#                 faces = self.face_detector.detectMultiScale(gray, 1.3, 5)
#                 for (x, y, w, h) in faces:
#                     if w < 30 and h < 30:  # skip the small faces (probably false detections)
#                         continue
#
#                     # bounding box
#                     cv2.rectangle(frame, (x, y), (x + w, y + h), self.BOX_COLOR, 2)
#
#                     # try to recognize emotion
#                     face = gray[y:y + h, x:x + w].copy()
#                     if time.time() - self.last_predicted_time < VIDEO_PREDICTOR.time_to_wait_between_predictions:
#                         label = self.last_predicted_emotion
#                         confidence = self.last_predicted_confidence
#                     else:
#                         label, confidence = self.predict_emotion(face)
#                         self.last_predicted_emotion = label
#                         self.last_predicted_confidence = confidence
#                         self.last_predicted_time = time.time()
#
#                     # display and send message by socket
#                     if VIDEO_PREDICTOR.show_confidence:
#                         text = "{0} ({1:.1f}%)".format(label, confidence * 100)
#                     else:
#                         text = label
#                     if label is not None:
#                         cv2.putText(frame, text, (x - 20, y - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.7, self.TEXT_COLOR, 2)
#
#                 # display images
#                 cv2.imshow("Facial Expression Recognition", frame)
#
#                 key = cv2.waitKey(1) & 0xFF
#                 if key == ord("q"):
#                     break
#             else:
#                 failedFramesCount += 1
#                 if failedFramesCount > 10:
#                     print("can't grab frames")
#                     break
#         print("---------------情感监测即将结束---------------")
#         self.video_stream.release()
#         cv2.destroyAllWindows()

'''-------------------------------------语音问答---------------------------------------------------'''
class ChildUi_K(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowTitle('强迫倾向测试')

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("强迫倾向测试")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("治疗方法")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("操作")
        self.left_label_3.setObjectName('left_label')

        # self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "返回")
        # self.left_button_1.setObjectName('left_button')
        # self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "跳转到")
        # self.left_button_2.setObjectName('left_button')
        # self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "进入测试")
        # self.left_button_3.setObjectName('left_button')

        self.left_xxx = QtWidgets.QPushButton(" ")

        # 控件布局
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_2, 6, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_3, 10, 0, 1, 3)

        # 主界面
        # 标题
        self.right_recommend_label = QtWidgets.QLabel("强迫倾向测试")
        self.right_recommend_label.setObjectName('right_lable')

        self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        self.right_recommend_widget.setLayout(self.right_recommend_layout)

        self.right_layout.addWidget(self.right_recommend_label, 0, 1, 1, 9)
        self.right_layout.addWidget(self.right_recommend_widget, 3, 0, 6, 9)

        # 文本内容
        # 在窗口w中，新建另一个label，名字叫做l2
        # 在窗口w中，新建一个lable，名字叫做l1
        pix = QPixmap('./文本图片/test/resize/5.png')

        lb1 = QLabel(self)
        lb1.setGeometry(190, 80, 800, 600)
        lb1.setPixmap(pix)

        # 顶部按钮（绿黄红）
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        #
        self.main_layout.setSpacing(0)

    # 回到第一个界面
    windowList = []

    def close_event(self, event):
        the_window = MainUi()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # the_window.show()
        event.accept()

'''-------------------------------------疑问解答---------------------------------------------------'''
class ChildUi_L(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowTitle('疑问解答')

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("疑问解答")
        self.left_label_1.setObjectName('left_label')

        self.left_xxx = QtWidgets.QPushButton(" ")

        # 控件布局
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_2, 6, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_3, 10, 0, 1, 3)

        # 主界面
        # 标题
        # self.right_recommend_label = QtWidgets.QLabel("疑问解答")
        # self.right_recommend_label.setObjectName('right_lable')
        #
        # self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        # self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        # self.right_recommend_widget.setLayout(self.right_recommend_layout)
        #
        # self.right_layout.addWidget(self.right_recommend_label, 0, 1, 1, 9)
        # self.right_layout.addWidget(self.right_recommend_widget, 3, 0, 6, 9)

        # 文本内容
        # 在窗口w中，新建另一个label，名字叫做l2
        # 在窗口w中，新建一个lable，名字叫做l1
        pix = QPixmap('./文本图片/提供服务/3.png')

        lb1 = QLabel(self)
        lb1.setGeometry(210, 0, 800, 600)
        lb1.setPixmap(pix)

        # 顶部按钮（绿黄红）
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        #
        self.main_layout.setSpacing(0)

    # 回到第一个界面
    windowList = []

    def close_event(self, event):
        the_window = MainUi()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # the_window.show()
        event.accept()

'''-------------------------------------联系专家---------------------------------------------------'''
class ChildUi_M(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowTitle('联系专家')

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("联系专家")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("治疗方法")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("操作")
        self.left_label_3.setObjectName('left_label')

        # self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.comment', color='white'), "返回")
        # self.left_button_1.setObjectName('left_button')
        # self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.star', color='white'), "跳转到")
        # self.left_button_2.setObjectName('left_button')
        # self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.question', color='white'), "进入测试")
        # self.left_button_3.setObjectName('left_button')

        self.left_xxx = QtWidgets.QPushButton(" ")

        # 控件布局
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_2, 6, 0, 1, 3)
        # self.left_layout.addWidget(self.left_button_3, 10, 0, 1, 3)

        # 主界面
        # 标题
        # self.right_recommend_label = QtWidgets.QLabel("联系专家")
        # self.right_recommend_label.setObjectName('right_lable')
        #
        # self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        # self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        # self.right_recommend_widget.setLayout(self.right_recommend_layout)
        #
        # self.right_layout.addWidget(self.right_recommend_label, 0, 1, 1, 9)
        # self.right_layout.addWidget(self.right_recommend_widget, 3, 0, 6, 9)

        # 文本内容
        # 在窗口w中，新建另一个label，名字叫做l2
        # 在窗口w中，新建一个lable，名字叫做l1
        pix = QPixmap('./文本图片/提供服务/4.png')

        lb1 = QLabel(self)
        lb1.setGeometry(210, 0, 800, 600)
        lb1.setPixmap(pix)

        # 顶部按钮（绿黄红）
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        #
        self.main_layout.setSpacing(0)

    # 回到第一个界面
    windowList = []

    def close_event(self, event):
        the_window = MainUi()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # the_window.show()
        event.accept()

'''-------------------------------------建议与意见---------------------------------------------------'''
class ChildUi_N(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(960, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局
        self.setWindowTitle('建议与意见')

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("建议与意见")
        self.left_label_1.setObjectName('left_label')

        self.left_xxx = QtWidgets.QPushButton(" ")

        # 控件布局
        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)
        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)

        # 主界面
        # 标题
        # self.right_recommend_label = QtWidgets.QLabel("建议与意见")
        # self.right_recommend_label.setObjectName('right_lable')
        #
        # self.right_recommend_widget = QtWidgets.QWidget()  # 推荐封面部件
        # self.right_recommend_layout = QtWidgets.QGridLayout()  # 推荐封面网格布局
        # self.right_recommend_widget.setLayout(self.right_recommend_layout)
        #
        # self.right_layout.addWidget(self.right_recommend_label, 0, 1, 1, 9)
        # self.right_layout.addWidget(self.right_recommend_widget, 3, 0, 6, 9)

        # 文本
        pix = QPixmap('./文本图片/提供服务/5.png')

        lb1 = QLabel(self)
        lb1.setGeometry(190, 20, 800, 600)
        lb1.setPixmap(pix)

        # 顶部按钮（绿黄红）
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        self.left_widget.setStyleSheet('''
            QPushButton{border:none;color:white;}
            QPushButton#left_label{
                border:none;
                border-bottom:1px solid white;
                font-size:18px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
            QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
        ''')

        self.right_widget.setStyleSheet('''
            QWidget#right_widget{
                color:#232C51;
                background:white;
                border-top:1px solid darkGray;
                border-bottom:1px solid darkGray;
                border-right:1px solid darkGray;
                border-top-right-radius:10px;
                border-bottom-right-radius:10px;
            }
            QLabel#right_lable{
                border:none;
                font-size:16px;
                font-weight:700;
                font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            }
        ''')

        self.setWindowOpacity(0.9)  # 设置窗口透明度
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明

        self.main_layout.setSpacing(0)

    # 回到第一个界面
    windowList = []

    def close_event(self, event):
        the_window = MainUi()
        self.windowList.append(the_window)  ##注：没有这句，是不打开另一个主界面的！
        # the_window.show()
        event.accept()


def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
