import imaplib
import email
import os
from config import SENDER_EMAIL, SENDER_PASSWORD

m = imaplib.IMAP4_SSL("imap.gmail.com", 993)
m.login(SENDER_EMAIL, SENDER_PASSWORD)
m.select('inbox') # select the inbox

result, data = m.uid('search', '(FROM "20094010@mail.wit.ie")')
print(result, data)

def store_processed_uid(uid):
    with open("db/processed_uids.txt", "a") as file:
        file.write(f"{uid}\n")

def is_uid_processed(uid):
    if not os.path.exists("db/processed_uids.txt"):
        return False
    with open("db/processed_uids.txt", "r") as file:
        processed_uids = file.read().splitlines()
    return uid in processed_uids

if result == 'OK':
    for num in data[0].split():
        if is_uid_processed(num.decode('utf-8')):
            print(f"Email UID {num.decode('utf-8')} already processed, skipping.")
            continue # skip if already processed
        result, data = m.fetch(num, '(RFC822)')
        if result == "OK":
            email_message = email.message_from_bytes(data[0][1])
            if email_message.is_multipart():
                for part in email_message.walk():
                    if part.get_content_type() == "text/plain":
                        body = part.get_payload(decode=True).decode("utf-8")
                        # Simplified condition to check for 'approve' in the reply
                        if "approve" in body.lower():  # This checks for both 'approve' and 'Approve'
                            print("Approved")
                            store_processed_uid(num.decode('utf-8'))
                        else:
                            print("Denied")
            else:
                # Handling non-multipart emails (unlikely for replies, but just in case)
                body = email_message.get_payload(decode=True).decode("utf-8")
                if "approve" in body.lower():
                    print("Approved")
                    store_processed_uid(num.decode('utf-8'))
                else:
                    print("Denied")
m.close()
m.logout()

# Inspired by below article, adapted for my needs.
# ref: https://alluaravind1313.medium.com/email-reading-using-python-imaplib-2d50912c119