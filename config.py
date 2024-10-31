env_vars = {
  # Get From my.telegram.org
  "API_HASH": "2b79fd2d2c83173807a039325e7e166f",
  # Get From my.telegram.org
  "API_ID": "23023343",
  #Get For @BotFather
  "BOT_TOKEN": "8188564702:AAHxYGMmAvYFtbZv5Mi0xD0bBPkPMhyV9uA",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "postgresql://itzmecp_owner:wKDqWiEdQ7c2@ep-bold-voice-a5kb68wc.us-east-2.aws.neon.tech/itzmecp?sslmode=require",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "itzcpbotlogs",
  # Force Subs Channel username without @
  "CHANNEL": "Animeforyoulk",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "",
  # Put Thumb Link 
  "THUMB": ""
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
