import os

import discord
import requests
from dotenv import load_dotenv

load_dotenv()

API_BASE_URL = os.environ.get("API_BASE_URL", "https://d2runewizard.com/api/terror-zone")


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
            providedBy: "https://d2runewizard.com/terror-zone-tracker"
        };
    }
    """
    params = {"token": auth_token}
    headers = {"User-Agent": "d2terror-discord"}
    response = requests.get(API_BASE_URL, params=params, headers=headers)
    return response.json() if response.status_code == 200 else {}


class D2Terror(discord.Client):
    def __init__(self, get_token, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.get_token = get_token
        self.cache = {}

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content.startswith("!terror"):
            self.get_terror_zone_json()
            await message.channel.send(self.status_text())

    def get_terror_zone_json(self):
        terror_zone_json = get_terror_zone_json(self.get_token)
        self.cache = terror_zone_json
        return terror_zone_json

    def status_text(self):
        if "terrorZone" not in self.cache:
            return "Data unavailable."

        terror_zone = self.cache["terrorZone"]["highestProbabilityZone"]["zone"]
        act = self.cache["terrorZone"]["highestProbabilityZone"]["act"]
        return f"Current Terror Zone:\n{terror_zone} (Act {act})\n> Powered by d2runewizard.com"


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
    print("Starting bot...")
    client.run(discord_token)
