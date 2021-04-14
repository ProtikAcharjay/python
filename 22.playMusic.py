from pygame import mixer
def musiconloop(file, stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        input_of_user = input()
        if input_of_user == stopper:
            mixer.music.stop()
            break
print("We are going to play a song right now")
musiconloop('kal ho na ho.mp3', 'stop')