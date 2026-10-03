import time
import imapclient
import pyzmail

conn = imapclient.IMAPClient('imap.gmail.com', ssl=True)
conn.login('drouxvg@gmail.com', 'your-app-password')
conn.select_folder('INBOX', readonly=True)

UIDs = conn.search(['SINCE 10-Mar-2026'])
print(UIDs)

rawMessage = conn.fetch(UIDs, ['BODY[]', 'FLAGS'])

for uid in UIDs:
    message = pyzmail.PyzMessage.factory(rawMessage[uid][b'BODY'])
    print(message.get_addresses('from'))
    print(message.get_addresses('to'))
    print(message.text_part.get_payload().decode('UTF-8') if message.text_part else "No text part")