# gh-follow

Welcome to gh-follow!

This Python script, combined with a Streamlit web app, allows you to manage your GitHub followers and following list efficiently. You can identify users who are not following you back and interact with your followers and following lists through an intuitive web interface.

Currently deployed at <a href="https://gh-follow.streamlit.app/">gh-follow.streamlit.app<a>.

## Features

1. Identify users who are not following you back
2. Follow a specific user
3. Unfollow a specific user
4. Follow all followers of a target account
5. Unfollow all followers of a target account
6. Follow all users not following you back from a target account
7. Unfollow all users not following you back from a target account

## How to Run the Web App

1. Clone this repository to your local machine and navigate to the project directory.
    
    ```bash
    git clone https://github.com/Vikranth3140/gh-follow.git
    cd gh-follow
    ```
    
2. Install the required packages.
    
    ```bash
    pip install -r requirements.txt
    ```
    
3. Run the Streamlit app.
    
    ```bash
    streamlit run app.py
    ```

4. Open your web browser and navigate to the displayed URL (usually `http://localhost:8501`).

## How to Run the Scripts

1. Clone this repository to your local machine and navigate to the project directory.
    
    ```bash
    git clone https://github.com/Vikranth3140/gh-follow.git
    cd gh-follow
    ```
    
2. Install the required packages.
    
    ```bash
    pip install -r requirements.txt
    ```
    
3. Navigate to the scripts directory.
    
    ```bash
    cd scripts
    ```

4. Use the following commands to run the script:

   - For following a specific user:
     ```bash
     python main.py follow_user --username YourUsername --token YourToken --target-user TargetUser
     ```

   - For unfollowing a specific user:
     ```bash
     python main.py unfollow_user --username YourUsername --token YourToken --target-user TargetUser
     ```

   - For following all followers of a target account:
     ```bash
     python main.py follow_followers --username YourUsername --token YourToken --target-account TargetAccount
     ```

   - For unfollowing all followers of a target account:
     ```bash
     python main.py unfollow_followers --username YourUsername --token YourToken --target-account TargetAccount
     ```

   - For following all users not following you back from a target account:
     ```bash
     python main.py follow_unfollowers --username YourUsername --token YourToken --target-account TargetAccount
     ```

   - For unfollowing all users not following you back from a target account:
     ```bash
     python main.py unfollow_unfollowers --username YourUsername --token YourToken --target-account TargetAccount
     ```

## Note

- Get your GitHub Access Token [here](https://github.com/settings/tokens).
- Replace `YourUsername`, `YourToken`, `TargetUser`, and `TargetAccount` with your actual GitHub username, personal access token, target user's username, and target account's username, respectively.
- Ensure you have the necessary permissions and abide by GitHub's terms of service while using this script.
- Check out [Follow-for-follow-back](https://github.com/AlgoArchives/Follow-for-follow-back.git) and run the script on those accounts to gain traction :)

## License

This project is licensed under the [MIT License](LICENSE).

Happy GitHub follower management!
