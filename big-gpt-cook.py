import requests
import time

def get_following(username, token, per_page=100):
    following = []
    page = 1

    while True:
        url = f'https://api.github.com/users/{username}/following'
        params = {
            'per_page': per_page,
            'page': page
        }
        headers = {
            'Authorization': f'token {token}'
        }

        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f'Error fetching following: {response.status_code}')
            break

        data = response.json()
        if not data:
            break

        following.extend(data)
        page += 1

    return following

def get_user_info(username, token):
    url = f'https://api.github.com/users/{username}'
    headers = {
        'Authorization': f'token {token}'
    }
    response = requests.get(url, headers=headers)
    
    if response.status_code != 200:
        print(f'Error fetching user info for {username}: {response.status_code}')
        return None

    return response.json()

def filter_users(following, token):
    filtered_users = {
        'more_following_than_followers': [],
        'more_than_10000_following': []
    }

    for user in following:
        user_info = get_user_info(user['login'], token)
        
        if user_info:
            followers_count = user_info.get('followers', 0)
            following_count = user_info.get('following', 0)
            
            if following_count > followers_count:
                filtered_users['more_following_than_followers'].append(user['login'])
            
            if following_count > 10000:
                filtered_users['more_than_10000_following'].append(user['login'])
        
        # Be respectful of GitHub's rate limits
        time.sleep(1)

    return filtered_users

def save_users_to_file(users, filename='filtered_users.txt'):
    with open(filename, 'w') as file:
        for category, usernames in users.items():
            file.write(f"{category}:\n")
            for username in usernames:
                file.write(f"{username}\n")
            file.write("\n")

def main():
    # Replace 'your_github_username' with your actual GitHub username
    username = 'your_github_username'
    # Replace 'your_github_token' with your personal GitHub token
    token = 'your_github_token'

    following = get_following(username, token)
    filtered_users = filter_users(following, token)
    save_users_to_file(filtered_users)
    print(f'Successfully saved filtered users to filtered_users.txt')

if __name__ == '__main__':
    main()