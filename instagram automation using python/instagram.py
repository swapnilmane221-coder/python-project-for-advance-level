from instabot import Bot
bot=Bot()
bot.login(username="******",password='*****')
bot.follow("wscubetechindia")
bot.upload_photo('"D:\python-project-for-advance-level\QR code\chhava_song.png"',caption="I love python")
bot.unfollow("wscubetechindia")
bot.send_message("hii",['username1','username2'])
followers=bot.get_user_followers("username")
for i in followers:
     print(bot.get_user_info(i))
following=bot.get_user_following("username")
for i in following:
     print(bot.get_user_info(i))

