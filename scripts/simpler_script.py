import requests
import time

# GitHub username and API token
username = 'your_username'
token = 'your_personal_access_token'

# Account whose followers you want to follow
target_account = 'target_username'

# GitHub API endpoints
followers_api_url = f'https://api.github.com/users/{target_account}/followers'
follow_api_url = 'https://api.github.com/user/following/'

# Header with authentication token
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

def follow_followers():
    while True:
        # Get the list of followers
        response = requests.get(followers_api_url, headers=headers)
        if response.status_code == 200:
            followers = response.json()
        else:
            print('Failed to get list of followers.')
            time.sleep(5)  # Wait for 5 seconds before retrying
            continue

        # Follow each follower with rate limit handling and duplicate check
        for follower in followers:
            follow_url = f'{follow_api_url}{follower["login"]}'
            response = requests.put(follow_url, headers=headers)

            if response.status_code == 204:  # Successful follow
                print(f'Followed: {follower["login"]}')
            else:
                print(f'Failed to follow: {follower["login"]}')
                time.sleep(10)  # Wait for 10 seconds before retrying

            # Check rate limit and wait if needed
            remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
            if remaining_requests == 0:
                reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
                wait_time = max(reset_time - time.time() + 1, 0)  # Add 1 second buffer
                print(f'Rate limit exceeded. Waiting for {wait_time} seconds...')
                time.sleep(wait_time)

        # Wait for 5 seconds before fetching followers again
        time.sleep(5)

if __name__ == "__main__":
    follow_followers()