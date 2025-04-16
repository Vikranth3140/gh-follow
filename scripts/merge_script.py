import requests

def get_followers(username, token, per_page=100):
    followers = []
    page = 1

    while True:
        url = f'https://api.github.com/users/{username}/followers'
        params = {
            'per_page': per_page,
            'page': page
        }
        headers = {
            'Authorization': f'token {token}'
        }

        response = requests.get(url, headers=headers, params=params)
        
        if response.status_code != 200:
            print(f'Error fetching followers: {response.status_code}')
            break

        data = response.json()
        if not data:
            break

        followers.extend(data)
        page += 1

    return followers

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

def get_non_reciprocal_users(followers, following):
    followers_set = {user['login'] for user in followers}
    following_set = {user['login'] for user in following}

    not_following_back = following_set - followers_set
    not_followed_back = followers_set - following_set

    return not_following_back, not_followed_back

def save_users_to_file(not_following_back, not_followed_back, filename = r'..\text files\non_reciprocal_users.txt'):
    with open(filename, 'w') as file:
        file.write("Users you follow but who don't follow you back:\n")
        for username in not_following_back:
            file.write(f'{username}\n')
        file.write("\nUsers who follow you but you don't follow back:\n")
        for username in not_followed_back:
            file.write(f'{username}\n')

def main():
    # Replace 'your_github_username' with your actual GitHub username
    username = 'your_github_username'
    # Replace 'your_github_token' with your personal GitHub token
    token = 'your_github_token'


    followers = get_followers(username, token)
    following = get_following(username, token)
    not_following_back, not_followed_back = get_non_reciprocal_users(followers, following)
    save_users_to_file(not_following_back, not_followed_back)
    print(f'Successfully saved {len(not_following_back)} users who you follow but don\'t follow you back to text files/non_reciprocal_users.txt')
    print(f'Successfully saved {len(not_followed_back)} users who follow you but you don\'t follow back to text files/non_reciprocal_users.txt')

if __name__ == '__main__':
    main()