import webbrowser

def open_and_remove_non_reciprocal_users(filename, max_users=15):
    with open(filename, 'r') as file:
        lines = file.readlines()

    start_index = None
    for i, line in enumerate(lines):
        if "Users you follow but who don't follow you back:" in line:
            start_index = i + 1
            break

    if start_index is None:
        print("Section not found.")
        return

    # Extract usernames after the section
    usernames = []
    end_index = start_index
    for i in range(start_index, len(lines)):
        line = lines[i].strip()
        if not line or line.startswith('Users'):
            break
        usernames.append(line)
        end_index = i + 1

    # Open first `max_users` profiles
    for username in usernames[:max_users]:
        webbrowser.open_new_tab(f'https://github.com/{username}')

    print(f"Opened {min(max_users, len(usernames))} GitHub profiles.")

    # Remove the opened usernames
    remaining_usernames = usernames[max_users:]

    # Reconstruct the file
    new_lines = lines[:start_index]  # keep everything before usernames
    for username in remaining_usernames:
        new_lines.append(f"{username}\n")
    new_lines += lines[end_index:]  # keep everything after the section

    # Write back to the file
    with open(filename, 'w') as file:
        file.writelines(new_lines)

# Example usage
open_and_remove_non_reciprocal_users(r"../../text files/non_reciprocal_users.txt", max_users=15)
