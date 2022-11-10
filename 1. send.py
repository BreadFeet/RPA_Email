# SMTP: Simple Mail Trasfer Protocol

import smtplib
from account import *     # account.py 파일로부터 모든 정보 가져옴

with smtplib.SMTP("smtp.gmail.com", 587) as smtp :     # port=587
    smtp.ehlo()     # 연결이 잘 되는지 확인(안해도 전송은 됨)
    smtp.starttls()     # 모든 내용이 암호화되어 전송(Transport Layer Security)
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)    # 계정 로그인

    # 메일 보내기 - 한글은 인식 안됨!
    subject = "test email"     # 메일 제목
    body = "email body"        # 메일 본문
    
    # 제목과 본문 형식
    # msg = f"Subject: {subject}\n{body}"
    msg = "subject: {}\n{}".format(subject, body)
    
    # 발신자, 수신자, 정해진 형식의 메세지
    smtp.sendmail(EMAIL_ADDRESS, "recipient@email.com", msg)    
