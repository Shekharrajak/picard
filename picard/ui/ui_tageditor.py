# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui/tageditor.ui'
#
# Created: Sat Mar  3 19:09:31 2007
#      by: PyQt4 UI code generator 4.1
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt4 import QtCore, QtGui

class Ui_TagEditorDialog(object):
    def setupUi(self, TagEditorDialog):
        TagEditorDialog.setObjectName("TagEditorDialog")
        TagEditorDialog.resize(QtCore.QSize(QtCore.QRect(0,0,455,355).size()).expandedTo(TagEditorDialog.minimumSizeHint()))

        self.vboxlayout = QtGui.QVBoxLayout(TagEditorDialog)
        self.vboxlayout.setMargin(9)
        self.vboxlayout.setSpacing(6)
        self.vboxlayout.setObjectName("vboxlayout")

        self.tabWidget = QtGui.QTabWidget(TagEditorDialog)
        self.tabWidget.setObjectName("tabWidget")

        self.tab = QtGui.QWidget()
        self.tab.setObjectName("tab")

        self.gridlayout = QtGui.QGridLayout(self.tab)
        self.gridlayout.setMargin(9)
        self.gridlayout.setSpacing(2)
        self.gridlayout.setObjectName("gridlayout")

        spacerItem = QtGui.QSpacerItem(20,40,QtGui.QSizePolicy.Minimum,QtGui.QSizePolicy.Expanding)
        self.gridlayout.addItem(spacerItem,7,0,1,2)

        self.label_7 = QtGui.QLabel(self.tab)
        self.label_7.setObjectName("label_7")
        self.gridlayout.addWidget(self.label_7,5,0,1,1)

        self.label_4 = QtGui.QLabel(self.tab)
        self.label_4.setObjectName("label_4")
        self.gridlayout.addWidget(self.label_4,4,0,1,1)

        self.albumartist = QtGui.QLineEdit(self.tab)
        self.albumartist.setObjectName("albumartist")
        self.gridlayout.addWidget(self.albumartist,3,1,1,1)

        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setObjectName("label_2")
        self.gridlayout.addWidget(self.label_2,3,0,1,1)

        self.label_3 = QtGui.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridlayout.addWidget(self.label_3,1,0,1,1)

        self.title = QtGui.QLineEdit(self.tab)
        self.title.setObjectName("title")
        self.gridlayout.addWidget(self.title,0,1,1,1)

        self.artist = QtGui.QLineEdit(self.tab)
        self.artist.setObjectName("artist")
        self.gridlayout.addWidget(self.artist,1,1,1,1)

        self.album = QtGui.QLineEdit(self.tab)
        self.album.setObjectName("album")
        self.gridlayout.addWidget(self.album,2,1,1,1)

        self.hboxlayout = QtGui.QHBoxLayout()
        self.hboxlayout.setMargin(0)
        self.hboxlayout.setSpacing(2)
        self.hboxlayout.setObjectName("hboxlayout")

        self.tracknumber = QtGui.QLineEdit(self.tab)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tracknumber.sizePolicy().hasHeightForWidth())
        self.tracknumber.setSizePolicy(sizePolicy)
        self.tracknumber.setMaximumSize(QtCore.QSize(40,16777215))
        self.tracknumber.setObjectName("tracknumber")
        self.hboxlayout.addWidget(self.tracknumber)

        self.label_5 = QtGui.QLabel(self.tab)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.hboxlayout.addWidget(self.label_5)

        self.totaltracks = QtGui.QLineEdit(self.tab)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totaltracks.sizePolicy().hasHeightForWidth())
        self.totaltracks.setSizePolicy(sizePolicy)
        self.totaltracks.setMaximumSize(QtCore.QSize(40,16777215))
        self.totaltracks.setObjectName("totaltracks")
        self.hboxlayout.addWidget(self.totaltracks)

        spacerItem1 = QtGui.QSpacerItem(241,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout.addItem(spacerItem1)
        self.gridlayout.addLayout(self.hboxlayout,4,1,1,1)

        self.hboxlayout1 = QtGui.QHBoxLayout()
        self.hboxlayout1.setMargin(0)
        self.hboxlayout1.setSpacing(2)
        self.hboxlayout1.setObjectName("hboxlayout1")

        self.discnumber = QtGui.QLineEdit(self.tab)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.discnumber.sizePolicy().hasHeightForWidth())
        self.discnumber.setSizePolicy(sizePolicy)
        self.discnumber.setMaximumSize(QtCore.QSize(40,16777215))
        self.discnumber.setBaseSize(QtCore.QSize(50,0))
        self.discnumber.setObjectName("discnumber")
        self.hboxlayout1.addWidget(self.discnumber)

        self.label_6 = QtGui.QLabel(self.tab)
        self.label_6.setObjectName("label_6")
        self.hboxlayout1.addWidget(self.label_6)

        self.totaldiscs = QtGui.QLineEdit(self.tab)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.totaldiscs.sizePolicy().hasHeightForWidth())
        self.totaldiscs.setSizePolicy(sizePolicy)
        self.totaldiscs.setMaximumSize(QtCore.QSize(40,16777215))
        self.totaldiscs.setBaseSize(QtCore.QSize(50,0))
        self.totaldiscs.setObjectName("totaldiscs")
        self.hboxlayout1.addWidget(self.totaldiscs)

        spacerItem2 = QtGui.QSpacerItem(241,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout1.addItem(spacerItem2)
        self.gridlayout.addLayout(self.hboxlayout1,5,1,1,1)

        self.hboxlayout2 = QtGui.QHBoxLayout()
        self.hboxlayout2.setMargin(0)
        self.hboxlayout2.setSpacing(2)
        self.hboxlayout2.setObjectName("hboxlayout2")

        self.date = QtGui.QLineEdit(self.tab)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Policy(1),QtGui.QSizePolicy.Policy(0))
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.date.sizePolicy().hasHeightForWidth())
        self.date.setSizePolicy(sizePolicy)
        self.date.setMaximumSize(QtCore.QSize(80,16777215))
        self.date.setObjectName("date")
        self.hboxlayout2.addWidget(self.date)

        spacerItem3 = QtGui.QSpacerItem(61,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout2.addItem(spacerItem3)
        self.gridlayout.addLayout(self.hboxlayout2,6,1,1,1)

        self.label_9 = QtGui.QLabel(self.tab)
        self.label_9.setObjectName("label_9")
        self.gridlayout.addWidget(self.label_9,2,0,1,1)

        self.label_8 = QtGui.QLabel(self.tab)
        self.label_8.setObjectName("label_8")
        self.gridlayout.addWidget(self.label_8,6,0,1,1)

        self.label = QtGui.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridlayout.addWidget(self.label,0,0,1,1)
        self.tabWidget.addTab(self.tab,"")

        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName("tab_4")

        self.vboxlayout1 = QtGui.QVBoxLayout(self.tab_4)
        self.vboxlayout1.setMargin(9)
        self.vboxlayout1.setSpacing(6)
        self.vboxlayout1.setObjectName("vboxlayout1")

        self.tags = QtGui.QTreeWidget(self.tab_4)
        self.tags.setRootIsDecorated(False)
        self.tags.setObjectName("tags")
        self.vboxlayout1.addWidget(self.tags)

        self.hboxlayout3 = QtGui.QHBoxLayout()
        self.hboxlayout3.setMargin(0)
        self.hboxlayout3.setSpacing(6)
        self.hboxlayout3.setObjectName("hboxlayout3")

        self.tags_add = QtGui.QPushButton(self.tab_4)
        self.tags_add.setObjectName("tags_add")
        self.hboxlayout3.addWidget(self.tags_add)

        self.tags_delete = QtGui.QPushButton(self.tab_4)
        self.tags_delete.setObjectName("tags_delete")
        self.hboxlayout3.addWidget(self.tags_delete)

        spacerItem4 = QtGui.QSpacerItem(151,20,QtGui.QSizePolicy.Expanding,QtGui.QSizePolicy.Minimum)
        self.hboxlayout3.addItem(spacerItem4)
        self.vboxlayout1.addLayout(self.hboxlayout3)
        self.tabWidget.addTab(self.tab_4,"")

        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName("tab_2")

        self.vboxlayout2 = QtGui.QVBoxLayout(self.tab_2)
        self.vboxlayout2.setMargin(9)
        self.vboxlayout2.setSpacing(6)
        self.vboxlayout2.setObjectName("vboxlayout2")

        self.artwork_list = QtGui.QListWidget(self.tab_2)
        self.artwork_list.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.artwork_list.setIconSize(QtCore.QSize(170,170))
        self.artwork_list.setMovement(QtGui.QListView.Static)
        self.artwork_list.setFlow(QtGui.QListView.LeftToRight)
        self.artwork_list.setWrapping(False)
        self.artwork_list.setResizeMode(QtGui.QListView.Fixed)
        self.artwork_list.setSpacing(10)
        self.artwork_list.setViewMode(QtGui.QListView.IconMode)
        self.artwork_list.setObjectName("artwork_list")
        self.vboxlayout2.addWidget(self.artwork_list)
        self.tabWidget.addTab(self.tab_2,"")

        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName("tab_5")

        self.vboxlayout3 = QtGui.QVBoxLayout(self.tab_5)
        self.vboxlayout3.setMargin(9)
        self.vboxlayout3.setSpacing(6)
        self.vboxlayout3.setObjectName("vboxlayout3")

        self.info = QtGui.QLabel(self.tab_5)
        self.info.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.info.setWordWrap(True)
        self.info.setObjectName("info")
        self.vboxlayout3.addWidget(self.info)
        self.tabWidget.addTab(self.tab_5,"")
        self.vboxlayout.addWidget(self.tabWidget)

        self.buttonbox = QtGui.QDialogButtonBox(TagEditorDialog)
        self.buttonbox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonbox.setObjectName("buttonbox")
        self.vboxlayout.addWidget(self.buttonbox)

        self.retranslateUi(TagEditorDialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(TagEditorDialog)
        TagEditorDialog.setTabOrder(self.title,self.artist)
        TagEditorDialog.setTabOrder(self.artist,self.album)
        TagEditorDialog.setTabOrder(self.album,self.albumartist)
        TagEditorDialog.setTabOrder(self.albumartist,self.tracknumber)
        TagEditorDialog.setTabOrder(self.tracknumber,self.totaltracks)
        TagEditorDialog.setTabOrder(self.totaltracks,self.discnumber)
        TagEditorDialog.setTabOrder(self.discnumber,self.totaldiscs)
        TagEditorDialog.setTabOrder(self.totaldiscs,self.date)
        TagEditorDialog.setTabOrder(self.date,self.tags)
        TagEditorDialog.setTabOrder(self.tags,self.tags_add)
        TagEditorDialog.setTabOrder(self.tags_add,self.tags_delete)
        TagEditorDialog.setTabOrder(self.tags_delete,self.tabWidget)
        TagEditorDialog.setTabOrder(self.tabWidget,self.artwork_list)

    def retranslateUi(self, TagEditorDialog):
        self.label_7.setText(_(u"Disc:"))
        self.label_4.setText(_(u"Track:"))
        self.label_2.setText(_(u"Album artist:"))
        self.label_3.setText(_(u"Artist:"))
        self.tracknumber.setInputMask(_(u"000; "))
        self.label_5.setText(_(u"of"))
        self.totaltracks.setInputMask(_(u"000; "))
        self.discnumber.setInputMask(_(u"000; "))
        self.label_6.setText(_(u"of"))
        self.totaldiscs.setInputMask(_(u"000; "))
        self.date.setInputMask(_(u"0000-00-00; "))
        self.label_9.setText(_(u"Album:"))
        self.label_8.setText(_(u"Date:"))
        self.label.setText(_(u"Title:"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _(u"&Basic"))
        self.tags_add.setText(_(u"&Add..."))
        self.tags_delete.setText(_(u"Delete"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _(u"&Advanced"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _(u"A&rtwork"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _(u"&Info"))

