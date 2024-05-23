import argparse
import requests
import time

def follow_user(username, token, action):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    follow_url = f'https://api.github.com/users/{username}/following'
    if action == 'follow':
        response = requests.put(follow_url, headers=headers)
        return response.status_code == 204
    elif action == 'unfollow':
        response = requests.delete(follow_url, headers=headers)
        return response.status_code == 204
    else:
        return False

def follow_followers(username, token, target_account):
    followers_api_url = f'https://api.github.com/users/{target_account}/followers'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(followers_api_url, headers=headers)
    if response.status_code == 200:
        followers = response.json()
        for follower in followers:
            follow_user(follower['login'], token, 'follow')
            time.sleep(10)  # Wait for 10 seconds between follows
    else:
        print('Failed to get list of followers.')

def unfollow_followers(username, token, target_account):
    followers_api_url = f'https://api.github.com/users/{target_account}/followers'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(followers_api_url, headers=headers)
    if response.status_code == 200:
        followers = response.json()
        for follower in followers:
            follow_user(follower['login'], token, 'unfollow')
            time.sleep(10)  # Wait for 10 seconds between unfollows
    else:
        print('Failed to get list of followers.')

def follow_unfollowers(username, token, target_account):
    following_api_url = 'https://api.github.com/user/following'
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    response = requests.get(following_api_url, headers=headers)
    if response.status_code == 200:
        following = response.json()
        followers_api_url = f'https://api.github.com/users/{target_account}/followers'
        response = requests.get(followers_api_url, headers=headers)
        if response.status_code == 200:
            followers = response.json()
            for follower in followers:
                if follower['login'] not in [f['login'] for f in following]:
                    follow_user(follower['login'], token, 'follow')
                    time.sleep(10)  # Wait for 10 seconds between follows
        else:
            print('Failed to get list of followers.')
    else:
        print('Failed to get list of users followed by you.')

def main():
    parser = argparse.ArgumentParser(description='Follower Frenzy - Follow/Unfollow GitHub users.')
    parser.add_argument('action', choices=['follow', 'unfollow'], help='Action to perform: follow or unfollow')
    parser.add_argument('--username', required=True, help='Your GitHub username')
    parser.add_argument('--token', required=True, help='Your personal access token')
    parser.add_argument('--target-account', help='Username of the target account for follower actions')
    parser.add_argument('--mode', choices=['followers', 'unfollowers'], help='Mode for follower actions: followers or unfollowers')

    args = parser.parse_args()

    if args.action == 'follow' and args.username and args.token and args.target_account:
        follow_followers(args.username, args.token, args.target_account)
        print(f'Followed followers of {args.target_account}.')
    elif args.action == 'unfollow' and args.username and args.token and args.target_account:
        unfollow_followers(args.username, args.token, args.target_account)
        print(f'Unfollowed followers of {args.target_account}.')
    elif args.action == 'follow' and args.username and args.token and args.target_account and args.mode == 'unfollowers':
        follow_unfollowers(args.username, args.token, args.target_account)
        print(f'Followed unfollowers of {args.target_account}.')
    else:
        print('Invalid arguments. Please check your input.')

if __name__ == "__main__":
    main()