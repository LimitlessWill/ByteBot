from discord.ext import tasks
from base import client
from grendate import GrenDate

ID_CHANNEL_CORNJOB = 971240750731890738

# A cornjob loops every 1 minute (get time send it in a specific channel)
@tasks.loop(minutes=1)
async def test():
 channel = client.get_channel(ID_CHANNEL_CORNJOB)
 year,month,day,month_name,hour,minute,meridiem = GrenDate().now()
 season = GrenDate(int(year),int(month),int(day)).season()
 sp = "\t"
 cur = f"\n\n{sp*5}    {year}/{month_name}/{day}\n\n{sp*5}\💚    {hour}:{minute}  {meridiem}    \💚"  
 await channel.send(f"{sp*5}**{cur}**\n{sp*10}**{season}**",delete_after=59)


@client.event
async def on_ready():
 print(f"{client.user} has connected to Discord!\nHello World")
 print("------")
 print("test function is starting ...")
 await test.start()

