import discord
from discord.ext import commands
import confidential
import eventdbfunctions
import eventhelpers

client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name=".help"))

@client.command()
async def setEventsChannel(ctx, channel: discord.TextChannel):
    author = ctx.message.author
    guild = ctx.guild
    if author.guild_permissions.administrator == True or author.guild_permissions.manage_guild == True:
        eventdbfunctions.set_events_channel(guild.id, channel.id)
        await ctx.send(":thumbsup:")

@client.command()
async def setApprovalChannel(ctx, channel: discord.TextChannel):
    author = ctx.message.author
    guild = ctx.guild
    if author.guild_permissions.administrator == True or author.guild_permissions.manage_guild == True:
        eventdbfunctions.set_approval_channel(guild.id, channel.id)
        await ctx.send(":thumbsup:")

@client.command()
async def makeEvent(ctx):
    title =""
    description =""
    time=""
    image_url = ""
    addImage = True
    all_set = ""
    guild = ctx.guild
    if eventhelpers._checkChannelsSetUp(guild.id) == False:
        await ctx.send("The channel setup for this server is incomplete. Please contact a moderator for more help.")
        return
    author = ctx.message.author
    if author.dm_channel is None:
        await author.create_dm()
    await author.dm_channel.send(embed=eventhelpers._welcomeEmbed())
    title = await _getNextMessage(author.dm_channel, author)
    if title is None:
        return
    await author.dm_channel.send(embed=eventhelpers._desciptionEmbed())
    description= await _getNextMessage(author.dm_channel, author)
    if description is None:
        return
    await author.dm_channel.send(embed=eventhelpers._timeEmbed())
    time= await _getNextMessage(author.dm_channel, author)
    if time is None:
        return
    await author.dm_channel.send(embed=eventhelpers._imageEmbed())
    image_url = await _getNextMessage(author.dm_channel, author)
    if image_url is None:
        return
    elif image_url == "skip":
        addImage = False
    await author.dm_channel.send("Preview of your event message:")
    eventEmbed=discord.Embed(
        title=title,
        description=description,
        colour=discord.Color.random()
    )
    eventEmbed.set_author(name="Check out this event!")
    eventEmbed.add_field(name=f'Time and Date', value=time, inline=True)
    eventEmbed.add_field(name=f'Author of event submission', value=author.mention, inline=True)

    if addImage:
        eventEmbed.set_image(url=image_url)

    eventEmbed.set_footer(text="This event submission was made by typing `.makeEvent` and was approved by a moderator.")

    await author.dm_channel.send(embed=eventEmbed)
    await author.dm_channel.send(embed=eventhelpers._allSetEmbed())
    all_set = await _getNextMessage(author.dm_channel, author)
    if all_set is None:
        return
    await author.dm_channel.send(embed=eventhelpers._doneEmbed())

    approval_channel_id = eventdbfunctions.get_approval_channel(guild.id)
    approval_channel = guild.get_channel(approval_channel_id)
    message = await approval_channel.send(embed=eventEmbed)
    await message.add_reaction('👍')
    await message.add_reaction('👎')    

async def _getNextMessage(channel, author):
    def check(m):
        return m.channel == channel and m.author == author
    message = None
    try:
        message = await client.wait_for('message', check=check, timeout=300)
    except Exception as e:
        print(e)
        await channel.send("Nothing has been entered after 5 minutes, so the process has ended!")
    content = message.content
    if content == "cancel":
        await channel.send("Process cancelled!")
        return None
    else:
        return content

@client.event
async def on_raw_reaction_add(payload):
    channel = await client.fetch_channel(payload.channel_id)
    message = await channel.fetch_message(payload.message_id)
    guild = message.guild
    emoji = payload.emoji
    user = payload.member
    if message.author == client.user and channel.id == eventdbfunctions.get_approval_channel(guild.id) and str(emoji) == '👍':
        event_channel_id = eventdbfunctions.get_events_channel(guild.id)
        event_channel = guild.get_channel(event_channel_id)
        await message.delete()
        await event_channel.send(embed=message.embeds[0])
    elif message.author == client.user and channel.id == eventdbfunctions.get_approval_channel(guild.id) and str(emoji) == '👎':
        await message.delete()
        
            



client.run(confidential.RUN_ID)