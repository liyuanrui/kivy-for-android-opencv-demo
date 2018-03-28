#coding=utf-8
#qpy:kivy

import time
from kivy.app import App
from kivy.clock import Clock
from kivy.uix.boxlayout import BoxLayout
from camera import Camera2

class MyLayout(BoxLayout):
    pass

class MainApp(App):
    def build(self):
        return MyLayout()
    def on_start(self):
        Clock.schedule_once(self.detect,5)

    def detect(self,nap):
        image=self.root.ids.camera.image
        rows,cols=image.shape[:2]
        ctime=time.ctime()[11:19]
        self.root.ids.label.text='%s image rows:%d cols:%d'%(ctime,rows,cols)
        Clock.schedule_once(self.detect,1)

if __name__ == '__main__':
    MainApp().run()
