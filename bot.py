{
    "name": "Media Search bot",
    "description": "When you going to send file on telegram channel/group this bot will save that in database, So you can search that easily in inline mode",
    "keywords": [
      "telegram",
      "best",
      "indian",
      "pyrogram",
      "media",
      "search",
      "channel",
      "index",
      "inline"
    ],
    "website": "https://github.com/Mahesh0253/Media-Search-bot",
    "repository": "https://github.com/Mahesh0253/Media-Search-bot",
    "env": {
        "BOT_TOKEN": {
            "description": "Your bot token.",
            "value": ""
        },
        "API_ID": {
            "description": "Get this value from https://my.telegram.org",
            "value": ""
        },
        "API_HASH": {
            "description": "Get this value from https://my.telegram.org",
            "value": ""
        },
        "CHANNELS": {
            "description": "Username or ID of channel or group. Separate multiple IDs by space.",
            "value": ""
        },
        "ADMINS": {
            "description": "Username or ID of Admin. Separate multiple Admins by space.",
            "value": ""
        },
        "DATABASE_URI": {
            "description": "mongoDB URI. Get this value from https://www.mongodb.com. For more help watch this video - https://youtu.be/dsuTn4qV2GA",
            "value": ""
        },
        "DATABASE_NAME": {
            "description": "Name of the database in mongoDB. For more help watch this video - https://youtu.be/dsuTn4qV2GA",
            "value": ""
        },
        "COLLECTION_NAME": {
            "description": "Name of the collections. Defaults to Telegram_files. If you going to use same database, then use different collection name for each bot",
            "value": "Telegram_files",
            "required": false
        },
        "MAX_RESULTS": {
            "description": "Maximum limit for inline search results",
            "value": "10",
            "required": false
        },
        "CACHE_TIME": {
            "description": "The maximum amount of time in seconds that the result of the inline query may be cached on the server",
            "value": "300",
            "required": false
        }
    },
    "addons": [],
    "buildpacks": [
        {
            "url": "heroku/python"
        }
    ],
    "formation": {
        "worker": {
            "quantity": 1,
            "size": "free"
        }
    }
}
