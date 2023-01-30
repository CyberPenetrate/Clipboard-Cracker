#Clipboard Cracker

#A simple tool which captures copied text
#from clipboard and save to a text file.

#Author - Cyber Penetrate

#Import library
import pyperclip as pc

#Get the data from the clipboard
clipboard_text = pc.paste()

#Save all copied text to a text file
with open("log.txt", 'a') as f:
        f.write(clipboard_text + "\n")
