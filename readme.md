# Ranch Bot
A bot that makes daily wall posts to the R a n c h Facebook page.

First, it searches tumblr for ranch related pictures and then combines it with a random quote, replacing all nouns with ranch, and finally makes a wall post.

##Making posts to a facebook page
To make a post to a page you ar an admin of, you will need to get a series of short-lived tokens which ultimately lead you to a never-expiring token. Rather than do all of that, you can just use the get_token.py script which does it for you:
1. Create a Facebook app

2. Open the config-example.py file and replace your_id and your_secret with your app id and secret. Then rename the file to config.py

3. Next, go to to the Facebook Graph API Explorer and select your app on the dropdown next to Application. Then click get access token. When the permissions page pops up, be sure to check off manage_pages under the extended permissions.

4. Once you have the token, run get_token.py along with your token and the name of your page, and the permenant token will generated into the file perm_token.cfg.
[Example](https://raw.githubusercontent.com/biggie96/RanchBot/master/example.png)

*To make use of the token check out an SDK in the language of your choice:
- [Javascript](https://developers.facebook.com/docs/javascript)
- [iOS](https://developers.facebook.com/docs/ios)
- [Android](https://developers.facebook.com/docs/android)
- [PHP](https://developers.facebook.com/docs/reference/php/4.0.0)
- [Unity](https://developers.facebook.com/docs/unity)
- [Python](http://facebook-sdk.readthedocs.org/en/latest/)
