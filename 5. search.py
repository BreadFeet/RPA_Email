from imap_tools import MailBox
from account import *

with MailBox("imap.gmail.com", 993).login(EMAIL_ADDRESS, EMAIL_PASSWORD, initial_folder="INBOX") as mailbox :
    # 1. 전체 메일 대상
    # for msg in mailbox.fetch(limit=5, reverse=True) :  
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 2. 읽지 않은 메일 대상
    # for msg in mailbox.fetch('(UNSEEN)', limit=3, reverse=True) :  
    #     print("[{}] {}".format(msg.from_, msg.subject)) 

    # 3. 특정인이 보낸 메일 검색
    # for msg in mailbox.fetch('(FROM mysterykkk@hanmail.net)', limit=3, reverse=True) :  
    #     print("[{}] {}".format(msg.from_, msg.subject)) 

    # 4. Header(제목, 보낸사람, 받는사람) 또는 내용 검색
    # for msg in mailbox.fetch('(TEXT "noreply")', limit=3, reverse=True) :  
    #     print("[{}] {}".format(msg.from_, msg.subject)) 

    # 띄어쓰기는 각각 단어를 갖는 메일을 찾게 된다!
    # for msg in mailbox.fetch('(TEXT "account registration")', limit=3, reverse=True) :  
    #     print("[{}] {}".format(msg.from_, msg.subject)) 

    # 5. 제목 검색
    # for msg in mailbox.fetch('(SUBJECT "application")', limit=3, reverse=True) :  
    #     print("[{}] {}".format(msg.from_, msg.subject)) 

    # 한글 제목을 검색하려면, 우회 방법 사용
    # for msg in mailbox.fetch(limit=5, reverse=True) :  
    #     if "테스트" in msg.subject :
    #         print("[{}] {}".format(msg.from_, msg.subject)) 

    # 6. 내용 검색
    # for msg in mailbox.fetch('(BODY "Sori Kim")', limit=3, reverse=True) :
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 7. 날짜 검색
    # for msg in mailbox.fetch('(SENTON 4-Feb-2021)', limit=5, reverse=True) :
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 날짜 이후 검색(특정 날짜 포함)
    # for msg in mailbox.fetch('(SENTSINCE 4-Feb-2021)', limit=5, reverse=True) :
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 특정 날짜 이전 검색(특정 날짜 포함 안함)
    # for msg in mailbox.fetch('(SENTBEFORE 4-Feb-2021)', limit=5, reverse=True) :
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 8. 2가지 이상의 조건을 모두 만족하는 메일
    # for msg in mailbox.fetch('(BODY "Sori" SENTSINCE 4-Feb-2021)', limit=5, reverse=True) :
    #     print("[{}] {}".format(msg.from_, msg.subject))

    # 9. 2가지 중 하나 조건을 만족하는 메일
    for msg in mailbox.fetch('(OR SUBJECT "offer" SENTSINCE 6-Feb-2021)', limit=5, reverse=True) :
        print("[{}] 날짜: {}, 제목: {}".format(msg.from_, msg.date, msg.subject))

        