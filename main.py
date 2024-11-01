# main.py
from info import *
from rep import reply_func  # استدعاء وظيفة الرد الافتراضية من rep.py
from botcommand import my_comd, mute_member, mute_member_hour  # استدعاء دوال الأوامر
from btns import call_result  # استدعاء وظيفة الأزرار

# معالجة الأعضاء الجدد أو الذين يغادرون
@bot.message_handler(content_types=['new_chat_member', 'left_chat_member'])
def cmbmr(m):
    bot.delete_message(m.chat.id, m.message_id)

# معالجة أوامر /start و /ban
@bot.message_handler(commands=['start', 'ban'])
def myc(m):
    my_comd(m)

# الرد على الرسائل النصية
@bot.message_handler(func=lambda m: True)
def rm(m):
    if m.text == "كتم":
        mute_member(m)
    elif m.text == "كتم ساعة":
        mute_member_hour(m)
    else:
        reply_func(m)

# معالجة الردود التفاعلية من الأزرار
@bot.callback_query_handler(func=lambda call: True)
def calling(call):
    call_result(call)

# بدء البوت
bot.infinity_polling()
