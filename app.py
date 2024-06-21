import streamlit as st
import requests

st.set_page_config(page_title="GitHub Follow Checker", layout="centered")

st.title("gh-follow")
st.subheader("Who is not following you back on GitHub?")

# Add custom styling
styl = """
    <style>
        .top-right {
            position: fixed;
            top: 10px;
            right: 10px;
            background-color: #fff;
            padding: 10px;
            border-radius: 5px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
        }
        .made-by {
            position: fixed;
            bottom: 10px;
            left: 800px;
            color: white;
        }
        .source-code {
            position: fixed;
            bottom: 10px;
            right: 400px;
            color: white;
        }
    </style>
"""

st.markdown(styl, unsafe_allow_html=True)

# Function to get followers and following lists from GitHub with pagination
def get_github_data(username, data_type):
    url = f"https://api.github.com/users/{username}/{data_type}"
    headers = {"Accept": "application/vnd.github.v3+json"}
    params = {'per_page': 100}
    data = []
    while True:
        response = requests.get(url, headers=headers, params=params)
        if response.status_code == 200:
            page_data = response.json()
            if not page_data:
                break
            data.extend(page_data)
            if 'next' in response.links:
                url = response.links['next']['url']
            else:
                break
        else:
            st.error(f"Error fetching {data_type} data for {username}: {response.status_code}")
            break
    return [user['login'] for user in data]

# Display "Support the project" links in the top right corner
st.markdown("""
    <div class="top-right">
        <h3>Support the project</h3>
        <ul>
            <li><a href="https://github.com/Vikranth3140/gh-follow" target="_blank">⭐️ Star us on GitHub</a></li>
        </ul>
    </div>
""", unsafe_allow_html=True)

# Form to input GitHub username
with st.form("username_form"):
    username = st.text_input("Your GitHub username", max_chars=39)
    submitted = st.form_submit_button("Submit")

if submitted:
    if username:
        st.write(f"Getting data for {username}...")

        # Get followers and following data
        followers = get_github_data(username, "followers")
        following = get_github_data(username, "following")

        if followers and following:
            # Calculate who is not following back
            not_following_back = [user for user in following if user not in followers]

            st.write(f"Who is not following {username} back on GitHub?")
            if not_following_back:
                st.write(f"{len(not_following_back)} users are not following you back:")
                for user in not_following_back:
                    st.markdown(f"- [{user}](https://github.com/{user})")
            else:
                st.success(f"Success! Everyone is following {username} back on GitHub.")
    else:
        st.warning("Please enter a GitHub username.")

# Footer
st.markdown("""
    <div class="made-by">Made by <a href='https://github.com/Vikranth3140' style='color:white; text-decoration:none;'>Vikranth Udandarao</a></div>
    <div class="source-code"><a href='https://github.com/Vikranth3140/gh-follow' style='color:white; text-decoration:none;'>Source Code</a></div>
""", unsafe_allow_html=True)