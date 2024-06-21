import streamlit as st
import requests

st.set_page_config(page_title="GitHub Follow Checker", layout="centered")

st.title("gh-follow")
st.subheader("Who is not following you back on GitHub?")

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

# Form to input GitHub username
with st.form("username_form"):
    username = st.text_input("Your GitHub username")
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
st.markdown("---")
st.markdown("### Support the project")
st.markdown("[⭐️ Star us on GitHub](https://github.com/Vikranth3140/gh-follow/)")
st.markdown("---")
st.markdown("### Developer")
st.markdown("[Vikranth3140](https://github.com/Vikranth3140) © 2024")