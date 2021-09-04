import discord
from discord.ext import commands
from discord.ext.commands import Bot, guild_only
import asyncio
from discord.ext.commands import Bot
from discord_components import DiscordComponents, Button, Select, SelectOption
import json

bot = Bot(command_prefix="!")


# Power
@bot.event
async def on_ready():
	print("Bot is ready!")
	activity = discord.Game(name="!start", type=3)
	await bot.change_presence(status=discord.Status.online, activity=activity)


bot.remove_command('start')
@bot.command()
async def start(ctx):
	embed = discord.Embed(color = 0xa180fa, title="Давно пора!", description="`!tik` - Стать тиктокером \n \n `!like` - Стать лайкером \n \n `!IT` - Типо умный \n \n")
	await ctx.send(embed = embed)

bot.remove_command('tik')
@bot.command()
async def tik(ctx):
	embed = discord.Embed(color = 0xa180fa, title="Соболезную, ну го", description="`!tik_create_ac` - Создать аккаунт в тиктоке \n \n`!tik_acc` `@участник` - Проверить наличие")
	await ctx.send(embed = embed)

bot.remove_command('tik_create_ac')
@bot.command()
async def tik_create_ac(ctx):
	embed = discord.Embed(color = 0xa180fa, title="Чел ты ботик?", description="`!tic_da` `@участник` `название` - Мне 9 лет, *Можно!* \n \n`!tik_da` `@участник` `название` - А чел поздно")
	await ctx.send(embed = embed)

# Warn
@bot.command()
async def tic_da(ctx, member: discord.Member, about):
	with open('userwarns.json','r', encoding='utf-8') as f:
		userwarns = json.load(f)

	if not str(member.name) in userwarns:
		userwarns[str(member.name)] = {}
		userwarns[str(member.name)]['warns'] = 1
		with open('userwarns.json','w') as f:
			json.dump(userwarns,f)

		await member.send(f'Вы создали аккаунт в тик токе! \n*Соболезную!* \n \nНазвания аккаунта: `{about}` ')

	else:
		warns = userwarns[str(member.name)]['warns']

		if warns + 1 == 3:
			await member.send(f'Вы создали аккаунт в тик токе! \n  *Соболезную!* \n \n Вы имеете аккаунтов: `3` \nНазвания аккаунта: `{about}` \n \n \nПримечание: Чел хаватит! Больше ты аккаунтов не создаешь!')

			userwarns[str(member.name)]['warns'] = 0
			with open('userwarns.json','w') as f:
				json.dump(userwarns,f)

		else:
			await member.send(f'Вы создали аккаунт в тик токе! \n  *Соболезную!* \n \n Вы имеете аккаунтов: `2` \nНазвания аккаунта: `{about}` ')
			userwarns[str(member.name)]['warns'] += 1
			with open('userwarns.json','w') as f:
				json.dump(userwarns,f)

@bot.command()
async def tik_acc(ctx, member: discord.Member):
	with open('userwarns.json','r', encoding='utf-8') as f:
		userwarns = json.load(f)

	if not str(member.name) in userwarns:
		await ctx.send(f'Участник `{member.name}` не бот, и аккаунов не имеет : )')

	else:
		warns = userwarns[str(member.name)]['warns']
		await ctx.send(f'Участник `{member}`\n Имеет аков: `{warns}`\n*Соболезную!*')

bot.remove_command('like')
@bot.command()
async def like(ctx):
	embed = discord.Embed(color = 0xff0004, title="не не не", description="Родительский контроль не позволит вам этого сделать : )\n \n А возможно это в лучшему?")
	await ctx.send(embed = embed)

bot.remove_command('IT')
@bot.command()
async def IT(ctx):
	embed = discord.Embed(color = 0x85ceff, title="Ну на, не жалко", description="```text```")
	await ctx.send(embed = embed)

bot.run("ODExOTk0Nzc5NTU0MjgzNTIw.YC6TEQ.34CGZCU8Cs8dXwmm2FLL_wMGlHQ")