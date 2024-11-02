env_vars = {
  # Get From my.telegram.org
  "API_HASH": "2b79fd2d2c83173807a039325e7e166f",
  # Get From my.telegram.org
  "API_ID": "23023343",
  #Get For @BotFather
  "BOT_TOKEN": "8188564702:AAHlI1L3m1U5Hliemj1QKLoGlnbP8QFjFu0",
  # Get For tembo.io
  "DATABASE_URL_PRIMARY": "postgres://koyeb-adm:ho2dWgXF1mvr@ep-weathered-firefly-a2lujlmx.eu-central-1.pg.koyeb.app/koyebdb",
  # Logs Channel Username Without @
  "CACHE_CHANNEL": "Animemangacp",
  # Force Subs Channel username without @
  "CHANNEL": "AnimeDownloaderX",
  # {chap_num}: Chapter Number
  # {chap_name} : Manga Name
  # Ex : Chapter {chap_num} {chap_name} @Manhwa_Arena
  "FNAME": "{chap_num} {chap_name} [SLMangaBay]",
  # Put Thumb Link 
  "THUMB": "slmangabay.jpg"
}

dbname = env_vars.get('DATABASE_URL_PRIMARY') or env_vars.get('DATABASE_URL') or 'sqlite:///test.db'

if dbname.startswith('postgres://'):
    dbname = dbname.replace('postgres://', 'postgresql://', 1)
    
