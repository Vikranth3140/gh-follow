import argparse
import requests
import time

def follow_user(token, target_user):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    follow_url = f'https://api.github.com/users/{target_user}/following'
    response = requests.put(follow_url, headers=headers)
    if response.status_code == 204:
        print(f'Followed {target_user}')
    else:
        print(f'Failed to follow {target_user}')

def unfollow_user(token, target_user):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    unfollow_url = f'https://api.github.com/users/{target_user}/following'
    response = requests.delete(unfollow_url, headers=headers)
    if response.status_code == 204:
        print(f'Unfollowed {target_user}')
    else:
        print(f'Failed to unfollow {target_user}')

def follow_followers(username, token, target_account):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    followers_api_url = f'https://api.github.com/users/{target_account}/followers'
    response = requests.get(followers_api_url, headers=headers)
    if response.status_code == 200:
        followers = response.json()
        for follower in followers:
            follow_user(username, token, follower['login'])
            time.sleep(10)  # Wait for 10 seconds between follows
    else:
        print('Failed to get list of followers.')

def unfollow_followers(username, token, target_account):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    followers_api_url = f'https://api.github.com/users/{target_account}/followers'
    response = requests.get(followers_api_url, headers=headers)
    if response.status_code == 200:
        followers = response.json()
        for follower in followers:
            unfollow_user(username, token, follower['login'])
            time.sleep(10)  # Wait for 10 seconds between unfollows
    else:
        print('Failed to get list of followers.')

def follow_unfollowers(username, token, target_account):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    following_api_url = 'https://api.github.com/user/following'
    response = requests.get(following_api_url, headers=headers)
    if response.status_code == 200:
        following = response.json()
        followers_api_url = f'https://api.github.com/users/{target_account}/followers'
        response = requests.get(followers_api_url, headers=headers)
        if response.status_code == 200:
            followers = response.json()
            for follower in followers:
                if follower['login'] not in [f['login'] for f in following]:
                    follow_user(username, token, follower['login'])
                    time.sleep(10)  # Wait for 10 seconds between follows
        else:
            print('Failed to get list of followers.')
    else:
        print('Failed to get list of users followed by you.')

def unfollow_unfollowers(username, token, target_account):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }
    following_api_url = 'https://api.github.com/user/following'
    response = requests.get(following_api_url, headers=headers)
    if response.status_code == 200:
        following = response.json()
        followers_api_url = f'https://api.github.com/users/{target_account}/followers'
        response = requests.get(followers_api_url, headers=headers)
        if response.status_code == 200:
            followers = response.json()
            for follower in followers:
                if follower['login'] not in [f['login'] for f in following]:
                    unfollow_user(username, token, follower['login'])
                    time.sleep(10)  # Wait for 10 seconds between unfollows
        else:
            print('Failed to get list of followers.')
    else:
        print('Failed to get list of users followed by you.')

def main():
    print('\nInstructions:\n'
          '- For following a specific user, use: python script.py follow_user --username YourUsername --token YourToken --target-user TargetUser\n'
          '- For unfollowing a specific user, use: python script.py unfollow_user --username YourUsername --token YourToken --target-user TargetUser\n'
          '- For following all followers of a target account, use: python script.py follow_followers --username YourUsername --token YourToken --target-account TargetAccount\n'
          '- For unfollowing all followers of a target account, use: python script.py unfollow_followers --username YourUsername --token YourToken --target-account TargetAccount\n'
          '- For following all users not following you back from a target account, use: python script.py follow_unfollowers --username YourUsername --token YourToken --target-account TargetAccount\n'
          '- For unfollowing all users not following you back from a target account, use: python script.py unfollow_unfollowers --username YourUsername --token YourToken --target-account TargetAccount\n')
    
    parser = argparse.ArgumentParser(description='Follow/Unfollow GitHub users.')
    parser.add_argument('action', choices=['follow_user', 'unfollow_user', 'follow_followers', 'unfollow_followers',
                                           'follow_unfollowers', 'unfollow_unfollowers'],
                        help='Action to perform: follow_user, unfollow_user, follow_followers, unfollow_followers, follow_unfollowers, unfollow_unfollowers')
    parser.add_argument('--username', required=True, help='Your GitHub username')
    parser.add_argument('--token', required=True, help='Your personal access token')
    parser.add_argument('--target-user', help='Username of the target user for follow/unfollow actions')
    parser.add_argument('--target-account', help='Username of the target account for follower actions')

    args = parser.parse_args()

    if args.action == 'follow_user' and args.username and args.token and args.target_user:
        follow_user(args.token, args.target_user)
    elif args.action == 'unfollow_user' and args.username and args.token and args.target_user:
        unfollow_user(args.token, args.target_user)
    elif args.action == 'follow_followers' and args.username and args.token and args.target_account:
        follow_followers(args.username, args.token, args.target_account)
    elif args.action == 'unfollow_followers' and args.username and args.token and args.target_account:
        unfollow_followers(args.username, args.token, args.target_account)
    elif args.action == 'follow_unfollowers' and args.username and args.token and args.target_account:
        follow_unfollowers(args.username, args.token, args.target_account)
    elif args.action == 'unfollow_unfollowers' and args.username and args.token and args.target_account:
        unfollow_unfollowers(args.username, args.token, args.target_account)
    else:
        print('Invalid arguments. Please check your input.')

if __name__ == "__main__":
    main()