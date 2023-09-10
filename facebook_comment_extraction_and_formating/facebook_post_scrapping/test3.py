import requests

def get_post_comments(post_id, access_token):
    base_url = "https://graph.facebook.com/v12.0/"
    endpoint = f"{post_id}/comments"

    params = {
        "access_token": access_token,
        "fields": "message,comments{message}",
        "limit": 100,  # Change the limit as needed
    }

    comments = []

    try:
        while True:
            response = requests.get(base_url + endpoint, params=params)
            data = response.json()

            if "data" in data:
                comments.extend(data["data"])

            if "paging" in data and "next" in data["paging"]:
                next_page_url = data["paging"]["next"]
                params = None  # To get the next page, don't include "params" in the request
            else:
                break
    except requests.exceptions.RequestException as e:
        print("An error occurred while making the request:", e)

    return comments

if __name__ == "__main__":
    page_id = "Pureit.Bangladesh"  # Replace with the page ID of your friend's public page
    access_token = "37fc4464c675a37aa9ee01a98e7dac8f"  # Replace with your Facebook App access token

    # Example of getting posts from the page's feed
    base_url = f"https://graph.facebook.com/v12.0/{page_id}/feed"
    params = {
        "access_token": access_token,
        "fields": "id,message",
        "limit": 5,  # Change the limit as needed
    }
    response = requests.get(base_url, params=params)
    data = response.json()
    print(data)
    for post in data["data"]:
        post_id = post["id"]
        post_message = post.get("message", "")
        print(f"Post ID: {post_id}\nPost Message: {post_message}")

        comments = get_post_comments(post_id, access_token)
        for i, comment in enumerate(comments, start=1):
            comment_message = comment["message"]
            print(f"\tComment {i}: {comment_message}")
            
            replies = comment.get("comments", {}).get("data", [])
            for j, reply in enumerate(replies, start=1):
                reply_message = reply["message"]
                print(f"\t\tReply {j}: {reply_message}")