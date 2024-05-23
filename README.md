# Follower Frenzy

Welcome to Follower Frenzy!

This Python script allows you to manage your GitHub followers and following list efficiently. You can follow/unfollow specific users, follow all followers of a target account, unfollow all followers of a target account, follow all users not following you back from a target account, and unfollow all users not following you back from a target account.

## Features

1. Follow a specific user
2. Unfollow a specific user
3. Follow all followers of a target account
4. Unfollow all followers of a target account
5. Follow all users not following you back from a target account
6. Unfollow all users not following you back from a target account

## How to Run

1. Clone this repository to your local machine.
    
    ```bash
    git clone https://github.com/Vikranth3140/Follower-Frenzy.git
    ```
    
3. Install the required packages.
    
    ```bash
    pip install -r requirements.txt
    ```

4. Open a terminal or command prompt in the cloned directory.

5. Use the following commands to run the script:

   - For following a specific user:
     ```bash
     python script.py follow_user --username YourUsername --token YourToken --target-user TargetUser
     ```

   - For unfollowing a specific user:
     ```bash
     python script.py unfollow_user --username YourUsername --token YourToken --target-user TargetUser
     ```

   - For following all followers of a target account:
     ```bash
     python script.py follow_followers --username YourUsername --token YourToken --target-account TargetAccount
     ```

   - For unfollowing all followers of a target account:
     ```bash
     python script.py unfollow_followers --username YourUsername --token YourToken --target-account TargetAccount
     ```

   - For following all users not following you back from a target account:
     ```bash
     python script.py follow_unfollowers --username YourUsername --token YourToken --target-account TargetAccount
     ```

   - For unfollowing all users not following you back from a target account:
     ```bash
     python script.py unfollow_unfollowers --username YourUsername --token YourToken --target-account TargetAccount
     ```

## Note

- Get your GitHub Access Token [here](https://github.com/settings/tokens).
- Replace `YourUsername`, `YourToken`, `TargetUser`, and `TargetAccount` with your actual GitHub username, personal access token, target user's username, and target account's username, respectively.
- Ensure you have the necessary permissions and abide by GitHub's terms of service while using this script.
- Do checkout [Follow-for-follow-back](https://github.com/AlgoArchives/Follow-for-follow-back.git) and run the script on those accounts inorder to gain traction :)

Happy GitHub follower management!