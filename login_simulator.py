import datetime

def load_users(filename):
    users = {}
    f = open(filename, 'r')         # Open the file
    lines = f.readlines()           # Read all lines
    f.close()                       # Close the file

    for line in lines:              # Go through each line
        if ':' in line:             # Check if it looks like "user:pass"
            name, pwd = line.strip().split(':')  # Split it
            users[name] = pwd       # Save it to dictionary
    return users

def log_attempt(username, success):
    # Get the current time like "2025-07-02 16:20:55"
    time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Decide the result text
    if success:
        status = "SUCCESS"
    else:
        status = "FAILURE"

    # Open the log file to add a new line (append mode "a")
    f = open("login_log.txt", "a")
    f.write("[" + time + "] " + username + " -> " + status + "\n")
    f.close()

def login():
    users = load_users("users.txt")             
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    if username in users and users[username] == password:
        print("✅ Login successful.")
        log_attempt(username, True)
    else:
        print("❌ Login failed.")
        log_attempt(username, False)

if __name__ == "__main__":
    login()
