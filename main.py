import praw

reddit = praw.Reddit(client_id='', client_secret='', user_agent='')

hot_posts = reddit.subreddit('').hot(limit=10)
for post in hot_posts:
    print(post.title, post.content,'\n')


onclick="window.location.href='{{ url_for('index') }}