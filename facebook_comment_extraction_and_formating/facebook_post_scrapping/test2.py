from facebook_scraper import get_posts

i = 1
for post in get_posts('Pureit.Bangladesh', pages=5,cookies="cookies.txt",extra_info=True):
    print(i)
    i = i +1
    print(post['text'])
    print('comments: ' + post['comments'])
    print('post_url : ' + post['post_url'])
    
    print()