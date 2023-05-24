import win32com.client

speakers  = win32com.client.Dispatch("SAPI.SpVoice")

while 1:
    print("Enter the work")
    s = input()
    speakers.Speak(s)