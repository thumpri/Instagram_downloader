import instaloader
import os
import sys




directory = sys.argv[1]

parent_dir = '/Users/priyanshisharma/Desktop/Instart'

path = os.path.join(parent_dir, directory)

bot = instaloader.Instaloader(dirname_pattern=path, download_videos=False, download_video_thumbnails=False, save_metadata=False, post_metadata_txt_pattern='')


bot.login('', '') 

profile = instaloader.Profile.from_username(bot.context, directory)

# Get all posts in a generator object
posts = profile.get_posts()

# Iterate and download
for index, post in enumerate(posts, 1):
    bot.download_post(post, target=f"{profile.username}_{index}")



image = '/Users/priyanshisharma/Downloads/IMG_0034.PNG'
text = 'What do you relate with the most?' + '\r\n' + ' Write-up - @verymanymusings ' + '\r\n' + 'Original visual art - @andreysamarin ' + '\r\n' + 'Edited by me using - @procreate ' + '\r\n' + '#deadbody #poetry #poemssayitall #100daysofpoetry'

