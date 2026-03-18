# DND Availability Bot

A Discord bot that automatically posts a weekly availability poll for your D&D group. Members can vote on which days they're free using interactive buttons, and the results update in real time.

---

## Features

- 📅 **Weekly auto-poll** — Automatically sends a new availability poll every 7 days
- 🖱️ **Interactive buttons** — Members vote with one click; clicking again removes their vote
- 📊 **Live results** — The embed updates instantly as votes come in
- 📣 **Role mention** — Pings the `dnd` role so no one misses the poll

---

## Prerequisites

- Python 3.8+
- A Discord bot token ([Discord Developer Portal](https://discord.com/developers/applications))
- The bot added to your server with the following permissions:
  - Send Messages
  - Embed Links
  - Read Message History
  - Mention Roles

---

## Setup

1. **Clone the repo**
   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo
   ```

2. **Install dependencies**
   ```bash
   pip install discord.py python-dotenv
   ```

3. **Create your environment file**

   Create a file named `key.env` in the project root:
   ```env
   DISCORD_TOKEN=your_discord_bot_token_here
   ```

4. **Configure the bot**

   In `bot.py`, update the following:
   ```python
   channel_id = YOUR_CHANNEL_ID   # The channel where polls will be posted
   ```
   To get a channel ID, enable Developer Mode in Discord settings, then right-click the channel and select **Copy ID**.

   Also make sure your server has a role named exactly `dnd` — this is the role that gets pinged with each poll.

5. **Run the bot**
   ```bash
   python bot.py
   ```

---

## Usage

Once the bot is running, it will:

1. Send the first poll immediately when it comes online
2. Automatically post a new poll every **168 hours (7 days)**
3. Each poll has buttons for all 7 days of the week plus an **IDK** option

Members can click a day to vote, and click it again to unvote. The vote count updates live for everyone.

---

## .gitignore

Make sure your `.gitignore` includes:
```
key.env
```

---

## Dependencies

| Package | Purpose |
|---|---|
| `discord.py` | Discord API wrapper |
| `python-dotenv` | Load environment variables from `.env` file |

---

## Notes

- The bot must remain running continuously for the weekly loop to work. Consider hosting it on a service, personal VPS, or on a rasberryPI.
- The poll does **not** persist across bot restarts — votes are stored in memory only.
