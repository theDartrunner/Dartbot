import discord
description = 'Shows playlist queue'

async def command(dartbot, message):
    server_voice = None
    for voice in dartbot.client.voice_clients:
        if voice.guild == message.author.guild:
            server_voice = voice
    if server_voice is None:
        await message.channel.send('I am not connected to any voice chat, dummy!')
        return

    if server_voice.source is None:
        await message.channel.send('There is nothing in the queue right now')
        return

    playlist = server_voice.source.get_playlist()
    title = str(len(playlist)) + ' songs'
    desc = ''
    for song in playlist:
        desc += (song.metadata['title'] if song.metadata is not None else 'No title') + '\n'
    embed = discord.Embed(title=title, description=desc, color=0xff00ff)
    await message.channel.send(embed=embed)