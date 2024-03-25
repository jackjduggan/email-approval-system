# Email Approval System with Python
I built this solution when testing things for my final year project.\
I needed a way to pause a Python/Bash Pipline and wait for approval before continuing.\
After a brief amount of research, I stumbled across the simple idea of using email.

## How it works:
- There's a hidden file called `config.py` with string entries for `SENDER_EMAIL`, `SENDER_PASSWORD`, and `RECEIVER_PASSWORD`.
    - For the sender, I created a new email specifically for this use case. The receiver is my college email.
    - The receiver's password is actually a GMail app password, which can only be obtained when 2FA is enabled.
    - This file's contents is imported at the top of the Python files.
- `send.py` is executed, which sends an email to the recipient
- The recipient must reply to the email with either **Approve** or **approve**.
- `read.py` is executed, and scans the sender's inbox for the reply. When it finds it, it checks it says **Approve**. Anything else is considered **Deny**.
- If all goes well, the email's UID as well as the message **Approved** are printed to the console.
- A hidden file at, `db/processed_uids.txt` tracks the emails that have already been read, so that an email can't be processed more than once.

## Screenshots:
![image](https://github.com/jackjduggan/email-approval-system/assets/74904632/d36dbd1b-19c1-41a7-b961-484bc12e1af9)
![image](https://github.com/jackjduggan/email-approval-system/assets/74904632/4dce1eb3-50c1-41db-bc56-cc75265bae81)

### References
This projects code was adapted from the following articles
[Send Email Code Reference](https://medium.com/@thakuravnish2313/sending-emails-with-python-using-the-smtplib-library-e5db3a8ce69a)
[Read Email Code Reference](https://alluaravind1313.medium.com/email-reading-using-python-imaplib-2d50912c119)
