import smtplib
conn = smtplib.SMTP('smtp.gmail.com', 587)
type(conn)
conn
conn.ehlo()
conn.starttls()
conn.login('drouxvg@gmail.com', 'W3tStones2013')