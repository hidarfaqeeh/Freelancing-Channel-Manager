import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from telegram import Bot, ChatMember, InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
from telegram.chataction import ChatAction
from telegram.parsemode import ParseMode
import os
import time
import datetime
from os.path import join as pjoin
import json


# Parameters
BOT_API = "1543026455:AAEMi_2iq71gnKn9jX-j_MGhTvoQOxLMe5c"
MAIN_CHANNEL = "@zawamlansarallah"
SUPPORT_USER = "@jod_yemen"
BOT_ID = '1543026455'
ADMIN_PASSWORD = 'hidar'
owenerID = 1 # Don't change this
# Parameters

# messages 
SabteAgahi = '📢' + 'Post a new ad'
ErtebatBaPoshtibani = '👩‍💻' + 'Contact support'
RahnamayeRobot = '🌐' + 'Guide'
YesSendit_posht = '👍' + 'yes, send it'
NoDontSendit_posht = '👎' + 'no, do not send it'
# messages 


##### owner pannel
users_count = 'Show number of users'
send_to_all = 'Send message to all users'
Deactive_bot = 'Block ad submission'
change_format = 'Change ads format'
enseraf_as_agahi = 'Cancel'
global_message = 0
global_message_id = None
Bot_ACTIVE_boolian = True
boolian_money = False
money_message = None
mozo_boolian = True
onvan_boolian = True
pishnagadiprice_boolian = True
tozihat_boolian = True
##### owner pannel
