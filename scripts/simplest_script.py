import requests
import time

# GitHub API token
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

def get_authenticated_username():
    user_response = requests.get('https://api.github.com/user', headers=headers)
    if user_response.status_code == 200:
        return user_response.json()['login']
    else:
        print('Failed to fetch authenticated user info.')
        exit(1)

def follow_followers():
    next_page = followers_api_url
    my_username = get_authenticated_username()  # Get your username

    while next_page:
        # Get the list of followers
        response = requests.get(next_page, headers=headers)
        if response.status_code == 200:
            followers = response.json()
            # Get the next page URL from the 'Link' header if it exists
            if 'Link' in response.headers:
                links = response.headers['Link']
                next_page = None
                for link in links.split(','):
                    if 'rel="next"' in link:
                        next_page = link.split(';')[0].strip().strip('<>')
                        break
            else:
                next_page = None
        else:
            print('Failed to get list of followers.')
            time.sleep(5)  # Wait for 5 seconds before retrying
            continue

        # Follow each follower with rate limit handling and duplicate check
        for follower in followers:
            follower_login = follower["login"]

            # Check if they already follow you
            follows_me_url = f'https://api.github.com/users/{follower_login}/following/{my_username}'
            reverse_follow_check = requests.get(follows_me_url, headers=headers)

            if reverse_follow_check.status_code == 204:  # They already follow you
                print(f'Skipping {follower_login} (already follows you).')
                continue

            # Check if you already follow them
            check_follow_url = f'{follow_api_url}{follower_login}'
            check_response = requests.get(check_follow_url, headers=headers)

            if check_response.status_code == 204:  # Already following
                print(f'Already following: {follower_login}')
                continue
            elif check_response.status_code == 404:  # Not following yet
                follow_url = f'{follow_api_url}{follower_login}'
                success = False
                retries = 0

                while not success and retries < 3:
                    response = requests.put(follow_url, headers=headers)

                    if response.status_code == 204:  # Successful follow
                        print(f'Followed: {follower_login}')
                        success = True
                    else:
                        retries += 1
                        print(f'Failed to follow: {follower_login}. Retrying ({retries}/3)...')
                        time.sleep(10)  # Wait for 10 seconds before retrying

                if not success:
                    print(f'Failed to follow: {follower_login} after 3 attempts.')
            else:
                print(f'Error checking follow status for: {follower_login}')
                time.sleep(10)  # Wait for 10 seconds before retrying

            # Check rate limit and wait if needed
            remaining_requests = int(response.headers.get('X-RateLimit-Remaining', 0))
            if remaining_requests == 0:
                reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
                wait_time = max(reset_time - time.time() + 1, 0)  # Add 1 second buffer
                print(f'Rate limit exceeded. Waiting for {wait_time} seconds...')
                time.sleep(wait_time)

        # Wait for 5 seconds before fetching the next page of followers
        time.sleep(5)

if __name__ == "__main__":
    follow_followers()
