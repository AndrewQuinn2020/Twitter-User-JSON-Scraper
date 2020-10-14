# Twitter User JSON Scraper

A very simple CLI that goes through a list of Twitter usernames and downloads basic JSON data about them.

# Usage

Clone this into a GitHub directory, and run it like so:

```bash
$ python scrape.py jack
WARNING:root:User JSON file directory doesn't exist - attempting to create @ /........here.........../TenTweetsFrom/user_jsons/
$ head user_jsons/jack__2020_10_14-20_59_09.json 
{
    "contributors_enabled": false,
    "created_at": "Tue Mar 21 20:50:14 +0000 2006",
    "default_profile": false,
    "default_profile_image": false,
    "description": "#bitcoin",
    "entities": {
        "description": {
            "urls": []
        }
$ 
```

# Command-Line Options

```bash
$ python scrape.py -h
usage: scrape.py [-h] [-v] [-q] U [U ...]

Download JSON data about one,or many, Twitter usernames, and tossesthem into ./user_jsons/.

positional arguments:
  U              A Twitter username, without the leading `@`.

optional arguments:
  -h, --help     show this help message and exit
  -v, --verbose  Set verbosity based on number of `v`s. `-v` = critical errors only; `-vvv` = default; `-vvvvv` = debug mode.
  -q, --quiet    All debug and error messages off. Overrides `-v`.
```

```bash
$ python scrape.py jack
WARNING:root:User JSON file directory doesn't exist - attempting to create @ /........here.........../TenTweetsFrom/user_jsons/
$ head user_jsons/jack__2020_10_14-20_59_09.json 
{
    "contributors_enabled": false,
    "created_at": "Tue Mar 21 20:50:14 +0000 2006",
    "default_profile": false,
    "default_profile_image": false,
    "description": "#bitcoin",
    "entities": {
        "description": {
            "urls": []
        }
$ 
```

# Example File Output
```json
{
    "contributors_enabled": false,
    "created_at": "Tue Mar 21 20:50:14 +0000 2006",
    "default_profile": false,
    "default_profile_image": false,
    "description": "#bitcoin",
    "entities": {
        "description": {
            "urls": []
        }
    },
    "favourites_count": 30380,
    "follow_request_sent": false,
    "followers_count": 4795615,
    "following": false,
    "friends_count": 4529,
    "geo_enabled": true,
    "has_extended_profile": true,
    "id": 12,
    "id_str": "12",
    "is_translation_enabled": false,
    "is_translator": false,
    "lang": null,
    "listed_count": 27827,
    "location": "",
    "name": "jack",
    "notifications": false,
    "profile_background_color": "EBEBEB",
    "profile_background_image_url": "http://abs.twimg.com/images/themes/theme7/bg.gif",
    "profile_background_image_url_https": "https://abs.twimg.com/images/themes/theme7/bg.gif",
    "profile_background_tile": false,
    "profile_banner_url": "https://pbs.twimg.com/profile_banners/12/1584998840",
    "profile_image_url": "http://pbs.twimg.com/profile_images/1115644092329758721/AFjOr-K8_normal.jpg",
    "profile_image_url_https": "https://pbs.twimg.com/profile_images/1115644092329758721/AFjOr-K8_normal.jpg",
    "profile_link_color": "990000",
    "profile_location": null,
    "profile_sidebar_border_color": "DFDFDF",
    "profile_sidebar_fill_color": "F3F3F3",
    "profile_text_color": "333333",
    "profile_use_background_image": true,
    "protected": false,
    "screen_name": "jack",
    "status": {
        "contributors": null,
        "coordinates": null,
        "created_at": "Wed Oct 14 20:44:59 +0000 2020",
        "entities": {
            "hashtags": [
                {
                    "indices": [
                        107,
                        115
                    ],
                    "text": "EndSARS"
                }
            ],
            "symbols": [],
            "urls": [],
            "user_mentions": [
                {
                    "id": 16684243,
                    "id_str": "16684243",
                    "indices": [
                        3,
                        15
                    ],
                    "name": "Karen Attiah",
                    "screen_name": "KarenAttiah"
                }
            ]
        },
        "favorite_count": 0,
        "favorited": false,
        "geo": null,
        "id": 1316480141367934977,
        "id_str": "1316480141367934977",
        "in_reply_to_screen_name": null,
        "in_reply_to_status_id": null,
        "in_reply_to_status_id_str": null,
        "in_reply_to_user_id": null,
        "in_reply_to_user_id_str": null,
        "is_quote_status": false,
        "lang": "en",
        "place": null,
        "retweet_count": 1847,
        "retweeted": false,
        "retweeted_status": {
            "contributors": null,
            "coordinates": null,
            "created_at": "Wed Oct 14 13:21:57 +0000 2020",
            "entities": {
                "hashtags": [
                    {
                        "indices": [
                            90,
                            98
                        ],
                        "text": "EndSARS"
                    }
                ],
                "symbols": [],
                "urls": [
                    {
                        "display_url": "twitter.com/i/web/status/1\u2026",
                        "expanded_url": "https://twitter.com/i/web/status/1316368647024238593",
                        "indices": [
                            117,
                            140
                        ],
                        "url": "https://t.co/EBLC4yGRJR"
                    }
                ],
                "user_mentions": []
            },
            "favorite_count": 1371,
            "favorited": false,
            "geo": null,
            "id": 1316368647024238593,
            "id_str": "1316368647024238593",
            "in_reply_to_screen_name": null,
            "in_reply_to_status_id": null,
            "in_reply_to_status_id_str": null,
            "in_reply_to_user_id": null,
            "in_reply_to_user_id_str": null,
            "is_quote_status": false,
            "lang": "en",
            "place": null,
            "possibly_sensitive": false,
            "retweet_count": 1847,
            "retweeted": false,
            "source": "<a href=\"https://mobile.twitter.com\" rel=\"nofollow\">Twitter Web App</a>",
            "text": "The largest black nation on earth is rising up against police brutality. \n\n Why Nigeria's #EndSARS campaign matters\u2026 https://t.co/EBLC4yGRJR",
            "truncated": true
        },
        "source": "<a href=\"http://twitter.com/download/iphone\" rel=\"nofollow\">Twitter for iPhone</a>",
        "text": "RT @KarenAttiah: The largest black nation on earth is rising up against police brutality. \n\n Why Nigeria's #EndSARS campaign matters for Am\u2026",
        "truncated": false
    },
    "statuses_count": 27235,
    "time_zone": null,
    "translator_type": "regular",
    "url": null,
    "utc_offset": null,
    "verified": true
}
```
