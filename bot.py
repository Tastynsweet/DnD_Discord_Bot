import discord
from discord.ext import commands, tasks
from discord.ui import Button, View
import datetime
import os
from dotenv import load_dotenv

load_dotenv("key.env")

class PollView(View):
    def __init__(self):
        super().__init__(timeout=None)
        self.votes = {day: set() for day in ["MON", "TUE", "WED", "THR", "FRI", "SAT", "SUN", "IDK"]}

    async def handle_vote(self, interaction: discord.Interaction, day: str):
        user = interaction.user
        if user.id in self.votes[day]:
            self.votes[day].remove(user.id)
        else:
            self.votes[day].add(user.id)
        
        results = "\n".join(f"{day}: {len(voters)} votes" for day, voters in self.votes.items())

        embed = discord.Embed(title="Weekly DND Availability", description=results, color=discord.Color.red())
        
        await interaction.response.edit_message(embed=embed, view=self)

def make_poll_view():
    view = PollView()
    
    layout = [
        ["MON", "TUE", "WED", "THR"],
        ["FRI", "SAT", "SUN", "IDK"] 
    ]

    for row_index, row_days in enumerate(layout):
        for day in row_days:
            async def callback(interaction, d=day):
                await view.handle_vote(interaction, d)

            button = Button(
                label=day,
                style=discord.ButtonStyle.success,
                row=row_index   
            )
            button.callback = callback
            view.add_item(button)

    return view

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

channel_id = 1412261482980315290

@bot.event
async def on_ready():
    print(f"Bot is online as {bot.user}")
    weekly_poll.start()

@tasks.loop(hours=168)
async def weekly_poll():
    channel = bot.get_channel(channel_id)
    role = discord.utils.get(channel.guild.roles, name="dnd")
    if channel:
        embed = discord.Embed(title="Weekly DND Availability", 
                              description="\n".join(f"{day}: 0 votes" for day in ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]), 
                              color=discord.Color.green())
        
        await channel.send(f"{role.mention}", embed=embed, view=make_poll_view())
        print("Poll sent.")

# --- Run Bot ---
bot.run(os.getenv("DISCORD_TOKEN"))