import datetime
import os

import discord
import requests
from dotenv import load_dotenv

from constants import ACT_COLORS, ZONE_INFO

load_dotenv()

API_BASE_URL = os.environ.get(
    "API_BASE_URL", "https://d2runewizard.com/api/terror-zone"
)


def get_terror_zone_json(auth_token):
    """
    {
        terrorZone: {
            lastReportedBy: {
                displayName: String;
                uid: String;
            };
            lastUpdate: {
                seconds: number;
                nanoseconds: number;
            };
            reportedZones: {
                [zone: string]: number;
            };
            highestProbabilityZone: {
                zone: String;
                act: String;
                amount: number;
                probability: number;
            };
        };
        providedBy: "https://d2runewizard.com/terror-zone-tracker"
    }
    """
    params = {"token": auth_token}
    headers = {"User-Agent": "d2terror-discord"}
    response = requests.get(API_BASE_URL, params=params, headers=headers)
    return response.json() if response.status_code == 200 else {}


def get_time_remaining():
    now = datetime.datetime.now()
    one_hour_ahead = now + datetime.timedelta(hours=1)
    next_zone_time = one_hour_ahead.replace(minute=0, second=0, microsecond=0)
    return next_zone_time - now


class D2Terror(discord.Client):
    def __init__(self, get_token, *, intents: discord.Intents):
        super().__init__(intents=intents)
        self.get_token = get_token
        self.cache = {}
        self.command_tree = discord.app_commands.CommandTree(self)

    async def setup_hook(self):
        await self.command_tree.sync()

    def update_terror_zone_cache(self):
        terror_zone_json = get_terror_zone_json(self.get_token)
        self.cache = terror_zone_json
        return terror_zone_json

    def terror_zone_info(self):
        if "terrorZone" not in self.cache:
            raise AttributeError("Cache missing!")

        terror_zone = self.cache["terrorZone"]["highestProbabilityZone"]["zone"]
        act = self.cache["terrorZone"]["highestProbabilityZone"]["act"]
        url = self.cache.get("providedBy", "https://d2runewizard.com/")
        minutes_remaining = get_time_remaining().seconds // 60
        title = f"{terror_zone} (act {act[-1]})"

        embed = discord.Embed(
            title=title,
            url=url,
            color=ACT_COLORS.get(act, discord.Colour.blue()),
        )
        embed.add_field(
            name="Time remaining:", value=f"{minutes_remaining} min", inline=True
        )

        if terror_zone in ZONE_INFO:
            zone = ZONE_INFO[terror_zone]
            embed.add_field(
                name="Immunities:", value=", ".join(zone["immunities"]), inline=True
            )
            embed.add_field(
                name="Boss packs:",
                value=f"{zone['boss_packs'][0]} to {zone['boss_packs'][1]}",
                inline=True,
            )
            if zone["uniques"]:
                embed.add_field(
                    name="Unique monsters:",
                    value=", ".join(zone["uniques"]),
                    inline=True,
                )
            embed.add_field(name="Sparkly chests:", value=zone["chests"], inline=True)
        else:
            print(f"zone info missing: {terror_zone}")

        embed.set_footer(
            text="Powered by d2runewizard.com",
            icon_url="https://d2runewizard.com/icons/favicon-32x32.png",
        )
        return embed


if __name__ == "__main__":
    discord_token = os.environ.get("DISCORD_TOKEN")
    if not discord_token:
        print("Please set the DISCORD_TOKEN environment variable!")
        exit(1)

    d2runewizard_token = os.environ.get("D2RUNEWIZARD_TOKEN")
    if not d2runewizard_token:
        print("Please set the D2RUNEWIZARD_TOKEN environment variable!")
        exit(1)

    client = D2Terror(d2runewizard_token, intents=discord.Intents.default())

    @client.command_tree.command()
    async def terror(interaction: discord.Interaction):
        """Reports current Terror Zone"""
        client.update_terror_zone_cache()
        try:
            embed = client.terror_zone_info()
            await interaction.response.send_message(embed=embed)
        except Exception as e:
            print(e)
            await interaction.response.send_message("Data unavailable.")

    print("Starting bot...")
    client.run(discord_token)
