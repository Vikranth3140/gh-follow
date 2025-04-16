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

def save_followers_to_file(followers, filename = r'..\text files\followers.txt'):
    with open(filename, 'w') as file:
        for follower in followers:
            file.write(f'{follower["login"]}\n')

def main():
    # Replace 'your_github_username' with your actual GitHub username
    username = 'your_github_username'
    # Replace 'your_github_token' with your personal GitHub token
    token = 'your_github_token'


    followers = get_followers(username, token)
    save_followers_to_file(followers)
    print(fr'Successfully saved {len(followers)} followers to text files\followers.txt')

if __name__ == '__main__':
    main()