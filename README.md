Follower Frenzy
===============

Welcome to Follower Frenzy!

Follower Frenzy is designed to simplify the process of following users who follow a particular GitHub account. It uses the GitHub API along with Python to retrieve the list of followers and follow them with rate limit handling.

Features
--------

*   Fetches the list of followers of a specified GitHub account.
*   Automatically follows each follower with rate limit handling.
*   Checks for duplicate follows and avoids redundant follows.

Setup and Usage
---------------

1.  Clone the repository to your local machine:
    
    ```bash
    git clone https://github.com/Vikranth3140/Follower-Frenzy.git
    cd Follower-Frenzy
    ```
    
2.  Install the required libraries:
    
    ```bash
    pip install -r requirements.txt
    ```
    
3.  Update the following variables in the script:
    
    *   `username`: Your GitHub username.
    *   `token`: Your personal access token.
    *   `target_account`: The GitHub account whose followers you want to follow.

4.  Run the script:
    
    ```bash
    python follow_followers.py
    ```
    
5.  Sit back and let Follower Frenzy do the work for you!

License
-------

This project is licensed under the [MIT License](LICENSE).