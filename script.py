import requests

# GitHub username and API token
username = 'your_username'
token = 'your_personal_access_token'

# Account whose followers you want to follow
target_account = 'target_username'

# GitHub API endpoint
api_url = f'https://api.github.com/users/{target_account}/followers'

# Header with authentication token
headers = {
    'Authorization': f'token {token}',
    'Accept': 'application/vnd.github.v3+json'
}

# Get the list of followers
response = requests.get(api_url, headers=headers)
followers = response.json()

# Follow each follower
for follower in followers:
    follow_url = f'https://api.github.com/user/following/{follower["login"]}'
    requests.put(follow_url, headers=headers)

    print(f'Followed: {follower["login"]}')