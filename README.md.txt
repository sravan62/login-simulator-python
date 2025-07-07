#  Login Simulator - Python Mini Project

This is a beginner-friendly Python project that simulates a login system using the command line.  
It reads usernames and passwords from a file, verifies user input, and logs login attempts with timestamps.

---

##  Features

- ✅ Reads user credentials from a `users.txt` file  
- ✅ Validates username and password input  
- ✅ Logs every login attempt (success or failure) in `login_log.txt` with date and time  
- ✅ Beginner-friendly and easy to understand

---

##  Project Structure

login-simulator/
├── login_simulator.py # Main Python script
├── users.txt # Stores username:password
└── login_log.txt # (Auto-generated) Logs login attempts

---

##  Example `users.txt` Format

jenny:password123
guest:guestpass
admin:admin123

> Format: `username:password`

---

##  How to Run

1. **Make sure you have Python installed** (version 3.x)
2. Open a terminal or PowerShell
3. Run:

```
python login_simulator.py

4. Enter a username and password from users.txt

##  Sample Output

###  If login is successful:
Enter username: jenny
Enter password: password123
✅ Login successful.

###  If login fails:
Enter username: guest
Enter password: wrongpass
❌ Login failed.

---

##  login_log.txt Example

[2025-07-02 18:45:12] jenny -> SUCCESS
[2025-07-02 18:46:01] guest -> FAILURE

> This file is created automatically in the same folder.

## 🧑‍💻 Author

**Sravan**  
🔗 GitHub: [sravan62](https://github.com/sravan62)

---

## 🏷️ Tags

`Python` • `Beginner` • `CLI Tool` • `Login System` • `SOC Practice`
