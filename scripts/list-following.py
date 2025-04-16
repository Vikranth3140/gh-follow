import requests

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

def save_following_to_file(following, filename = r'..\text files\following.txt'):
    with open(filename, 'w') as file:
        for user in following:
            file.write(f'{user["login"]}\n')

def main():
    # Replace 'your_github_username' with your actual GitHub username
    username = 'your_github_username'
    # Replace 'your_github_token' with your personal GitHub token
    token = 'your_github_token'

    following = get_following(username, token)
    save_following_to_file(following)
    print(fr'Successfully saved {len(following)} following users to text files\following.txt')

if __name__ == '__main__':
    main()