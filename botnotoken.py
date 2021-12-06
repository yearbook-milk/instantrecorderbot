import discord
client = discord.Client()

@client.event
async def on_message(message):
    msg = f'ID = {message.channel.id}, CONTENTS = {message.content}, ATTACHMENTS = {message.attachments}\n'
    f = open('log.txt','a')
    f.write(msg)
    f.close()
    
client.run('API KEY')