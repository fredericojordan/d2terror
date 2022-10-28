# Diablo II: Resurrected - Terror Zone Discord Bot

[![Add to Discord](https://img.shields.io/static/v1?label=&message=Add%20to%20Discord&color=7289da&logo=discord&labelColor=424549)](https://discord.com/api/oauth2/authorize?client_id=1035556810951753889&permissions=380104756288&scope=bot) [![powered-by-d2runewizard](https://img.shields.io/badge/powered%20by-d2runewizard-green)](https://d2runewizard.com/)

This is a bot that scrapes [d2runewizard's API](https://d2runewizard.com/integration) and offers the following functionalities on Discord:

1. `!terror` command for Terror Zone tracker verification.

## Quickstart

[Click here](https://discord.com/api/oauth2/authorize?client_id=1035556810951753889&permissions=380104756288&scope=bot) to add D2 Terror Zone bot to your Discord server!

## Running the bot

You may also download the code, alter it in any fashion and run the bot on your own computer.

1. Create a [Discord Application](https://discord.com/developers/applications), enable a bot account and create its authentication token.
2. Set your token as the `DISCORD_TOKEN` environment variable by running `export DISCORD_TOKEN=YOUR_TOKEN_HERE`.
3. Download and run the bot by executing the following:
   ```shell
   git clone https://github.com/fredericojordan/d2terror.git
   cd d2terror
   python d2terror_discord.py
   ```
4. Generate an invite link and add the bot to your Discord server.
