from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *
import pyttsx3
import speech_recognition as s
import threading

engine= pyttsx3.init()
voices= engine.getProperty('voices')
print(voices)
engine.setProperty('voice',voices[1].id)

def speak(word):
    engine.say(word)
    engine.runAndWait()




#print("Hey Say something here in ENGLISH")




bot= ChatBot("Bot")
print("Hello")
convo= [
    "Information regarding",
    "Covid19 2020 Pandemic situation",
    "Where and when did the first case of the coronavirus disease originate?",
    "China , december 2019",

    "Most affected states of india due to covid19",
    "1.Maharashtra 2.NCT of Delhi 3.Tamil Nadu 4.Gujarat 5.Uttar Pradesh 6.Rajasthan 7.West Bengal 8.Madhya Pradesh",
    "2020-8-28 confirmed cases",
    "3468987 confirmed cases"
    "Hello",
    "Hi there!",
    "Safety Tips during corona time ",
    "1. Wash your hand for atleast 20 seconds 2. Avoid close contact 3. Cover your mouth and noise ",

    "What is your name?",
    "My name is COFO bot  and i am created by Anshu The Boss an HMRITM student",
    "11 september 2020 confirmed cases in india",
    "4484029 confirmed cases",
    "Thank you.",
    "You're welcome."
]

trainer= ListTrainer(bot)
trainer.train(convo)

main = Tk()

main.geometry("500x650")
main.title("CHATBOT By Anshu Kumari")
img = PhotoImage("botUsing.png")
PhotoL = Label(main,image=img)
PhotoL.pack(pady=5)

def takeQuery():
    sr = s.Recognizer()
    sr.pause_threshold=0.8
    print("My Bot Is Listening You ")
    with s.Microphone() as m:
        try:
            audio = sr.listen(m)
            
            
            query = sr.recognize_google(audio, language='eng-in')
            print(query)
            textF.delete(0, END)
            textF.insert(0, query)
            ask_from_bot()
                
            
        except Exception as e:
            print(e)
            print("Not Recognized")

def ask_from_bot():
    query= textF.get()
    answer = bot.get_response(query)
    msgs.insert(END, "YOU  :", query)
    msgs.insert(END, "BOT  :", answer)
    speak(answer)
    textF.delete(0, END)
    msgs.yview(END)



frame = Frame(main)
sc = Scrollbar(frame)

msgs = Listbox(frame, width=80, height=20,yscrollcommand=sc.set)
sc.pack(side=RIGHT, fill=Y)
msgs.pack(side=LEFT, fill=BOTH, pady=10)
frame.pack()

textF = Entry(main, font=("Verdana", 20))
textF.pack(fill=X, pady=10)
btn = Button(main, text="Ask From CO-FO bot", font=("Verdana", 20),command=ask_from_bot)
btn.pack()

def enter_function(event):
    btn.invoke()

main.bind('<Return>',enter_function)

def repeatL():
    while True:
        takeQuery()

t= threading.Thread(target=repeatL)

t.start()
main.mainloop()





