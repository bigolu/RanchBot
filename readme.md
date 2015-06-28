# Ranch Bot
A bot on DigitalOcean that makes daily wall posts to the R a n c h Facebook page.

First, it searches tumblr for ranch related pictures.

Next, it gets a random quote using the
<a href="http://quotesondesign.com/" target="_blank">quotesondesign</a>
api and processes it using the
<a href="http://www.nltk.org/" target="_blank">Natural Language Toolkit</a>
to replace any and all nouns with ranch

 And finally it combines the two to make a wall post.


##Making posts to a facebook page
To make a post to a page you ar an admin of, you will need to get a series of short-lived tokens which ultimately lead you to a never-expiring token. Rather than do all of that, you can just use the get_token.py script in this repo, here's how:

1. Create a Facebook app

2. Open the config-example.py file and replace your_id and your_secret with your app id and secret. Then rename the file to config.py

3. Next, go to to the Facebook Graph API Explorer and select your app on the dropdown next to Application. Then click get access token. When the permissions page pops up, be sure to check off manage_pages under the extended permissions.

4. Once you have the token, run get_token.py along with your token and the name of your page, and the permenant token will generated into the file perm_token.cfg.

Example:
![alt tag](https://raw.githubusercontent.com/biggie96/RanchBot/master/example.png)

*To make use of the token check out an SDK in the language of your choice:
- <a href="https://developers.facebook.com/docs/javascript" target="_blank">Javascript</a>
- <a href="https://developers.facebook.com/docs/ios" target="_blank">iOS</a>
- <a href="https://developers.facebook.com/docs/android" target="_blank">Android</a>
- <a href="https://developers.facebook.com/docs/reference/php/4.0.0" target="_blank">PHP</a>
- <a href="https://developers.facebook.com/docs/unity" target="_blank">Unity</a>
- <a href="http://facebook-sdk.readthedocs.org/en/latest/" target="_blank">Python</a>
