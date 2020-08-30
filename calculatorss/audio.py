import pyttsx3
import os

class playaudio:
    def __init__(self,voice='male',speakstatus=True):
        self.voice='male'
        self.speakstatus=speakstatus
        self.speakwords={
            '1':'one',
            '2':'two',
            '3':'three',
            '4':'four',
            '5':'five',
            '6':'six',
            '7':'seven',
            '8':'eight',
            '9':'nine',
            '-':'minus',
            '+':'plus',
            '/':'divide',
            'x':'multiply',
            '=':'equal to',
            '0':'zero',
            '.':'dot'            
        }
        self.engine=pyttsx3.init()
        v=self.engine.getProperty('voices')
        self.engine.setProperty('voice',v[0].id)
    def speak(self,content):
        if self.speakstatus==True:
            self.engine.say(self.speakwords[content])
            self.engine.runAndWait()
if __name__ == '__main__':
    ob=playaudio()
    ob.speak('=')