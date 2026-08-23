import os, time, re
id_pattern = re.compile(r'^.\d+$')



class Config(object):
    # pyro client config
    API_ID    = os.environ.get("API_ID", "32541562")
    API_HASH  = os.environ.get("API_HASH", "e37e4432298d5a5eb4a6e32c18804283")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "8813217868:AAFplgrX7Kie_rzursBp1u689UJW5GyhsJ0") 
   
    # database config
    DATABASE_NAME = os.environ.get("DATABASE_NAME","yato")     
    DATABASE_URL  = os.environ.get("DATABASE_URL","mongodb+srv://aaryansah954:QgDQRgyD7VUa7Eho@cluster0.wjo9zfm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
 
    # other configs
    BOT_UPTIME  = time.time()
    START_PIC   = os.environ.get("START_PIC", "https://64.media.tumblr.com/04812811d689a930620ac4eea583b3ee/d4a1eaa3f9029f76-f4/s1280x1920/77fb3e77d4531f4692fa4715112bdaf7b6806c05.jpg")
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '2021145517').split()]

    # channels logs
    FORCE_SUBS   = os.environ.get("FORCE_SUBS", "") 
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1002521835919"))

    # wes response configuration     
    WEBHOOK = bool(os.environ.get("WEBHOOK", False))



class Txt(object):
    # part of text configuration
    START_TXT = """Hello {} 👋 

➻ This Is An Advanced And Yet Powerful Rename Bot. | Using This Bot You Can Rename And Change Thumbnail Of Your Files.
➻ You Can Also Convert Video To File And File To Video. | This Bot Also Supports Custom Thumbnail And Custom Caption."""

    ABOUT_TXT = """
╭───────────────⍟
├<b>My Name</b> : {}
├<b>Developer</b> : <a href=https://t.me/MadflixBotz>MadflixBotz</a> 
├<b>Programer</b> : <a href=https://t.me/MadflixSupport>Jishu Developer</a>
├<b>Library</b> : <a href=https://github.com/pyrogram>Pyrogram</a>
├<b>Language</b> : <a href=https://www.python.org>Python 3</a>
├<b>Database</b> : <a href=https://cloud.mongodb.com>Mongo DB</a>
├<b>Build Version</b> : <a href=https://instagram.com/jishukumarsinha>Rename v4.7.0</a></b>     
╰───────────────⍟
"""

    HELP_TXT = """
🌌 <b><u>How To Set Thumbnail</u></b>
  
➪ /start - Start The Bot And Send Any Photo To Automatically Set Thumbnail.
➪ /del_thumb - Use This Command To Delete Your Old Thumbnail.
➪ /view_thumb - Use This Command To View Your Current Thumbnail.

📑 <b><u>How To Set Custom Caption</u></b>

➪ /set_caption - Use This Command To Set A Custom Caption
➪ /see_caption - Use This Command To View Your Custom Caption
➪ /del_caption - Use This Command To Delete Your Custom Caption
➪ Example - <code>/set_caption 📕 Name ➠ : {filename}

🔗 Size ➠ : {filesize} 

⏰ Duration ➠ : {duration}</code>

✏️ <b><u>How To Rename A File</u></b>

➪ Send Any File And Type New File Name And Select The Format [ Document, Video, Audio ].           

"""

    PROGRESS_BAR = """\n
 <b>🔗 Size :</b> {1} | {2}
️ <b>⏳️ Done :</b> {0}%
 <b>🚀 Speed :</b> {3}/s
️ <b>⏰️ ETA :</b> {4}
"""

    DONATE_TXT = """
<b>🥲 Thanks For Showing Interest In Donation! ❤️</b>

If You Like My Bots & Projects, You Can 🎁 Donate Me Any Amount From 10 Rs Upto Your Choice.

<b>🛍 UPI ID:</b> `fork.aaryan@fam`
"""


    SEND_METADATA = """<b><u>🖼️  HOW TO SET CUSTOM METADATA</u></b>

For Example :-

<code>By :- @MadflixBotz</code>

💬 For Any Help Contact @MadflixSupport
"""








# Jishu Developer 
# Don't Remove Credit 🥺
# Telegram Channel @MadflixBotz
# Backup Channel @JishuBotz
# Developer @JishuDeveloper
# Contact @MadflixSupport
