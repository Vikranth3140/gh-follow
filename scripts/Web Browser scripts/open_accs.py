import webbrowser

def open_non_reciprocal_github_users(filename, max_users=15):
    with open(filename, 'r') as file:
        lines = file.readlines()

    start_index = None
    for i, line in enumerate(lines):
        if 'Users you follow but who don\'t follow you back:' in line:
            start_index = i + 1
            break

    if start_index is None:
        print("Section not found.")
        return

    # Grab usernames until we hit an empty line or end of file
    usernames = []
    for line in lines[start_index:]:
        line = line.strip()
        if not line or line.startswith('Users'):
            break
        usernames.append(line)

    # Open first `max_users` GitHub profiles
    for username in usernames[:max_users]:
        url = f'https://github.com/{username}'
        webbrowser.open_new_tab(url)

    print(f"Opened {min(max_users, len(usernames))} GitHub profiles.")

# Example usage
open_non_reciprocal_github_users("non_reciprocal_users.txt", max_users=15)
