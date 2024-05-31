import discord
import tokenSecret as ts
import discordPhrases

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    
    async def on_message(self, message):
        if message.author == client.user:
            return
        
        if message.content.startswith('$kramnik'):
            await message.channel.send(discordPhrases.kramnik1)
            await message.channel.send(discordPhrases.kramnik2)    

        print(f'Message from {message.author}:{message.content}')

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(ts.token)