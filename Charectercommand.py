import turtle
import speech_recognition as sr
import pyttsx3

#turtle color
turtle.color("blue")

#initialising python speech 
engine = pyttsx3.init()
rate = engine.getProperty('rate')
engine.setProperty('rate',150)
volume = engine.getProperty("volume")
engine.setProperty('volume', volume-0.05)
#initialising recogniser
recogniser = sr.Recognizer()

#capturing audio
with sr.Microphone() as source:
    print("say something: ")
    # adjust for ambient noise
    recogniser.adjust_for_ambient_noise(source)
    audio = recogniser.listen(source)

#recognise speech using google api
    
try:
    text = recogniser.recognize_google(audio)
    print(":", text)
    engine.say("You said")
    engine.say(text)
    engine.runAndWait()
except sr.UnknownValueError:
    print("Sorry i could not get that")
except sr.RequestError as e:
    print("error connecting to api")


# Create a new turtle named "slow_turtle"
slow_turtle = turtle.Turtle()

# Set the speed of the turtle
slow_turtle.speed(1)
while True:
        
    if text == "forward":
        slow_turtle.forward(200)
    if text == "left":
        slow_turtle.left(90)
    if text == "backward":
        slow_turtle.backward(200)
    if text == "right":
        slow_turtle.right(90)


turtle.done()  

