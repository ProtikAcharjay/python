def speak(str):
    from win32com.client import Dispatch
    speak=Dispatch("sapi.spvoice")
    speak.speak(str)
if __name__ == '__main__':
    speak("Protik the best great don in the world")
    speak("Thanks Buddy")
    p=open("Protik.txt")
    file=p.read()
    speak(file)
    p.close()
