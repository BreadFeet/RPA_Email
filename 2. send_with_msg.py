import smtplib
from account import *
from email.message import EmailMessage    # 한글 전송 가능

msg = EmailMessage()
msg["Subject"] = "테스트 메일"             # 제목
msg["From"] = EMAIL_ADDRESS                # 보내는 사람
msg["to"] = "recipient@email.com"       # 받는 사람
msg.set_content("테스트 본문")             # 본문

# 여러명에게 메일을 보내는 경우
# msg["To"] = "recipient1@email.com, recipient2@email.com"

# 다량의 이메일 주소를 리스트로 받는 경우
# to_list = ["recipient1@email.com", "recipient2@email.com"]
# msg["To"] = ",".join(to_list)   # to_list를 ,를 이용하여 합침


# 참조
msg["Cc"] = "ccrecipient@email.com"

# 숨김참조
msg["Bcc"] = "bccrecipient@email.com"


with smtplib.SMTP("smtp.gmail.com", 587) as smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

