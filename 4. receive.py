from imap_tools import MailBox
from account import *

# mailbox = MailBox("imap.gmail.com", 993)     # port=993
# mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")    # 기본폴더=받은편지함


# with를 사용하는 경우에는 with 안에서만 login 상태이기 때문에 logout이 필요 없음!
with MailBox("imap.gmail.com", 993) as mailbox :
    mailbox.login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX")

    # limit: 최대 불러오는 메일 수
    # reverse: 날짜가 큰 순으로 정렬
    for msg in mailbox.fetch(limit=1, reverse=True) :  
        print("제목:", msg.subject)
        print("발신자:", msg.from_)    # 패키지 불러오는 from과 구분
        print("수신자:", msg.to)
        print("참조:", msg.cc)
        print("숨김참조:", msg.bcc)
        print("날짜:", msg.date)    # 시간은 GMT로 출력
        print("본문:", msg.text)
        # print("HTML 메시지:", msg.html)
        print("=" * 100)      # ====== 줄 긋기

        # 첨부파일 내용
        for att in msg.attachments :
            print("첨부파일 이름:", att.filename)
            print("타입:", att.content_type)
            print("크기", att.size)

            # 첨부파일 다운로드
            with open("download_" + str(att.filename), "wb") as f :
                f.write(att.payload)
                print("첨부파일 '{}' 다운로드 완료".format(att.filename))


# mailbox.logout()
