from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ("hello", "hi", "sup"):
        return "Hey now's it going"


    if user_message in ("who are you", "who are you ?", "Как зовут ?", "как зовут ?"):
        return "I am Eminbot"

    if user_message in ("bitch", "you bitch", "пидарас"):
        return "Fuck you"
    
    if user_message in ("Как дела", "как дела ?"):
        return "good"

    if user_message in ("time", "time ?"):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)

    return "I don't understand you"