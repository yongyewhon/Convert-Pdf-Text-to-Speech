# Convert-Pdf-Text-to-Speech
Text to Speech by using pyttsx3 to converting a PDF file and text file into audio and MP3

Packages Used:

pyttsx3: It is a text-to-speech conversion library in Python. It will help the machine to speak to us

PyPDF2: It will convert to the text from the PDF. A Pure-Python library built as a PDF toolkit. It is capable of extracting document information, splitting documents page by page, merging documents page by page etc. Can follow the my previous repositories (Create-and-Modify-PDF-Files-in-Python)

  pip install pyttsx3

  pip install pypdf

  sudo apt install libespeak1 is required for Linux system


-An application invokes the pyttsx3.init() factory function to get a reference to a pyttsx3. Engine instance

-The pyttsx3 module supports two voices first is male and the second is female for Windows

  e.g. voice_engine.setProperty("voice", voices[0].id) # Male voice

  e.g. voice_engine.setProperty("voice", voices[1].id) # Female voice

-Remember to comment the code on voice_engine.setProperty("voice", voices[0].id) and voice_engine.setProperty("voice", voices[1].id) for Linux


-Integer speech rate in words per minute. Defaults to 200 word per minute

  voice_engine.setProperty("rate", 200)


-Floating point volume in the range of 0.0 to 1.0 inclusive. Defaults to 1.0

  voice_engine.setProperty("volume", 1.0)


Three examples are included

1. Select a page of PDF file to perform text-to-speech conversion and save to audio 

2. Text file for text-to-speech conversion and save to audio 

3. Whole PDF file to text file conversion for text-to-speech conversion and save to audio 
