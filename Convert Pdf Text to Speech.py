# sudo apt install libespeak1
# sudo apt-get install espeak
# importing the modules
import pypdf
import pyttsx3

# Initialize the Pyttsx3 engine
voice_engine = pyttsx3.init()
voices = voice_engine.getProperty("voices")
volume = voice_engine.getProperty("volume")
rate = voice_engine.getProperty("rate")
#voice_engine.setProperty("voice", voices[0].id) # Male voice
voice_engine.setProperty("voice", voices[1].id) # Female voice
# Integer speech rate in words per minute. Defaults to 200 word per minute
voice_engine.setProperty("rate", 200)
# Floating point volume in the range of 0.0 to 1.0 inclusive. Defaults to 1.0
voice_engine.setProperty("volume", 1.0)

def pdf_to_speech(select_page, pdf_file, output_audio):
    # creating a PdfFileReader object
    reader = pypdf.PdfReader(pdf_file)

    total_page = len(reader.pages)

    if select_page < total_page:
        # the page with which you want to start
        page = reader.pages[select_page]

        # extracting the text from the PDF
        text = page.extract_text()

        if voice_engine.isBusy():
            # We can use file extension as mp3 and wav, both will work
            voice_engine.save_to_file(text, output_audio)

            # reading the text
            voice_engine.say(text)

            # Wait until above command is not finished.
            voice_engine.runAndWait()

def text_to_speech(text_file, output_audio):
    # creating a PdfFileReader object
    with open(text_file) as file:
        file = file.read().strip().split("\n")
        if len(file) > 0 and voice_engine.isBusy():
            voice_engine.save_to_file(file, output_audio)
            voice_engine.say(file)
            voice_engine.runAndWait()

def pdf_to_text_speech(pdf_file, output_text, output_audio):
    reader = pypdf.PdfReader(pdf_file)
    total_page = len(reader.pages)

    # extracting text from whole pdf
    if total_page > 0:
        with open(output_text, "w") as file: file.write("")
        for select in range(total_page):
            print(select)
            page = reader.pages[select]
            with open(output_text, "a") as file:
                file.write(page.extract_text() + "\n\n\n")
        text_to_speech(output_text, output_audio)

#1 Select a page of PDF file to perform text-to-speech conversion and save to audio 
pdf_to_speech(1, "sample_a.pdf", "audio1.mp3")

#2 Text file for text-to-speech conversion and save to audio 
text_to_speech("sample_c.txt", "audio2.mp3")

#3 Whole PDF file to text file conversion for text-to-speech conversion and save to audio 
pdf_to_text_speech("sample_d.pdf", "output.txt", "audio3.mp3")
