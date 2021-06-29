import discord
import random
from discord.ext import commands
from discord.utils import get

bot = commands.Bot(command_prefix='/')


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    if message.content.lower().startswith('hello'):
        await message.channel.send('Hi There!')
    await bot.process_commands(message)


@bot.command(name='ping')
async def ping(ctx):
    await ctx.send(f'pong!\n{round(bot.latency * 1000)}ms')


@bot.command(name='8ball')
async def _8ball(ctx, *, question):
    responses = ['It is Certain.', 'It is decidedly so.', 'Without a doubt.', 'Yes definitely.', 'You may rely on it.',
                 'As I see it, yes.', 'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
                 'Reply hazy, try again.', 'Ask again later.', 'Better not tell you now.', 'Cannot predict now.',
                 'Concentrate and ask again.', "Don't count on it.", 'My reply is no.', 'My sources say no.',
                 'Outlook not so good.', 'Very doubtful.']
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


@bot.command(name='verify')
async def verify(ctx):
    verified = discord.utils.get(ctx.guild.roles, name="The Mansion's Residents")
    unverified = discord.utils.get(ctx.guild.roles, name="Visitor of the Mansion")
    unvmember = ctx.author
    if verified in unvmember.roles:
        return
    else:
        await unvmember.add_roles(verified)
        await ctx.message.delete()
        await unvmember.remove_roles(unverified)


@bot.command(name='playfata')
async def playfata(ctx):
    member = ctx.author
    _reading = discord.utils.get(ctx.guild.roles, name="Currently Reading")
    finished = discord.utils.get(ctx.guild.roles, name="Finished Reading")
    fataoverwrites = {
        discord.utils.get(ctx.guild.roles, name="Visitor of the Mansion"): discord.PermissionOverwrite(
            read_messages=False),
        discord.utils.get(ctx.guild.roles, name="The Mansion's Residents"): discord.PermissionOverwrite(
            read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Currently Reading"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Reading"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Reading Requiem"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Requiem"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Reading Reincarnation"): discord.PermissionOverwrite(
            read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Reincarnation"): discord.PermissionOverwrite(
            read_messages=True),
        member: discord.PermissionOverwrite(manage_channels=True),
        discord.utils.get(ctx.guild.roles, name="Visitor of the Mansion"): discord.PermissionOverwrite(
            send_messages=False),
        discord.utils.get(ctx.guild.roles, name="The Mansion's Residents"): discord.PermissionOverwrite(
            send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Currently Reading"): discord.PermissionOverwrite(send_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Reading"): discord.PermissionOverwrite(send_messages=True),
        discord.utils.get(ctx.guild.roles, name="Reading Requiem"): discord.PermissionOverwrite(send_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Requiem"): discord.PermissionOverwrite(send_messages=True),
        discord.utils.get(ctx.guild.roles, name="Reading Reincarnation"): discord.PermissionOverwrite(
            send_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Reincarnation"): discord.PermissionOverwrite(
            send_messages=True)
    }
    if _reading in member.roles:
        await ctx.reply("You are already reading The House In Fata Morgana")
        return
    if finished in member.roles:
        await ctx.reply("You have already finished reading The House In Fata Morgana")
        return
    else:
        await member.add_roles(_reading)
        await ctx.reply("You are now reading The House In Fata Morgana"
                        "\nHope you enjoy your playthrough!")
        fatachannel = ctx.author.name + "-door-1"
        activefata = discord.utils.get(ctx.guild.categories, name="active fata read-throughs")
        channel = await ctx.guild.create_text_channel(name=fatachannel, overwrites=fataoverwrites, category=activefata)
        await channel.send(member.mention)
        await channel.send('Welcome to your The House in Fata Morgana playthrough channel!'
                           '\nHere you can discuss your opinions without worrying about spoilers')


@bot.command(name='playrequiem')
async def playrequiem(ctx):
    member = ctx.author
    _readingrequiem = discord.utils.get(ctx.guild.roles, name="Reading Requiem")
    finishedrequiem = discord.utils.get(ctx.guild.roles, name="Finished Requiem")
    requiemoverwrites = {
        discord.utils.get(ctx.guild.roles, name="Visitor of the Mansion"): discord.PermissionOverwrite(
            read_messages=False),
        discord.utils.get(ctx.guild.roles, name="The Mansion's Residents"): discord.PermissionOverwrite(
            read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Currently Reading"): discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Finished Reading"): discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Reading Requiem"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Requiem"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Reading Reincarnation"): discord.PermissionOverwrite(
            read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Reincarnation"): discord.PermissionOverwrite(
            read_messages=True),
        member: discord.PermissionOverwrite(manage_channels=True),
        discord.utils.get(ctx.guild.roles, name="Visitor of the Mansion"): discord.PermissionOverwrite(
            send_messages=False),
        discord.utils.get(ctx.guild.roles, name="The Mansion's Residents"): discord.PermissionOverwrite(
            send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Currently Reading"): discord.PermissionOverwrite(send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Finished Reading"): discord.PermissionOverwrite(send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Reading Requiem"): discord.PermissionOverwrite(send_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Requiem"): discord.PermissionOverwrite(send_messages=True),
        discord.utils.get(ctx.guild.roles, name="Reading Reincarnation"): discord.PermissionOverwrite(
            send_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Reincarnation"): discord.PermissionOverwrite(
            send_messages=True)
    }
    if _readingrequiem in member.roles:
        await ctx.reply("You are already reading The House in Fata Morgana: A Requiem for Innocence")
        return
    if finishedrequiem in member.roles:
        await ctx.reply("You have already finished reading The House in Fata Morgana: A Requiem for Innocence")
        return
    else:
        await member.add_roles(_readingrequiem)
        await ctx.reply("You are now reading The House in Fata Morgana: A Requiem for Innocence"
                        "\nHope you enjoy your playthrough!")
        requiemchannel = ctx.author.name + "-requiem"
        activerequiem = discord.utils.get(ctx.guild.categories, name="active requiem read-throughs")
        channel = await ctx.guild.create_text_channel(name=requiemchannel, overwrites=requiemoverwrites,
                                                      category=activerequiem)
        await channel.send(member.mention)
        await channel.send('Welcome to your The House in Fata Morgana: Requiem playthrough channel!'
                           '\nHere you can discuss your opinions without worrying about spoilers')


@bot.command(name='playreincarnation')
async def playreincarnation(ctx):
    member = ctx.author
    _readingreincarnation = discord.utils.get(ctx.guild.roles, name="Reading Reincarnation")
    finishedreincarnation = discord.utils.get(ctx.guild.roles, name="Finished Reincarnation")
    reincarnationoverwrites = {
        discord.utils.get(ctx.guild.roles, name="Visitor of the Mansion"): discord.PermissionOverwrite(
            read_messages=False),
        discord.utils.get(ctx.guild.roles, name="The Mansion's Residents"): discord.PermissionOverwrite(
            read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Currently Reading"): discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Finished Reading"): discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Reading Requiem"): discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Finished Requiem"): discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Reading Reincarnation"): discord.PermissionOverwrite(
            read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Reincarnation"): discord.PermissionOverwrite(
            read_messages=True),
        member: discord.PermissionOverwrite(manage_channels=True),
        discord.utils.get(ctx.guild.roles, name="Visitor of the Mansion"): discord.PermissionOverwrite(
            send_messages=False),
        discord.utils.get(ctx.guild.roles, name="The Mansion's Residents"): discord.PermissionOverwrite(
            send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Currently Reading"): discord.PermissionOverwrite(send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Finished Reading"): discord.PermissionOverwrite(send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Reading Requiem"): discord.PermissionOverwrite(send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Finished Requiem"): discord.PermissionOverwrite(send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Reading Reincarnation"): discord.PermissionOverwrite(
            send_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Reincarnation"): discord.PermissionOverwrite(
            send_messages=True)
    }
    if _readingreincarnation in member.roles:
        await ctx.reply("You are already reading The House in Fata Morgana: Reincarnation")
        return
    if finishedreincarnation in member.roles:
        await ctx.reply("You have already finished reading The House in Fata Morgana: Reincarnation")
        return
    else:
        await member.add_roles(_readingreincarnation)
        await ctx.reply("You are now reading The House in Fata Morgana: Reincarnation"
                        "\nHope you enjoy your playthrough!")
        reincarnationchannel = ctx.author.name + "-door-1-reincarnation"
        activereincarnation = discord.utils.get(ctx.guild.categories, name="active reincarnation read-throughs")
        channel = await ctx.guild.create_text_channel(name=reincarnationchannel, overwrites=reincarnationoverwrites,
                                                      category=activereincarnation)
        await channel.send(member.mention)
        await channel.send('Welcome to your The House in Fata Morgana: Reincarnation playthrough channel!'
                           '\nHere you can discuss your opinions without worrying about spoilers')


@bot.command(name="pause")
@commands.has_permissions(manage_channels=True)
async def pause(ctx):
    paused = discord.utils.get(ctx.guild.channels, name="paused read-throughs")
    await ctx.channel.edit(category=paused)


@bot.command(name="continuetorequiem")
@commands.has_permissions(manage_channels=True)
async def continuetorequiem(ctx):
    activefata = discord.utils.get(ctx.guild.channels, name="active fata read-throughs")
    activerequiem = discord.utils.get(ctx.guild.channels, name="active requiem read-throughs")
    member = ctx.message.author
    requiemoverwritesre = {
        discord.utils.get(ctx.guild.roles, name="Visitor of the Mansion"): discord.PermissionOverwrite(
            read_messages=False),
        discord.utils.get(ctx.guild.roles, name="The Mansion's Residents"): discord.PermissionOverwrite(
            read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Currently Reading"): discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Finished Reading"): discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Reading Requiem"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Requiem"): discord.PermissionOverwrite(read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Reading Reincarnation"): discord.PermissionOverwrite(
            read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Reincarnation"): discord.PermissionOverwrite(
            read_messages=True),
        member: discord.PermissionOverwrite(manage_channels=True),
        discord.utils.get(ctx.guild.roles, name="Visitor of the Mansion"): discord.PermissionOverwrite(
            send_messages=False),
        discord.utils.get(ctx.guild.roles, name="The Mansion's Residents"): discord.PermissionOverwrite(
            send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Currently Reading"): discord.PermissionOverwrite(send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Finished Reading"): discord.PermissionOverwrite(send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Reading Requiem"): discord.PermissionOverwrite(send_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Requiem"): discord.PermissionOverwrite(send_messages=True),
        discord.utils.get(ctx.guild.roles, name="Reading Reincarnation"): discord.PermissionOverwrite(
            send_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Reincarnation"): discord.PermissionOverwrite(
            send_messages=True)
    }
    await ctx.channel.edit(category=activerequiem, overwrites=requiemoverwritesre)


@bot.command(name="continuetoreincarnation")
@commands.has_permissions(manage_channels=True)
async def continuetoreincarnation(ctx):
    activerequiem = discord.utils.get(ctx.guild.channels, name="active requiem read-throughs")
    member = ctx.message.author
    reincarnationoverwritesre = {
        discord.utils.get(ctx.guild.roles, name="Visitor of the Mansion"): discord.PermissionOverwrite(
            read_messages=False),
        discord.utils.get(ctx.guild.roles, name="The Mansion's Residents"): discord.PermissionOverwrite(
            read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Currently Reading"): discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Finished Reading"): discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Reading Requiem"): discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Finished Requiem"): discord.PermissionOverwrite(read_messages=False),
        discord.utils.get(ctx.guild.roles, name="Reading Reincarnation"): discord.PermissionOverwrite(
            read_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Reincarnation"): discord.PermissionOverwrite(
            read_messages=True),
        member: discord.PermissionOverwrite(manage_channels=True),
        discord.utils.get(ctx.guild.roles, name="Visitor of the Mansion"): discord.PermissionOverwrite(
            send_messages=False),
        discord.utils.get(ctx.guild.roles, name="The Mansion's Residents"): discord.PermissionOverwrite(
            send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Currently Reading"): discord.PermissionOverwrite(send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Finished Reading"): discord.PermissionOverwrite(send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Reading Requiem"): discord.PermissionOverwrite(send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Finished Requiem"): discord.PermissionOverwrite(send_messages=False),
        discord.utils.get(ctx.guild.roles, name="Reading Reincarnation"): discord.PermissionOverwrite(
            send_messages=True),
        discord.utils.get(ctx.guild.roles, name="Finished Reincarnation"): discord.PermissionOverwrite(
            send_messages=True)
    }
    await ctx.channel.edit(category=activerequiem, overwrites=reincarnationoverwritesre)


@bot.command(name="finishedfata")
async def finishedfata(ctx):
    member = ctx.author
    finished = discord.utils.get(ctx.guild.roles, name="Finished Reading")
    _reading = discord.utils.get(ctx.guild.roles, name="Currently Reading")
    if finished in member.roles:
        await ctx.reply("You already have the 'Finished Playing' role")
        return
    if _reading in member.roles:
        await member.remove_roles(_reading)
        await member.add_roles(finished)
        await ctx.reply("Hope you enjoyed your playthrough of The House in Fata Morgana!"
                        "\nYou now have access to the spoiler channels")
        return
    else:
        await member.add_roles(finished)
        await ctx.reply("Hope you enjoyed your playthrough of The House in Fata Morgana!"
                        "\nYou now have access to the spoiler channels")


@bot.command(name="finishedrequiem")
async def finishedrequiem(ctx):
    member = ctx.author
    _reading = discord.utils.get(ctx.guild.roles, name="Currently Reading")
    _readingrequiem = discord.utils.get(ctx.guild.roles, name="Reading Requiem")
    finishedrequiem = discord.utils.get(ctx.guild.roles, name="Finished Requiem")
    if finishedrequiem in member.roles:
        await ctx.reply("You already have the 'Finished Playing' role")
        return
    if _readingrequiem in member.roles:
        await member.remove_roles(_readingrequiem)
        await member.add_roles(finishedrequiem)
        await member.remove_roles(_reading)
        await ctx.reply("Hope you enjoyed your playthrough of The House in Fata Morgana: A Requiem for Innocence!"
                        "\nYou now have access to the spoiler channels")
        return
    if _reading  in member.roles:
        await member.remove_roles(_readingrequiem)
        await member.add_roles(finishedrequiem)
        await ctx.reply("Hope you enjoyed your playthrough of The House in Fata Morgana: A Requiem for Innocence!"
                        "\nYou now have access to the spoiler channels")
        return
    else:
        await member.add_roles(finishedrequiem)
        await ctx.reply("Hope you enjoyed your playthrough of The House in Fata Morgana: A Requiem for Innocence!"
                        "\nYou now have access to the spoiler channels")


@bot.command(name="finishedreincarnation")
async def finishedreincarnation(ctx):
    member = ctx.author
    _readingreincarnation = discord.utils.get(ctx.guild.roles, name="Reading Reincarnation")
    finishedreincarnation = discord.utils.get(ctx.guild.roles, name="Finished Reincarnation")
    if finishedreincarnation in member.roles:
        await ctx.reply("You already have the 'Finished Playing' role")
        return
    if _readingreincarnation in member.roles:
        await member.remove_roles(_readingreincarnation)
        await member.add_roles(finishedreincarnation)
        await ctx.reply("Hope you enjoyed your playthrough of The House in Fata Morgana: Reincarnation!"
                        "\nYou now have access to the spoiler channels")
        return
    else:
        await member.add_roles(finishedreincarnation)
        await ctx.reply("Hope you enjoyed your playthrough of The House in Fata Morgana: Reincarnation!"
                        "\nYou now have access to the spoiler channels")


bot.run(<BOT TOKEN HERE>)
