import requests
from bs4 import BeautifulSoup

def scrape_facebook_comments(page_url):
    comments = []
    response = requests.get(page_url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, "html.parser")
        comment_elements = soup.find_all("div", {"data-testid": "UFI2Comment/body"})
        
        for comment_element in comment_elements:
            comment = comment_element.get_text(strip=True)
            comments.append(comment)
        
    return comments

if __name__ == "__main__":
    page_url = "https://www.facebook.com/bbcnews"  # Replace with the actual Facebook page URL
    comments = scrape_facebook_comments(page_url)
    
    for i, comment in enumerate(comments, start=1):
        print(f"Comment {i}: {comment}")

# <div class="_72vr"><a class="_6qw4" data-hovercard="/ajax/hovercard/user.php?id=pfbid02H6H9ebXA1q5CNLpragnkby9BiuSPwq4Mn3kwWJHJdp44prG8BE83nXUgSDDRKS2Ul&amp;extragetparams={&quot;directed_target_id&quot;: &quot; &quot;}" href="/salim.hossain.71216?comment_id=Y29tbWVudDo2NjI1OTE0MjE3NDM1NzM0XzExNzEwNTczMTY4ODY2Mzc%3D">Salim Hossain</a> <span dir="ltr"><span class="_3l3x"><span>নারায়ণগঞ্জে কোথায় পাব।</span></span></span></div>