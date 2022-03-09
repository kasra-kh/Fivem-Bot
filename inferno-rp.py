import os
import time
import random
import asyncio
import discord
import requests as rq
from asyncio import *
from discord import embeds
from discord import colour
from discord.ext import tasks
from discord.ext import commands
from discord.ext.commands.errors import DisabledCommand


intents = discord.Intents.default()
intents.members=True
client = discord.Client(intents=intents)

colors = [0x01b8a1, 0xaa0e6c, 0x390174, 0xf6fa02, 0x5df306, 0x2206f3, 0xfffdfd, 0xff0a0e, 0x850000, 0xe76868, 0x4eca75, 0xb38203, 0xc44400, 0x000000, 0x0517dd, 0x6c6f92, 0x144900, 0xffffff, 0x020246, 0xe209b7, 0x0976e2, 0x3de209, 0xe29209, 0x08a247]


class CONFIG:
    TOKEN = "" # Your Token
    PREFIX = "" # Your Prefix
    guildID = 0 #Your Discord Server ID
    serverIP = ""#IP:PORT | Example: 127.0.0.1:30120
    URl = "" #your discord icon

client = commands.Bot(command_prefix=CONFIG.PREFIX)
client.remove_command("help")


@client.event
async def on_ready():
    servers = client.guilds
    servers.sort(key=lambda x: x.member_count, reverse=True)
    y = 0
    for x in client.guilds:
        y += x.member_count
    print(f"Developer's {len(client.users)}, In {len(client.guilds)} Server's Is Rune:), See {y}+ Users!,  Bot Run Shod!")
    client.my_current_task = live_status.start()

def pc():
    try:
        resp = rq.get('http://'+CONFIG.serverIP+'/players.json').json()
        return(len(resp))
    except:
        return('N/A')

#  run shodan Bot



@client.command(aliases=["LOCK", "Lock"], pass_context=True)
@commands.has_permissions(manage_channels=True)
async def lock(ctx, channel: discord.TextChannel=None):
    if channel == None:
        embed = discord.Embed(title="Lotfan channel mored nazar ra Tag konid!", colour=random.choice(colors))
        embed.set_footer(text="mesal : Lock #x", icon_url = ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    else:
        the_channel = client.get_channel(channel.id)
        await the_channel.set_permissions(ctx.guild.default_role, send_messages=False)
        embed = discord.Embed(title="🔒 channel ro kardam az posht ghofl :))", colour=random.choice(colors))
        await channel.send(embed=embed)

#   Lock channel




@lock.error
async def lock_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            colour=random.choice(colors)
        )
        embed.set_author(
            name="Shoma Gabeliyat estefade az dastor ($lock) ra nadarid ⛔❌",
        )
        await ctx.reply(embed=embed)


# Dastresi be $lock


@client.command(aliases=["unLOCK", "unLock", "UNLOCK", "Unlock", "UNlock", "UNLock"], pass_context=True)
@commands.has_permissions(manage_channels=True)
async def unlock(ctx, channel: discord.TextChannel):
    if channel == None:
        embed = discord.Embed(title="Lotfan channel mored nazar ra Tag konid!", colour=random.choice(colors))
        embed.set_footer(text="mesal : Lock #x", icon_url = ctx.author.avatar_url)
        await ctx.reply(embed=embed)
    else:
        the_channel = client.get_channel(channel.id)
        await the_channel.set_permissions(ctx.guild.default_role, send_messages=True)
        embed = discord.Embed(title="🔒 channel has been unLock", colour=random.choice(colors))
        await channel.send(embed=embed)

#   Unlock kardan



@unlock.error
async def unlock_error(ctx, error):
    if isinstance(error, commands.CheckFailure ):
        embed = discord.Embed(
            colour=random.choice(colors)
        )
        embed.set_author(
            name="Shoma Gabeliyat estefade az dastor ($unlock) ra nadarid ⛔❌",
        )
        await ctx.reply(embed=embed)




@client.command(aliases=["user", "User"])
async def userinfo(ctx, member: discord.Member = None):
    if not member:  
        member = ctx.message.author  
    roles = [role for role in member.roles]
    embed = discord.Embed(colour=random.choice(colors), timestamp=ctx.message.created_at,
                          title=f"User Info  {member}")
    embed.set_thumbnail(url=member.avatar_url)
    embed.set_footer(text=f"Darkhast Tavasot: {ctx.author}", icon_url = ctx.author.avatar_url)

    embed.add_field(name="ID:", value=member.id)
    embed.add_field(name="Nickname:", value=member.display_name)

    embed.add_field(name="Created Account On:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p "))
    embed.add_field(name="Joined Server On:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p "))

    embed.add_field(name="Roles:", value="".join([role.mention for role in roles]))
    embed.add_field(name="Top Role:", value=member.top_role.mention)

    await ctx.reply(embed=embed)


# user info


@client.command()
@commands.has_permissions(administrator=True)
async def unmute(cdv, member: discord.Member):
    mutedRole = discord.utils.get(cdv.guild.roles, name="Muted")

    await member.remove_roles(mutedRole)
    embed = discord.Embed(title=f" shoma unmute shodid! **( {member.name} )**", colour=random.choice(colors))
    await cdv.send(embed=embed)
    embed = discord.Embed(title=f" shoma unmute shodid az server: **( {cdv.guild.name} )**", colour=random.choice(colors))
    await member.send(embed=embed)

#unmute server


@client.command()
@commands.has_permissions(administrator=True)
async def mute(cdv, member: discord.Member, *, reason=None):
    guild = cdv.guild
    mutedRole = discord.utils.get(guild.roles, name="Muted")
    if not mutedRole:
        mutedRole = await guild.create_role(name="Muted")
        for channel in guild.channels:
            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False, connect=False)
    await member.add_roles(mutedRole, reason=reason)
    embed = discord.Embed(title=f" Shoma mute shodid (** {member.name} **) Be dalil : ( ||**{reason}**|| ) 💀", colour=random.choice(colors))
    await cdv.send(embed=embed)
    embed = discord.Embed(title=f" Shoma az Server : ( **{guild.name}** ) mute shodid , Be dalil : ( **{reason}** ) 💀", colour=random.choice(colors))
    await member.send(embed=embed)

#mute server


@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    embed = discord.Embed(title=f" Shoma az Server : ( ||**{ctx.guild.name}**|| ) Be Dalil ( **{reason}** ) Kick Shodid! ", colour=random.choice(colors))
    await member.send(embed=embed)
    embed = discord.Embed(title=f" Karbar ( {member.name} ) az Server Be dalil : ( ||{reason}|| ) Kick shod!", colour=random.choice(colors))
    await ctx.send(embed=embed)


#kick server


@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    embed = discord.Embed(title=f" Shoma az Server  : ( **||{ctx.guild.name}||** ) Ban Shodid , Be dalil : ( **{reason}** ) 💀", colour=random.choice(colors))
    await member.send(embed=embed)
    embed = discord.Embed(title=f" Karbar  : ( **{member.name}** ) az Server Ban Shod , Be dalil : ( **||{reason}||** ) 💀", colour=random.choice(colors))
    await ctx.send(embed=embed)



#ban server



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
     embed = discord.Embed(
       title="Command Not Found!",
       colour=random.choice(colors),
       description="dastor yaft nashod"
      )
     embed.set_footer(text="az (help) estefade konid!")
     await ctx.reply(embed=embed)


# command not found


@client.command()
@commands.has_permissions(administrator=True)
async def warn(ctx,member: discord.Member,*,result=None):
    authorm = ctx.message.author
    embed = discord.Embed(
      title = ":warning:",
      colour=random.choice(colors),
      description=f"Warn Be ( **{member}** ) Be Dalil ( **{result}** ) Dadeshod! :no_entry_sign:"
      )
    await ctx.reply(embed=embed)
    embed = discord.Embed(
      title = ":warning:",
      colour=random.choice(colors),
      description = f"Shoma Tavasot ( **{authorm}** ) Be Dalil ( **{result}** ) Warn Gereftid! :no_entry_sign:"
      )
    await member.send(embed=embed)

#warn dadan




@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=100):
    mention = ctx.author.mention
    await ctx.channel.purge(limit=amount)
    my_embed = discord.Embed(title=f'{amount} Message Deleted ✅', description=f'\n\n **💌 By :** {mention}', colour=random.choice(colors))
    my_embed.set_thumbnail(
        url=ctx.guild.icon_url)
    my_embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
    await ctx.send(embed=my_embed)


@client.command()
async def avatar(ctx, member: discord.Member=None):
    if member == None:
        member = ctx.author
    icon_url = member.avatar_url

    avatarEmbed = discord.Embed(title = f"{member.name}\'s avatar ", colour=random.choice(colors))

    avatarEmbed.set_image(url = f"{icon_url}")

    avatarEmbed.timestamp = ctx.message.created_at

    await ctx.send(embed = avatarEmbed)  

# pak kardn payam ha = $clear



@client.command(aliases=["logout"])
@commands.has_permissions(administrator=True)
async def shutdown(ctx):
    embed1 = discord.Embed(colour=random.choice(colors),description=f"**Bot Shutdowned by** {ctx.author.mention} ")
    embed1.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
    await ctx.send(embed=embed1)
    await client.logout()

@client.command(aliases=["kobs"])
@commands.has_permissions(administrator=True)
async def restart(ctx):
    embed = discord.Embed(colour=random.choice(colors),description=f"**Bot restarted by** {ctx.author.mention} ")
    embed.set_footer(text=ctx.guild.name, icon_url=ctx.guild.icon_url)
    await ctx.send(embed=embed)
    os.system('cd /home/root1/Desktop/')
    os.system('python3 inferno-rp.py')

@client.command()
async def dmsend(cdv, member: discord.Member,*, res):
    embed = discord.Embed(colour=random.choice(colors),description=f"**Dm Send To** : {member.mention}")
    await cdv.send(embed=embed)
    await member.send(res)       
   
@client.command()
async def datauser(ctx, member: discord.Member):
    created_at = member.created_at.strftime("%b %d, %Y")
    embed = discord.Embed(colour=random.choice(colors),description=f"**Account Created In** {created_at} ")
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    embed = discord.Embed(colour=random.choice(colors),description=f' Ping client Is :{round(client.latency * 1000)}MS')
    await ctx.send(embed=embed)

@client.command(pass_content=True, aliases=['s'])
@commands.has_permissions(administrator=True) 
async def announce(ctx, *, text):
    
    try:
        await ctx.message.delete()
        timenow = time.strftime("%H:%M")
        embed=discord.Embed(title="𝐢𝐧𝐟𝐞𝐫𝐧𝐨 𝐑𝐏t", description=" ", color=random.choices(colors))
        embed.set_author(name="**Announcement**", icon_url=CONFIG.URl)
        embed.set_thumbnail(url=ctx.message.author.avatar_url)
        embed.add_field(name="Message:", value=text, inline=False)
        embed.set_footer(text=f"Message By : {ctx.author.mention} {timenow}")
        await ctx.send(embed=embed)
    except Exception as err:
        print(err)

@client.command()
async def help(ctx):
    embed = discord.Embed(title="𝐢𝐧𝐟𝐞𝐫𝐧𝐨 𝐑𝐏",descriptiob=f"Prefix : {CONFIG.PREFIX}",colour=random.choice(colors))
    embed.set_thumbnail(url=CONFIG.URl)
    embed.set_footer(text="𝐢𝐧𝐟𝐞𝐫𝐧𝐨 𝐑𝐏 | Developer : ! 001ᴿᶻ#0001", icon_url=CONFIG.URl)
    embed.add_field(name="lock", value="```lock kardan```", inline=True)
    embed.add_field(name="unlock", value="```unlock kardan```", inline=True)
    embed.add_field(name="ban", value="```ban kardan```", inline=True)
    embed.add_field(name="mute", value="```mute kardan```", inline=True)
    embed.add_field(name="unmute", value="```unmute kardan```", inline=True)
    embed.add_field(name="kick", value="```kick kardan```", inline=True)
    embed.add_field(name="warn", value="```warn dadan```", inline=True)
    embed.add_field(name="clear", value="```pak kardan payam```", inline=True)
    embed.add_field(name="user", value="```didan User info```", inline=True)
    embed.add_field(name="avatar", value="```didan avatar memeber```", inline=True)
    embed.add_field(name="restart", value="```baray restart dadan bot```", inline=True)
    embed.add_field(name="shutdown", value="```baray shutdown kardan bot```", inline=True)
    embed.add_field(name="dmsend", value="```baray ferestadan payam az taraf bot bara member```", inline=True)
    embed.add_field(name="dateuser", value="```baray didan time discord user```", inline=True)
    embed.add_field(name="ping", value="```baray didan ping bot```", inline=True)
    await ctx.send(embed=embed)



@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed = discord.Embed(
        description=f"{error}",
        colour=random.choice(colors)
        )
        await ctx.reply(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed = discord.Embed(
        description=f"{error}",
        colour=random.choice(colors)
        )
        await ctx.reply(embed=embed)
    if isinstance(error, commands.CommandNotFound):
        embed = discord.Embed(
        description=f"{error}",
        colour=random.choice(colors)
        )
        await ctx.reply(embed=embed)
    if isinstance(error, commands.BotMissingPermissions):
        embed = discord.Embed(
        description=f"{error}",
        colour=random.choice(colors)
        )
        await ctx.reply(embed=embed)
    if isinstance(error, commands.MemberNotFound):
        embed = discord.Embed(
        description=f"{error}",
        colour=random.choice(colors)
        )
        await ctx.reply(embed=embed)

@tasks.loop()
async def live_status(seconds=30):
    pcount = pc()
    Dis = client.get_guild(CONFIG.guildID) #Int

    activity = discord.Activity(type=discord.ActivityType.watching, name=f'🐌 {pcount}/64')
    await client.change_presence(activity=activity)
    await asyncio.sleep(15)

    activity = discord.Activity(type=discord.ActivityType.watching, name=f'👥 {Dis.member_count}')
    await client.change_presence(activity=activity)
    await asyncio.sleep(15)

client.run(CONFIG.TOKEN)
