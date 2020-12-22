import speech_recognition as sr 
import pyttsx3 
import keyboard
import sys
from datetime import datetime 

print("----------Speak!----------")
# Initialize the recognizer 
r = sr.Recognizer() 
fp = open('speechRecog.txt', 'a');

# Function to convert text to 
# speech 
def SpeakText(command): 
 
 # Initialize the engine 
	engine = pyttsx3.init() 
	engine.say(command) 
	engine.runAndWait() 
 
def savetxt(txt):
	txt += '.\n'
	s=str(datetime.now())
	d=' :: '
	fp.write(s+d+txt)
	
 
 
# Loop infinitely for user to 
# speak 
 
while(1): 
 
 # Exception handling to handle 
 # exceptions at the runtime 
	try: 
	
 # use the microphone as source for input. 
		with sr.Microphone() as source2: 
 
 # wait for a second to let the recognizer 
 # adjust the energy threshold based on 
 # the surrounding noise level 
			r.adjust_for_ambient_noise(source2, duration=0.2) 
 
 #listens for the user's input 
			audio2 = r.listen(source2) 
 
 # Using ggogle to recognize audio 
			MyText = r.recognize_google(audio2) 
			MyText = MyText.lower() 
 
			print("Did you say -"+MyText) 
			savetxt(MyText)
			SpeakText(MyText)
			
			
 
	except sr.RequestError as e: 
		print("Could not request results; {0}".format(e)) 
 
	except sr.UnknownValueError: 
		print("Sorry, Can't hear you. Repeat again!")
		
	except KeyboardInterrupt:
		print("----------KeyboardInterrupt----------")
		sys.exit()
		sys.close()
	 	
	
fp.close()

 


 