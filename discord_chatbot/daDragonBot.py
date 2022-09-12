import discord
from discord.ext import commands, tasks
from discord.voice_client import VoiceClient
import youtube_dl
import os
import requests
import json
import random
from random import choice
from replit import db
import asyncio

# i had this hosted on Replit.com using UptimeRobot to keep it alive

from keep_alive import keep_alive

client = discord.Client()

youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
  'format': 'bestaudio/best',
  'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
  'restrictfilenames': True,
  'noplaylist': True,
  'nocheckcertificate': True,
  'ignoreerrors': False,
  'logtostder': False,
  'quiet': True,
  'no_warnings': True,
  'default_search': 'auto',
  'source_address': '0.0.0.0'
}

ffmpeg_options = {
  'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
  def __init__(self, source, *, data, volume=0.5):
    super().__init__(source, volume)

    self.data = data

    self.title = data.get('title')
    self.url = data.get('url')

  @classmethod
  async def from_url(cls, url, *, loop=None, stream=False):
    loop= loop or asyncio.get_event_loop()
    data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

    if 'entries' in data:
      data = data['entries'][0]

    filename = data['url'] if stream else ytdl.prepare_filename(data)
    return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)

status = ['Music and Jammin!', 'Eating mutton!', 'Counting the hoard!', 'Sleeping!']

sad_words = ["sad", "shitty", "fucked up", "lame", "sucks", "depressed", "unhappy", "angry", "miserable", "depressing", "depression", "fatigued",
"bad", "blue", "brokenhearted", "cast down", "crestfallen", "dejected", "depressed", "despondent", "disconsolate", "doleful", "down", "downcast", "downhearted", "down in the mouth", "droopy", "forlorn", "gloomy", "glum", "hangdog", "heartbroken", "heartsick", "heartsore", "heavyhearted", "inconsolable", "joyless", "low", "low-spirited", "melancholic", "melancholy", "miserable", "mournful", "saddened", "sorrowful", "sorry", "unhappy", "woebegone", "woeful", "wretched"]

starter_encouragements = [
  "Cheer up!",
  "Hang in there!",
  "You are a great person/bot!"
]

if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " - " + json_data[0]["a"]
  return (quote)

def update_encouragements(encouraging_message):
  if "encouragements" in db.keys():
    encouragements = db["encouragements"]
    encouragements.append(encouraging_message)
    db["encouragements"] = encouragements
  else:
    db["encouragements"] = [encouraging_message]

def update_que(que_add):
  if "que" in db.keys():
    que = db["que"]
    que.append(que_add)
    db["que"] = que
  else:
    db["que"] = [que_add]

def delete_que(index):
  que = db["que"]
  if len(que) > index:
    del que[index]
    db["que"] = que

def delete_encouragement(index):
  encouragements = db["encouragements"]
  if len(encouragements) > index:
    del encouragements[index]
    db["encouragements"] = encouragements

@client.event
async def on_ready():
  change_status.start()
  print('We have logged in as {0.user}'.format(client))

@tasks.loop(seconds=60)
async def change_status():
  await client.change_presence(activity=discord.Game(choice(status)))

@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  if msg.startswith('$help'):
    await message.channel.send('Help: $wisdom/attack/hide/list/new yourencouragment/del 0 to whatever index number of item in database starting at 0.')

  if msg.startswith('$hello'):
    dragResp = ['***GRUMBLE*** Why did you wake me?', 'Adventurer, what treasures to do seek?', '***ROOAAARR***, It was unwise to come here!']
    await message.channel.send(choice(dragResp))

  if msg.startswith('$ping'):
    await message.channel.send(f'**Pong!** Latency: {round(client.latency * 1000)}ms')

  if msg.startswith('$wisdom'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]

    if any(word in msg for word in sad_words):
      await message.channel.send(random.choice(options))

  if msg.startswith("$new"):
    encouraging_message = msg.split("$new ",1)[1]
    update_encouragements(encouraging_message)
    await message.channel.send("New encouraging message added!")

  if msg.startswith("$del"):
    encouragements = []
    if "encouragements" in db.keys():
      index = int(msg.split("$del", 1)[1])
      delete_encouragement(index)
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$list"):
    encouragements = []
    if "encouragements" in db.keys():
      encouragements = db["encouragements"]
    await message.channel.send(encouragements)

  if msg.startswith("$attack"):
    bot_health = int()
    attack = random.randint(1,20)
    dmg = random.randint(1,10) + random.randint(1,10)
    if attack >= 12:
      bot_health = bot_health + dmg
      await message.channel.send("A wound opens as you do " + str(dmg) + " dmg!! A long challenge awaits!")
      return bot_health
    else:
      drag_bite = random.randint(1,20) + 2
      drag_dmg = random.randint(1,8) + random.randint(1,8)
      await message.channel.send("'Your flimsy attacks are no match for me!!' daDragon bites out at you for a " + str(drag_bite) + " to hit, for " + str(drag_dmg) + " dmg!!")

  if msg.startswith("$hide"):
    hide = random.randint(1,20)
    if hide >= 12:
      await message.channel.send(str(hide) + "!! You are hidden till next attack!!")
    else:
      await message.channel.send("There is no escape from daDragon!!!")

  if msg.startswith("$responding"):
    value = msg.split("$responding ",1)[1]

    if value.lower() == "true":
      db["responding"] = True
      await message.channel.send("Responding is on!")
    else:
      db["responding"] = False
      await message.channel.send("Responding is off!")

  if msg.startswith("$join"):
    if not message.author.voice:
      await message.channel.send("Please Connect to a Voice Channel.")
      return
    else:
      channel = message.author.voice.channel
      await channel.connect()

  if msg.startswith("$que"):
    que_add = msg.split("$que ",1)[1]
    update_que(que_add)
    await message.channel.send("New song added to que!")

  if msg.startswith("$remove"):
    que = []
    if "que" in db.keys():
      index = int(msg.split("$remove", 1)[1])
      delete_que(index)
      que = db["que"]
    await message.channel.send(que)

  if msg.startswith("$play"):
    que = ["que"]
    index = 0;
    server = message.author.guild
    voice_channel = server.voice_client
    player = await YTDLSource.from_url(que[0], loop=client.loop)
    voice_channel(player, after=lambda e: print('Player error: %s' % e) if e else None)
    await message.channel.send("**Now playing**")
    index = 0
    delete_que(index)

  if msg.startswith("$stop"):
    voice_client = message.author.guild.voice_client
    await voice_client.disconnect()

keep_alive()

client.run(os.getenv('TOKEN'))
