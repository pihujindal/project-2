from kivymd.app import MDApp
from kivy.lang import Builder

class SampleApp(MDApp):
    
    def build(self):
        self.appKv='''
MDScreen:
    MDLabel:
        text:'Welcome to pihu tech'
        multiline:True
        halign:'center'         
'''
        AppScreen=Builder.load_string(self.appKv)
        return AppScreen

SampleApp().run()
    
