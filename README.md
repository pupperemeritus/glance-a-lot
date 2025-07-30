# Glance-A-Lot Discord Bot

Glance-A-Lot is a multi-functional Discord bot designed to provide useful information and emotional support to server members.

## Features

- **Weather Forecasts:** Get real-time weather information for any city.
- **Web Search:** Perform quick searches on Google or YouTube directly from Discord.
- **Emotion Detection:** The bot analyzes messages to detect negative emotions (sadness, anger, fear). After detecting a pattern of negative messages from a user, it offers a supportive message and suggests a fun command to help lift their spirits.
- **Welcome Messages:** Greets new members who join the server with a warm welcome message.

## Commands

- **Get Weather:**

  ```
  glance wthr <city_name>
  ```

  _Example: `glance wthr London`_

- **Search the Web:**

  ```
  glance srch <engine> <query>
  ```

  _Engines: `google`, `youtube` (or aliases like `ggl`, `yt`)_
  _Example: `glance srch google python tutorial`_

## Setup and Installation

1. **Clone the repository:**

   ```bash
   git clone https://github.com/pupperemeritus/glance-a-lot.git
   cd glance-a-lot
   ```

2. **Install dependencies:**
   _It is recommended to create a virtual environment first._

   ```bash
   pip install -r requirements.txt
   ```

3. **Create Model Files:**
   Run the `emotion_detection_model_creator.py` script to train the emotion detection model and create the `nb.pkl` and `vectorizer.pkl` files.

   ```bash
   python emotion_detection_model_creator.py
   ```

4. **Set up Environment Variables:**
   Create a `.env` file in the root directory and add your API keys:

   ```
   DISCORD_TOKEN=your_discord_bot_token
   OWM_API_KEY=your_openweathermap_api_key
   ```

5. **Database:**
   This bot uses a local MongoDB instance. Make sure you have MongoDB installed and running on `localhost:27017`. The bot will automatically create the `glancealot` database and the `userNegativeDetects` collection.

6. **Run the bot:**

   ```bash
   python glance_a_lot.py
   ```

## File Descriptions

- `glance_a_lot.py`: The main script to start the bot.
- `glance_a_lot_client.py`: Contains the core Discord client logic, event handlers (`on_message`, `on_member_join`), and command processing.
- `emotion_detection_model_creator.py`: A script to train the sentiment analysis model from a dataset.
- `emotion_detection_model_loader.py`: Loads the pre-trained model to make predictions on message content.
- `weather.py`: Handles fetching and formatting weather data from the OpenWeatherMap API.
- `search.py`: Handles search queries for Google and YouTube.
