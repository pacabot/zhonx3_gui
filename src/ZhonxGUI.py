# import logging

from kivy.app import App
# from kivy.logger import Logger
import serial
from serial.tools import list_ports

import ZhonxCommand
from kivy.uix.spinner import Spinner
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.switch import Switch
from kivy.uix.tabbedpanel import TabbedPanel, TabbedPanelItem
from math import sin
from kivy.garden.graph import Graph, MeshLinePlot


# Logger.setLevel(logging.CRITICAL)


def listSerialPorts():
    ports = list_ports.comports()
    portList = list()
    for port in ports:
        portList.append(port.device)
    return portList
        
  
class ZhonxGUIApp(App):
    
    def connect(self, instance, value):
        print('the switch', instance, 'is', value)
        if value == True:
            try:
                self.connection = serial.Serial(self.dlPort.text, self.dlBaudrate.text)
            except Exception as e:
#                 instance.active = False
                print(e)
        else:
            try:
                self.connection.close()
            except Exception as e:
#                 instance.active = True
                print(e)
    
    def build(self):
        self.availablePorts = listSerialPorts()
        if len(self.availablePorts) == 0:
            self.availablePorts.append("----")
        
        tabbedPannel = TabbedPanel(do_default_tab=False)
        
        # Connection Tab
        self.connectionTab = TabbedPanelItem(text="Connection")
        
        self.layout1 = BoxLayout(orientation='vertical', spacing=10, padding=(200, 200))
        self.connectionTab.add_widget(self.layout1)
        
        self.lblSerialSettings = Label(text="Connection settings")
        self.layout1.add_widget(self.lblSerialSettings)
        
        self.dlBaudrate = Spinner(values = ["57600", "115200", "230400", "460800", "921600"],
                                  text = "115200")
        self.layout1.add_widget(self.dlBaudrate)
        
        self.dlPort = Spinner(values = self.availablePorts,
                              text = self.availablePorts[0])
        self.layout1.add_widget(self.dlPort)
        
        self.btnConnect = Switch()
        self.btnConnect.bind(active = self.connect)
        
        self.layout1.add_widget(self.btnConnect)
        
        # Graph tab
        self.graphTab = TabbedPanelItem(text = "Graph")
#         self.layout2 = BoxLayout(orientation='vertical', spacing=10, padding=(200, 200))
#         self.graphTab.add_widget(self.layout2)
        
        graph = Graph(xlabel='X', ylabel='Y', x_ticks_minor=5,
        x_ticks_major=25, y_ticks_major=1,
        y_grid_label=True, x_grid_label=True, padding=5,
        x_grid=True, y_grid=True, xmin=-0, xmax=100, ymin=-1, ymax=1)
        plot = MeshLinePlot(color=[1, 1, 0, 1])
        plot.points = [(x, sin(x / 10.)) for x in range(0, 101)]
        graph.add_plot(plot)
        self.graphTab.add_widget(graph)
        
        
        tabbedPannel.add_widget(self.connectionTab)
        tabbedPannel.add_widget(self.graphTab)
        return tabbedPannel

if __name__ == '__main__':
#     listSerialPorts()
    ZhonxGUIApp().run()