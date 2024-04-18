from datetime import datetime

def sample_responses(input_text):
    user_message = str(input_text).lower()

    if user_message in ('hello', 'hi', 'sup'):
        return "Hey! How's it going?"
    
    if user_message in ('who are you', 'who are you?'):
        return "I am Python Bot"

    if user_message in ('time', 'time?', 'date', 'date?'):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%y, %H:%M:%S")

        return str(date_time)
    
    if user_message in ('السلام عليكم'):
        return "وعليكم السلام ورحمة الله وبركاته"

    if user_message in ('كيف حالك', 'اخبارك'):
        return 'الحمدلله بخير'

    if user_message in ('شكرا'):
        return 'عفوا الشكرلله'

    return "I don't learn to response that"