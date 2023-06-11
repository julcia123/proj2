# -*- coding: utf-8 -*-
"""
/***************************************************************************
 wtyczka_projektDialog
                                 A QGIS plugin
 Wtyczka pozwalająca na liczenie przewyższenia pomiędzy dwoma punktami oraz pole powierzchni metodą Gaussa
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2023-06-10
        git sha              : $Format:%H$
        copyright            : (C) 2023 by wdef
        email                : julka571@gmail.com
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
"""


import os
from qgis.PyQt import uic
from qgis.PyQt import QtWidgets
from qgis.core import QgsMessageLog, Qgis
import numpy as np
import os
from qgis.core import QgsProject, QgsPointXY
from qgis.utils import iface


# This loads your .ui file so that PyQt can populate your plugin with the elements from Qt Designer
FORM_CLASS, _ = uic.loadUiType(os.path.join(
    os.path.dirname(__file__), 'wtyczka_pro_dialog_base.ui'))


class wtyczka_projektDialog(QtWidgets.QDialog, FORM_CLASS):
    def __init__(self, parent=None):
        """Constructor."""
        super(wtyczka_projektDialog, self).__init__(parent)
        # Set up the user interface from Designer through FORM_CLASS.
        # After self.setupUi() you can access any designer object by doing
        # self.<objectname>, and you can use autoconnect slots - see
        # http://qt-project.org/doc/qt-4.8/designer-using-a-ui-file.html
        # #widgets-and-dialogs-with-auto-connect
        self.setupUi(self)
        
        self.PB_wys.clicked.connect(self.licz_roznice_wys)
        
        
        self.PB_pole.clicked.connect(self.licz_pole)
        
        
    def licz_roznice_wys(self):
        
        obiekt = self.layer.currentLayer()
        if obiekt is None:
            iface.messageBar().pushMessage("Różnica wysokosci", 'Nie wybrano aktywnej warstwy', level = Qgis.Warning)
            return
        
        obiekt2 = self.layer.currentLayer().selectedFeatures()
        if len(obiekt2) != 2:
            iface.messageBar().pushMessage("Różnica wysokosci", 'Aby policzyć wysokosc wybierz DWA PUNKTY', level = Qgis.Warning)
            return
        
        if len(obiekt2) == 2:
            
            H1 = float(obiekt2[0]['h_plevrf2007nh'])
            H2 = float(obiekt2[1]['h_plevrf2007nh'])
            
            przewyzszenie = round(H2 - H1, 3)
            
            self.label_wys.setText(str(przewyzszenie))
            
            
        QgsMessageLog.logMessage('Różnica wysokości między wybranymi punktami wynosi:' +str(przewyzszenie) +'m', level = Qgis.Success)
        
        iface.messageBar().pushMessage("Różnica wysokosci", 'Różnica wysokości między wybranymi punktami wynosi:' +str(przewyzszenie), level = Qgis.Success)
        
        
        
        
        
    #def licz_pole(self):
        
        