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

# Get the list of followers
response = requests.get(followers_api_url, headers=headers)
followers = response.json()

# Get the list of users already followed
response = requests.get(follow_api_url, headers=headers)
if response.status_code == 200:
    already_following = [follower['login'] for follower in response.json()]
else:
    print('Failed to get list of users already followed.')
    already_following = []

# Follow each follower with rate limit handling and duplicate check
for follower in followers:
    if follower["login"] in already_following:
        print(f'Already following: {follower["login"]}')
        continue

    follow_url = f'{follow_api_url}{follower["login"]}'
    response = requests.put(follow_url, headers=headers)

    if response.status_code == 204:  # Successful follow
        print(f'Followed: {follower["login"]}')
    else:
        print(f'Failed to follow: {follower["login"]}')

    # Check rate limit and wait if needed
    remaining_requests = int(response.headers['X-RateLimit-Remaining'])
    if remaining_requests == 0:
        reset_time = int(response.headers['X-RateLimit-Reset'])
        wait_time = reset_time - time.time() + 1  # Add 1 second buffer
        print(f'Rate limit exceeded. Waiting for {wait_time} seconds...')
        time.sleep(wait_time)