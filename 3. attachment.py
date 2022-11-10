import smtplib
from account import *
from email.message import EmailMessage

msg = EmailMessage()
msg["subject"] = "테스트 메일"
msg["from"] = EMAIL_ADDRESS
msg['to'] = "recipient@email.com"
msg.set_content("첨부파일을 다운로드 하세요")


# 첨부파일 - 이미지 파일
with open("paint.png", "rb") as f :
    msg.add_attachment(f.read(), maintype='image', subtype='png', filename=f.name)
    # MIME type : MS window에서 확장자로 파일 형태를 읽는 것과 같이, 인터넷에서 데이터를 인식하는 라벨

# 첨부파일 - pdf
f = open('attachment.pdf', 'rb')
msg.add_attachment(f.read(), maintype='application', subtype='pdf', filename=f.name)

# 첨부파일 - excel
with open('excelfile.xls', 'rb') as f :
    msg.add_attachment(f.read(), maintype='application', subtype='octet-stream', filename='excel_file_test.xls')


with smtplib.SMTP("smtp.gmail.com", 587) as smtp :
    smtp.ehlo()
    smtp.starttls()
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)