import requests

class JSONPlaceholderClient:
    
    BASE_URL = "https://jsonplaceholder.typicode.com"

    def __init__(self):
        
        self.session = requests.Session()

    def get_posts(self, post_id=None):
        
        url = f"{self.BASE_URL}/posts"
        if post_id:
            url += f"/{post_id}"

        resp = self.session.get(url)
        resp.raise_for_status()  
        return resp.json()

    def create_post(self, title, body, user_id):
    
        url = f"{self.BASE_URL}/posts"
        payload = {
            "title": title,
            "body": body,
            "userId": user_id
        }

        resp = self.session.post(url, json=payload)
        resp.raise_for_status()
        return resp.json()


# Example usage
if __name__ == "__main__":
    client = JSONPlaceholderClient()

    posts = client.get_posts()
    print("First two posts:", posts[:2])

    post = client.get_posts(post_id=1)
    print("Post #1:", post)

    new_post = client.create_post(
        title="Hello World",
        body="This is a test post created via our client.",
        user_id=1
    )
    print("Newly created post:", new_post)
