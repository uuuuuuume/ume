from tkinter import *
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import simpledialog
import random
#회원가입 정보 딕셔너리
users = {}
   
#회원가입 창 코드 
def rgsEvent1():
    rgs1 = Tk()
    rgs1.title("학생 회원가입 창")
    rgs1.geometry("400x200")

    lab1 = Label(rgs1)
    lab1.config(text = "생성할 ID")
    lab1.pack()

    ent1 = Entry(rgs1)

    ent1.pack()

    lab2 = Label(rgs1)
    lab2. config(text = "생성할 Password")
    lab2.pack()

    ent2 = Entry(rgs1)
    ent2.config(show = "*")
    ent2.pack()

    def save_users():
        userID = ent1.get()
        userPassword = ent2.get()
        users[userID] = userPassword
        messagebox.showinfo("회원가입 완료", "회원가입이 완료되었습니다.")
        rgs1.destroy()

    btn = Button(rgs1)
    btn.config(text = "회원가입", command = save_users)
    btn.pack()
    rgs1.mainloop()
      
#학생 로그인창 코드
def btnEvent1():
    JJ2 = Tk()
    JJ2.title("학생 로그인창")
    JJ2.geometry("400x200")

    lab1 = Label(JJ2)
    lab1.config(text = "ID")
    lab1.pack()

    ent1 = Entry(JJ2)
    ent1.pack()

    lab2 = Label(JJ2)
    lab2.config(text = "Password")
    lab2.pack()

    ent2 = Entry(JJ2)
    ent2.config(show = "*")
    ent2.pack()

    def Login():
        userID = ent1.get()
        userPassword = ent2.get()

        if userID in users and users[userID] == userPassword:
            messagebox.showinfo("로그인 성공", "학생 로그인 성공")
            JJ2.destroy()
        
###(메인화면에 들어있는 화면)
           #학생 기능 화면 코드
            STDfunc = Tk()
            STDfunc.title("학생 기능")
            STDfunc.geometry('450x350')
            
            STDbtn1 = Button(STDfunc)
            STDbtn1.config(text = '도서관 이용하기', width = 20, command = LB )
            STDbtn1.grid(row = 0, column = 0, padx = 5, pady = 10)
            
            STDbtn2 = Button(STDfunc)
            STDbtn2.config(text = '질문 게시판', width = 20, command = create_main_window)
            STDbtn2.grid(row = 1, column = 0, padx = 5, pady = 10)

            STDbtn3 = Button(STDfunc)
            STDbtn3.config(text = '자기 계발 열람실 확인하기', width = 20, command = main)
            STDbtn3.grid(row = 2, column = 0, padx = 5, pady = 10)
           
            STDbtn5 = Button(STDfunc)
            STDbtn5.config(text = '공지 확인하기', width = 20, command = main4)
            STDbtn5.grid(row = 0, column = 1, padx = 100, pady = 30)
   
            STDbtn6 = Button(STDfunc)
            STDbtn6.config(text = '전주대학교 지도 보기', width = 20, command = main6)
            STDbtn6.grid(row = 1, column = 1, padx = 100, pady = 30)
       
            STDbtn7 = Button(STDfunc)
            STDbtn7.config(text = '과제 제출하기', width = 20, command = main2)
            STDbtn7.grid(row = 2, column = 1, padx = 100, pady = 30)
            
            STDfunc.mainloop()
        else:
            messagebox.showwarning("로그인 실패", "저희 회원이 아니십니다. 회원가입 후 로그인 해주세요.")

    btn1 = Button(JJ2)
    btn1.config(text = "로그인", command = Login)
    btn1.pack()

    btn2 = Button(JJ2)
    btn2.config(text = "회원가입", command = rgsEvent1)
    btn2.pack()
    JJ2.mainloop()

#교수 로그인창 코드
def btnEvent2():
    JJ3 = Tk()
    JJ3.title("교수 로그인창")
    JJ3.geometry("400x200")

    lab1 = Label(JJ3)
    lab1.config(text = "ID")
    lab1.pack()

    ent1 = Entry(JJ3)
    ent1.pack()

    lab2 = Label(JJ3)
    lab2.config(text = "Password")
    lab2.pack()

    ent2 = Entry(JJ3)
    ent2.config(show = "*")
    ent2.pack()

    def Login():
        userID = ent1.get()
        userPassword = ent2.get()

        if userID in users and users[userID] == userPassword:
            messagebox.showinfo("로그인 성공", "교수 로그인 성공")
            JJ3.destroy()

            #교수 기능 화면 코드
            PROfunc = Tk()
            PROfunc.title("교수 기능")
            PROfunc.geometry('450x350')

            PRObtn1 = Button(PROfunc)
            PRObtn1.config(text = '과제 등록하기', width = 20, command = main3)
            PRObtn1.grid(row = 0, column = 0, padx = 5, pady = 10)
                           
            PRObtn5 = Button(PROfunc)
            PRObtn5.config(text = '공지 등록하기', width = 20, command = main5)
            PRObtn5.grid(row = 0, column = 1, padx = 100, pady = 30)

            PROfunc.mainloop()
        else:
            print("저희 회원이 아니십니다. 회원가입 후 로그인 해주세요.")

    btn1 = Button(JJ3)
    btn1.config(text = "로그인", command = Login)
    btn1.pack()

    btn2 = Button(JJ3)
    btn2.config(text = "회원가입", command = rgsEvent1)
    btn2.pack()
    JJ3.mainloop()

#메인화면 코드
JJ1 = Tk()
JJ1.title("JJ 학생 교수 교류앱")
JJ1.geometry("400x200")
lab = Label(JJ1, text = "이용할 기능을 선택해주세요")
lab.pack(side = 'top')
frame = Frame(JJ1)
btn1 = Button(frame, text = '학생', command = btnEvent1, width = 20)
btn1.pack(side = 'left')
btn2 = Button(frame, text = '교수', command = btnEvent2, width = 20)
btn2.pack(side = 'right')
frame.pack(side = 'top')

#도서관 메인 화면
def LB():
    JJ5 = Toplevel()
    JJ5.title("도서관 기능 선택하기")
    JJ5.geometry("400x200")
    btn1 = Button(JJ5, text = "게시판 이용하기", command = openpost ,width = 20)
    btn1.pack(side = 'left')
    btn2 = Button(JJ5, text = "도서관 자리 예약하기", command = open_reservation ,width = 20 )
    btn2.pack(side = 'right')

#도서관 게시판 이용 화면
def openpost():
    global IDentry, NAMEentry, CONTENTentry, display_area  

    root = Toplevel()
    root.title("게시판")
    root.geometry("400x400")

    IDlabel = Label(root, text="학번:")
    IDlabel.grid(column=0, row=0, padx=10, pady=5)
    IDentry = Entry(root, width=20)
    IDentry.grid(column=1, row=0, padx=10, pady=5)

    NAMElabel = Label(root, text="이름:")
    NAMElabel.grid(column=0, row=1, padx=10, pady=5)
    NAMEentry = Entry(root, width=20)
    NAMEentry.grid(column=1, row=1, padx=10, pady=5)

    CONTENTlabel = Label(root, text="내용:")
    CONTENTlabel.grid(column=0, row=2, padx=10, pady=5)
    CONTENTentry = Entry(root, width=40)
    CONTENTentry.grid(column=1, row=2, padx=10, pady=5)

    POSTbutton = Button(root, text="게시", command=POSTmessage)
    POSTbutton.grid(column=1, row=3, padx=10, pady=5)

    display_area = scrolledtext.ScrolledText(root, width=50, height=15, wrap=WORD)
    display_area.grid(column=0, row=4, columnspan=2, padx=10, pady=10)
    display_area.config(state=DISABLED)  # Read-only

def POSTmessage():
    studentID = IDentry.get()
    studentNAME = NAMEentry.get()
    content = CONTENTentry.get()

    if studentID and studentNAME and content:
        post = f"{studentNAME} ({studentID}):\n{content}\n\n"
        display_area.config(state=NORMAL)
        display_area.insert(END, post)
        display_area.config(state=DISABLED)
        clear_entries()
    else:
        messagebox.showwarning("입력 오류", "모든 입력칸에 입력해 주세요.")

def clear_entries():
    IDentry.delete(0, END)
    NAMEentry.delete(0, END)
    CONTENTentry.delete(0, END)

#도서관 자리 예약 프로그램
def open_reservation():
    res_root = Toplevel(JJ1)
    res_root.title("도서관 자리 예약 프로그램")
    res_root.geometry("650x200")

    seats = {}
    create_seats(res_root, seats)
def create_seats(root, seats):
    for r in range(3):
        for c in range(5):
            seat = f"R{r+1}C{c+1}"
            btn = Button(root, text=seat, width=15, height=3, bg="green",
                         command=lambda s=seat: reser_button(s, seats))
            btn.grid(row=r, column=c, padx=5, pady=5)
            seats[seat] = btn

def reser_button(seat, seats):
    btn = seats[seat]
    if btn.cget('bg') == 'green':
        twopage_reser(seat, seats)
    else:
        messagebox.showinfo("예약 불가", f"{seat} 자리는 이미 예약되었습니다.")

def twopage_reser(seat, seats):
    popup = Toplevel()
    popup.title("자리 예약")
    popup.geometry("300x200")

    Label(popup, text="학번:").pack(pady=5)
    id_entry = Entry(popup)
    id_entry.pack(pady=5)

    Label(popup, text="이름:").pack(pady=5)
    name_entry = Entry(popup)
    name_entry.pack(pady=5)

    def save():
        sid = id_entry.get()
        name = name_entry.get()
        if sid and name:
            btn = seats[seat]
            btn.config(bg='red', text=name)
            btn.config(command=lambda s=seat: cancel(s, seats))
            messagebox.showinfo("예약 완료", f"{seat} 자리가 {name}님에게 예약되었습니다.")
            popup.destroy()
        else:
            messagebox.showwarning("입력 오류", "모든 정보를 입력해주세요.")

    Button(popup, text="예약", command=save).pack(pady=20)

def cancel(seat, seats):
    btn = seats[seat]
    if btn.cget('bg') == 'red':
        btn.config(bg='green', text=seat)
        btn.config(command=lambda s=seat: reser_button(s, seats))
        messagebox.showinfo("예약 취소", f"{seat} 자리 예약이 취소되었습니다.")

#자기계발
def main():  # 학과 챌린지 및 데이터 초기화
    context = {"departments": {"반려동식물학과": ["식물 기르기", "유기견 봉사활동", "애완동물 훈련", "정원 가꾸기", "동물과 교감"],
            "경영학과": ["한 달 자금 관리", "마케팅 계획 작성", "경영 관련 책 읽기", "기업가 정신 워크샵 참석", "CEO 강연 듣기"],
            "한식조리학과": ["한식 요리 만들기", "전통 음식 연구", "쿠킹 클래스 참여", "한식 조리법 배우기", "한식을 통해 지역 문화와 풍속 이해하기"],
            "공연방송연기학과": ["공연 참여", "방송 프로듀싱 배우기", "단편 영화 제작", "연기 워크샵", "특별 공연 관람"],
            "컴퓨터공학과": ["코딩 하기", "알고리즘 문제 해결", "프로젝트 활동", "해킹 보안 연구", "프로그래밍 언어 배우기"],
            "간호학과": ["간호 실습", "환자 돌보기", "응급 처치 훈련", "의료 기기 사용 연습", "의료 봉사활동"],
            "소방안전공학과": ["화재 예방 훈련", "안전 점검 연습", "소방 장비 사용 훈련", "화재 시뮬레이션 참여", "화재 예방 영상 창작"],
            "수학교육과": ["수학 문제 풀이", "교육 자료 만들기", "수학 교육 연구", "교구 개발", "수학 퍼즐 창작"],
            "상담심리학과": ["상담 실습", "심리 테스트 연구", "집단 상담 참여", "심리학 논문 읽기", "상담 기술 체험"],
            "영어영문학과": ["영어 에세이 쓰기", "영문학 작품 분석", "영어 토론 참여", "번역 연습", "3분 영어 대화"]},
        "progress": 0,
        "activityCount": 0,
        "challengeCount": 0,
        "cultureCount": 0,
        "currentDepartment": None,
        "currentActivity": None,
        "currentChallenge": None,
        "current_activity_type": None}

    win = Toplevel()
    win.title("자기계발")
    context["win"] = win

    lbDepartment = Label(win, text="학과 탐색")
    lbDepartment.pack()

    btnDepartment = Button(win, text="학과 랜덤 추천", command=lambda: random_department(context))
    btnDepartment.pack()

    lbChallenge = Label(win, text="학과 챌린지")
    lbChallenge.pack()

    btnChallenge = Button(win, text="챌린지 참여", command=lambda: join_challenge(context))
    btnChallenge.pack()

    lbActivity = Label(win, text="문화 활동")
    lbActivity.pack()

    btnActivity = Button(win, text="활동 추천", command=lambda: recommend_activity(context))
    btnActivity.pack()

    btn_certify_activity = Button(win, text="활동 인증", command=lambda: certify_activity(context), state="disabled")
    btn_certify_activity.pack()
    context["btn_certify_activity"] = btn_certify_activity
    
def random_department(context):  # 학과 추천
    context["currentDepartment"] = random.choice(list(context["departments"].keys()))
    messagebox.showinfo("랜덤 학과 추천", f"추천 학과: {context['currentDepartment']}")
    return context

def join_challenge(context):  # 학과 챌린지 참여
    if context["currentDepartment"]:
        challenges = context["departments"][context["currentDepartment"]]
        context["currentChallenge"] = random.choice(challenges)
        context["current_activity_type"] = "challenge"
        messagebox.showinfo("챌린지 참여", f"챌린지: {context['currentChallenge']}\n활동을 인증하고 '활동 인증' 버튼을 눌러주세요.")
        context["btn_certify_activity"].config(state="normal")
    else:
        messagebox.showwarning("오류", "먼저 학과를 추천받으세요.")
    return context

def recommend_activity(context):  # 문화 활동 추천
    activities = ["운동", "여행", "요리", "악기 배우기", "미술 수업", "서점 투어", "박물관 방문", "음악 공연 관람", "사진 전시회", "영화 감상", "독서 모임", "요가 수업", "드라이브", "자격증 공부", "토익 공부"]
    context["currentActivity"] = random.choice(activities)
    context["current_activity_type"] = "activity"
    messagebox.showinfo("문화 활동 추천", f"추천 활동: {context['currentActivity']}\n활동을 인증하고 '활동 인증' 버튼을 눌러주세요.")
    context["btn_certify_activity"].config(state="normal")
    return context

def certify_activity(context):  # 활동 인증
    if context["currentChallenge"] or context["currentActivity"]:
        options = ["블로그 포스팅", "SNS 공유", "동영상 업로드", "사진 업로드"]
        activityType = simpledialog.askstring("활동 인증", "어떤 방법으로 활동을 인증하시겠습니까?", parent=context["win"], 
                                              initialvalue=random.choice(options))
        if activityType:
            messagebox.showinfo("활동 인증 완료", f"활동이 {activityType}(으)로 인증되었습니다.")
            context = track_activity(context)
        else:
            messagebox.showwarning("인증 오류", "인증 방법을 선택하세요.")
    else:
        messagebox.showwarning("오류", "먼저 활동을 선택하세요.")
    return context

def track_activity(context):  # 활동 추적
    if context["current_activity_type"] == "challenge":
        context["challengeCount"] += 1
        if context["challengeCount"] == 5:
            context = grant_reward(context, "challenge")
            context["challengeCount"] = 0
    elif context["current_activity_type"] == "activity":
        context["cultureCount"] += 1
        if context["cultureCount"] == 5:
            context = grant_reward(context, "activity")
            context["cultureCount"] = 0

    context["activityCount"] += 1  # 진행률 업데이트
    if context["activityCount"] % 4 == 0:
        context["progress"] += 25
        if context["progress"] >= 100:
            messagebox.showinfo("목표 달성", f"축하합니다! 자기계발 목표를 달성했습니다. 보상: {get_progress_reward(context['progress'])}")
            context["progress"] = 0
            context["activityCount"] = 0
        else:
            reward = get_progress_reward(context["progress"])
            messagebox.showinfo("진행률 상황", f"진행률 {context['progress']}% 달성! 보상: {reward}")

    context["currentChallenge"] = None
    context["currentActivity"] = None
    context["current_activity_type"] = None
    context["btn_certify_activity"].config(state="disabled")
    return context

def grant_reward(context, activity_type):  # 챌린지, 문화 활동 보상 설정  
    if activity_type == "challenge":  # 학과 챌린지 참여 보상
        rewards = ["전문 서적", "워크샵 참여권", "온라인 강의 쿠폰", "전문가 멘토링 세션", "학습 자료", "연구 지원금", "학회 참여권", "프로젝트 기금"]
        reward = random.choice(rewards)
    else:  # activity_type == "activity", 문화 활동 보상
        rewards = {"운동": ["운동용품 할인권", "운동복 세트", "체육시설 무료 이용권", "피트니스 앱 구독권", "pt 2회 무료"],
            "여행": ["여행 할인권", "항공사 마일리지", "호텔 숙박권", "캐리어", "랜터카 무료 대여"],
            "요리": ["음식 재료 할인권", "조리도구 할인권", "요리 교실 무료 참여", "특별 레시피북", "요리도구 세트"],
            "악기 배우기": ["악기 레슨 할인권", "음악 앨범", "음악 학원 수강권", "악기 구매 할인권", "무료 전문 레슨 1회"],
            "미술 수업": ["미술용품 할인권", "전시회 티켓", "미술 워크샵 참가권", "디지털 드로잉 태블릿", "미술 책 증정"],
            "서점 투어": ["도서 쿠폰", "서적 할인권", "문학세미나 참가권", "작가 사인본 책", "독서 클럽 멤버십"],
            "박물관 방문": ["박물관 입장권", "기념품샵 상품권", "박물관 투어 이용권", "특별 전시회 초대권", "박물관 테마 굿즈"],
            "음악 공연 관람": ["음악 공연 티켓", "음악 앨범", "음악 강습 수강권", "콘서트 VIP 티켓", "음악 서비스 프리미엄 이용권"],
            "사진 전시회": ["사진 전시회 티켓", "사진 전문 카메라", "사진 워크샵 참가권", "카메라 장비 할인권", "전시회 기념품"],
            "영화 감상": ["영화 티켓", "영화 관람 쿠폰", "영화 굿즈", "팝콘/음료 세트 쿠폰", "영화 서비스 프리미엄 이용권"],
            "독서 모임": ["책 쿠폰", "독서 모임 참여권", "독서 토론 세미나", "독서 일기장", "독서 모임 참여 포인트"],
            "요가 수업": ["요가 무료 수업", "요가 매트", "요가복 세트", "요가 보조도구", "요가 수업료 할인"],
            "드라이브": ["차량 무료 점검 쿠폰", "차량 내부 클리닝 서비스", "주유 상품권", "무료 세차", "차량 관리 용품"],
            "자격증 공부": ["자격증 시험료 지원", "자격증 교재", "온라인 강의 수강권", "온라인 시험 응시권", "자격증 발급 수수료 면제"],
            "토익 공부": ["토익 시험료 지원", "토익 교재", "온라인 모의고사 무료 이용권", "어학원 수강권", "학습 자료 증정"]}

        reward = random.choice(rewards.get(context["currentActivity"], ["보상 없음"]))
    messagebox.showinfo("보상 받기", f"보상: {reward}\n활동이 완료되었습니다!")
    return context

def get_progress_reward(progress):  # 진행률에 따른 보상 설정
    rewards = {25: ["문화 상품권 2장", "차/커피 선물세트", "향초", "과자 선물 박스"],
        50: ["블루투스 헤드폰", "손목시계", "휴대용 스피커", "문화활동 할인권"],
        75: ["특별 강연 초청권", "학습 자료 증정", "미니 공기 청정기", "레저 시설 이용권"],
        100: ["연구비용 전액 지원", "해외 학회 참여비 지원", "국제 학술대회 초청권", "전문 프로젝트 참가 기회권 "]}
    return random.choice(rewards.get(progress, ["보상 없음"]))

#질문게시판
questions = []
tips = []

# 메인 화면 생성
def create_main_window():
    global main1
    main1 = Toplevel()
    main1.geometry('500x350')
    main1.title("질문게시판")

    # 출력 프레임
    display_frame = Frame(main1)
    display_frame.pack()

    # 검색 프레임
    search_frame = Frame(display_frame)
    search_frame.pack()

    # 질문 프레임
    question_frame = Frame(display_frame)
    question_frame.pack(side='bottom')

    # 검색 입력
    global search_entry
    search_entry = Entry(search_frame, width=20)
    search_entry.pack(side='left')

    # 검색 버튼
    search_button = Button(search_frame, text='검색', command=search_question)
    search_button.pack(side='right')

    # 리스트박스 생성 + 스크롤바
    global question_listbox
    question_listbox = Listbox(display_frame, height=15, width=50)
    question_listbox.pack(side='left', padx=5, pady=5)

    scrollbar = Scrollbar(display_frame)
    scrollbar.pack(side='right', fill='y')
    question_listbox.config(yscrollcommand=scrollbar.set)
    scrollbar.config(command=question_listbox.yview)

    # 질문 입력
    global question_entry
    question_entry = Entry(question_frame)
    question_entry.pack(side='left')

    # 답변 버튼
    answer_button = Button(question_frame, text='답변', command=answer_question)
    answer_button.pack(side='right')

    # 삭제 버튼
    delete_button = Button(question_frame, text='삭제', command=delete_question)
    delete_button.pack(side='right')

    # Tip 게시판 버튼
    tip_button = Button(main1, text='Tip 게시판', command=open_tip_board)
    tip_button.pack()

    # 질문 버튼
    ask_button = Button(question_frame, text='질문', command=add_question)
    ask_button.pack(side='right')

    # 더블클릭 이벤트 바인딩
    question_listbox.bind('<Double-Button-1>', double_click_question)

# 질문을 리스트박스에 추가하는 함수
def add_question():
    question_text = question_entry.get()
    if question_text:
        questions.append({"question": question_text, "answer": None})
        question_listbox.insert(END, question_text)
        question_entry.delete(0, END)

# 질문 삭제 함수
def delete_question():
    selected_index = question_listbox.curselection()
    if selected_index:
        question_listbox.delete(selected_index)
        del questions[selected_index[0]]

# 검색 함수
def search_question():
    search_text = search_entry.get()
    question_listbox.delete(0, END)
    for qa in questions:
        if search_text in qa["question"]:
            question_listbox.insert(END, qa["question"])

# 답변 버튼 함수
def answer_question():
    selected_index = question_listbox.curselection()
    if selected_index:
        selected_question = questions[selected_index[0]]["question"]
        answer_window = Toplevel(main1)
        answer_window.geometry('300x450')
        answer_window.title('답변 작성')

        lbl = Label(answer_window, text=f"질문: {selected_question}")
        lbl.pack(pady=10)

        answer_listbox_frame = Frame(answer_window)
        answer_listbox_frame.pack(pady=10)
        answer_listbox = Listbox(answer_listbox_frame)
        answer_listbox.pack(pady=30)

        answer_entry = Entry(answer_window, width=50)
        answer_entry.pack(side='bottom', pady=50)

        def submit_answer():
            answer_text = answer_entry.get()
            if answer_text:
                questions[selected_index[0]]["answer"] = answer_text
                answer_listbox.insert(END, answer_text)
                answer_entry.delete(0, END)

                question_listbox.delete(selected_index)
                question_listbox.insert(selected_index, f'{selected_question} - 답변이 있습니다.')

        submit_button = Button(answer_window, text='제출', command=submit_answer)
        submit_button.pack(side='bottom', pady=10)

# 팁 게시판 열기 함수
def open_tip_board():
    tip_board_window = Toplevel(main1)
    tip_board_window.geometry('300x200')
    tip_board_window.title('직급')
    rank_var = StringVar()
    rank_var.set(None)
    def open_tip():
        rank = rank_var.get()
        if rank:
            one_window = Toplevel(main1)
            one_window.geometry('300x250')
            one_window.title('팁 창')
            lbl = Label(one_window, text=f'{rank} 팁 창입니다.')
            lbl.pack(side='top')

            tip_listbox = Listbox(one_window)
            tip_listbox.pack(padx=10, pady=10)

            def add_tip():
                two_window = Toplevel(one_window)
                two_window.geometry('300x250')
                two_window.title('팁 창')

                tip_entry = Entry(two_window)
                tip_entry.pack(side='top')

                tip_text = Text(two_window, height=10)
                tip_text.pack(side='top', pady=10)

                def submit_tip():
                    tip_title = tip_entry.get()
                    tip_content = tip_text.get('1.0', END).strip()
                    tip_listbox.insert(END, tip_title)
                    tip_entry.delete(0, END)
                    tips.append({'title': tip_title, 'content': tip_content})

                def show_tip(event):
                    selected_index = tip_listbox.curselection()
                    if selected_index:
                        selected_index = selected_index[0]
                        selected_tip = tips[selected_index]

                        three_window = Toplevel(one_window)
                        three_window.geometry('300x350')
                        three_window.title('팁')

                        tip_content_text = Text(three_window, height=30)
                        tip_content_text.pack(side='top', pady=10)
                        tip_content_text.insert(END, selected_tip['content'])

                tip_listbox.bind('<Double-1>', show_tip)

                submit_button = Button(two_window, text='제출', command=submit_tip)
                submit_button.pack(side='bottom', pady=10)

            add_tip_button = Button(one_window, text='글쓰기', command=add_tip)
            add_tip_button.pack(side='right', padx=10, pady=10)

    select_button = Button(tip_board_window, text='선택', command=open_tip)
    select_button.pack(side='bottom')

    rank1_button = Radiobutton(tip_board_window, text='1학년', variable=rank_var, value='1학년')
    rank2_button = Radiobutton(tip_board_window, text='2학년', variable=rank_var, value='2학년')
    rank3_button = Radiobutton(tip_board_window, text='3학년', variable=rank_var, value='3학년')
    rank4_button = Radiobutton(tip_board_window, text='4학년', variable=rank_var, value='4학년')
    professor_button = Radiobutton(tip_board_window, text='교수', variable=rank_var, value='교수')

    professor_button.pack(side='bottom')
    rank4_button.pack(side='bottom')
    rank3_button.pack(side='bottom')
    rank2_button.pack(side='bottom')
    rank1_button.pack(side='bottom')

    lbl = Label(tip_board_window, text='자신의 직급을 선택해 주세요')
    lbl.pack(side='top', padx=5, pady=5)

# 더블클릭 이벤트 처리 함수
def double_click_question(event):
    selected_index = question_listbox.curselection()
    if selected_index:
        show_question_details()

# 질문 확인 함수
def show_question_details():
    selected_index = question_listbox.curselection()
    if selected_index:
        selected_question = questions[selected_index[0]]["question"]
        selected_answer = questions[selected_index[0]]["answer"]

        details_window = Toplevel(main1)
        details_window.geometry('300x300')
        details_window.title('답변 확인')

        lbl = Label(details_window, text=f"질문: {selected_question}")
        lbl.pack(pady=10)

        answer_frame = Frame(details_window)
        answer_frame.pack(pady=10)
        answer_listbox = Listbox(answer_frame)
        answer_listbox.pack(pady=30)

        if selected_answer:
            answer_listbox.insert(END, selected_answer)

gwandata = {}  # 작성한 내용을 기억합니다.
yunlist = []  # 교수 창에서 새로 생성되는 버튼을 저장합니다.
yunlists = []  # 학생 창에서 새로 생성되는 버튼을 저장합니다.
smnlist = {}  #제출 버튼을 눌렀을 때 내용을 저장합니다.
months = ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월']  # 월이 저장된 리스트 입니다.

def radiobutton1(plus, txt, vie, vle, row, cln):
    radiobutton1 = Radiobutton(plus, text=txt, variable=vie, value=vle)
    radiobutton1.grid(row=row, column=cln)
    return radiobutton1

def calendar11(month):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29
    else:
        return 31

def yun1(day):  # 정확한 day값을 전달하기 위해 이렇게 작성했습니다.
    def Lee1():
        openbutton1(day)
    return Lee1

def openbutton1(day):
    new = Toplevel()  # 해당 날짜에 과제쓰는 칸을 출력합니다.
    new.title('%s일' % day)

    write = Text(new, font=("돋움", 12), width=70, height=25)
    write.grid(row=0, column=0, columnspan=2)
    st = Label(new, text="", font=("돋움", 12))
    st.grid(row=2, column=0, columnspan=2)

    # 제출 버튼 명령을 실행하는 함수입니다.
    def submit():
        new.config(bg="lightgreen")
        write.config(fg="lightgreen", bg="lightgreen")
        st.config(text="제출되었습니다.", fg="black", bg="lightgreen")
        smnlist[day] = write.get("1.0", END).strip() # 제출한 내용을 저장합니다
        del gwandata[day]

    if day in gwandata:
        write.insert(END, gwandata[day])  # 입력된 내용이 있으면 출력합니다.
        stbutton = Button(new, text="제출", width=25, command=submit)
        stbutton.grid(row=1, column=1)  # 입력된 내용이 있으면 제출 버튼이 생성됩니다.

    # 확인 버튼을 누르면 창을 닫습니다.
    def guisave1():
        new.destroy()

    yunsave = Button(new, text="확인", width=25, command=guisave1)
    yunsave.grid(row=1, column=0)

def oneday1():
    manymonth = radios.get()  # 라디오 버튼에서 선택된 값을 저장합니다.
    if manymonth:
        monthchoice = months.index(manymonth) + 1

        for button in yunlists:
            button.destroy()
        yunlists.clear()

        for day in range(1, calendar11(monthchoice) + 1):  # 버튼의 행, 열을 계산합니다.
            row = (day - 1) // 7 + 2
            cln = (day - 1) % 7
            button = plusbutton1(gwans, '%s일' % day, row, cln, yun1(day))
            yunlists.append(button)

# 버튼 추가 함수입니다.
def plusbutton1(plus, txt, row, cln, cmd):
    button = Button(plus, text=txt, command=cmd, font=("돋움", 14), width=6, height=3)
    button.grid(row=row, column=cln)
    return button

# 우선순위에 따라 과제를 정렬합니다.
def rank1():
    sortedlist = sorted(gwandata.items())  # sorted로 딕셔너리를 정렬하고 대입했습니다.
    new2 = Toplevel()
    new2.title("우선순위")

    write2 = Text(new2, font=("돋움", 12), width=70, height=25)
    write2.grid(row=0, column=0)

    for key, data in sortedlist:
        write2.insert(END, "%s일\n%s\n\n" % (key, data))

    close = Button(new2, text="확인", command=new2.destroy)
    close.grid(row=1, column=0)

def main2():
    global gwans, radios
    gwans = Toplevel()
    gwans.title('2024년도 과제 확인 창')
    gwans.geometry("500x416")

    start = Button(gwans, text='적용', width=7, command=oneday1)
    start.grid(row=0, column=6)

    rankbtn = Button(gwans, text='우선순위', command=rank1)
    rankbtn.grid(row=1, column=6)

    radios = StringVar()
    radios.set(None)
    # 라디오 버튼을 생성하는 함수의 값들을 대입합니다.
    for i in range(6):
        radiobutton1(gwans, months[i], radios, months[i], 0, i)
    for i in range(6, 12):
        radiobutton1(gwans, months[i], radios, months[i], 1, i - 6)

# 라디오 버튼을 생성하는 함수
def radiobutton(plus, txt, vie, vle, row, cln):
    radiobutton = Radiobutton(plus, text=txt, variable=vie, value=vle)
    radiobutton.grid(row=row, column=cln)
    return radiobutton

# 달마다 다른 일 수를 계산하는 함수
def calendar1(month):
    if month in [4, 6, 9, 11]:
        return 30
    elif month == 2:
        return 29
    else:
        return 31

def yun(day):  # 정확한 day값을 전달하기 위해 이렇게 작성했습니다.
    def Lee():
        openbutton(day)
    return Lee

def openbutton(day):
    new = Toplevel()  # 해당 날짜에 과제쓰는 칸을 출력합니다.
    new.title('%s일' % day)

    write = Text(new, font=("돋움", 12), width=70, height=25)
    write.grid(row=0, column=0, columnspan=2)
    
    if day in gwandata:
        write.insert(END, gwandata[day])  # 입력된 내용이 있으면 출력합니다.
    if day in smnlist:
        write.insert(END, smnlist[day])  # 제출된 내용이 있으면 출력합니다.

    # 저장 버튼을 실행하는 함수
    def guisave():
        gwandata[day] = write.get("1.0", END).strip()  # 입력한 내용을 저장합니다.
        if day in smnlist:
            del smnlist[day]
        new.destroy()

    yunsave = Button(new, text="저장", width=25, command=guisave)
    yunsave.grid(row=1, column=0, columnspan=2)

def oneday():
    manymonth = radio.get()  # 라디오 버튼에서 선택된 값을 저장합니다.
    if manymonth:
        monthchoice = months.index(manymonth) + 1

        for button in yunlist:
            button.destroy()
        yunlist.clear()

        for day in range(1, calendar1(monthchoice) + 1):  # 버튼의 행, 열을 계산합니다.
            row = (day - 1) // 7 + 2
            cln = (day - 1) % 7
            button = plusbutton(gwan, '%s일' % day, row, cln, yun(day))
            yunlist.append(button)

# 버튼 추가 함수
def plusbutton(plus, txt, row, cln, cmd):
    button = Button(plus, text=txt, command=cmd, font=("돋움", 14), width=6, height=3)
    button.grid(row=row, column=cln)
    return button

# 우선순위에 따라 과제를 정렬합니다.
def rank():
    sortedlist = sorted(gwandata.items())  # sorted로 딕셔너리를 정렬하고 대입했습니다.
    new2 = Toplevel()
    new2.title("우선순위")

    write2 = Text(new2, font=("돋움", 12), width=70, height=25)
    write2.grid(row=0, column=0)

    for key, data in sortedlist:
        write2.insert(END, "%s일\n%s\n\n" % (key, data))

    close = Button(new2, text="확인", command=new2.destroy)
    close.grid(row=1, column=0)

def main3():
    global gwan, radio
    gwan = Toplevel()
    gwan.title('2024년도 과제 작성 창')
    gwan.geometry("500x416")

    start = Button(gwan, text='적용', width=7, command=oneday)
    start.grid(row=0, column=6)

    rankbtn = Button(gwan, text='우선순위', command=rank)
    rankbtn.grid(row=1, column=6)

    radio = StringVar()
    radio.set(None)
    # 라디오 버튼을 생성하는 함수의 값들을 대입합니다.
    for i in range(6):
        radiobutton(gwan, months[i], radio, months[i], 0, i)
    for i in range(6, 12):
        radiobutton(gwan, months[i], radio, months[i], 1, i - 6)

def display_notices():
    try:
        with open("notices.txt", "r") as file:
            notices = file.readlines()
        if len(notices) == 0:
            text_notice.config(state="normal")
            text_notice.delete("1.0", "end")
            text_notice.insert("end", "공지가 없습니다.")
            text_notice.config(state="disabled")
        else:
            text_notice.config(state="normal")
            text_notice.delete("1.0", "end")
            for notice in notices:
                text_notice.insert("end", notice)
            text_notice.config(state="disabled")
    except FileNotFoundError:
        text_notice.config(state="normal")
        text_notice.delete("1.0", "end")
        text_notice.insert("end", "공지가 없습니다.")
        text_notice.config(state="disabled")

def main4():
    global text_notice
    root = Toplevel()
    root.title("학생용 공지 확인 프로그램")

    text_notice = Text(root, width=50, height=10)
    text_notice.grid(row=0, column=0, padx=5, pady=5)

    btn_refresh = Button(root, text="새로고침", command=display_notices)
    btn_refresh.grid(row=1, column=0, padx=5, pady=5)

    display_notices()  

def add_notice():
    title = entry_title.get()
    content = text_content.get("1.0", "end-1c")
    if title.strip() == "" or content.strip() == "":
        messagebox.showerror("Error", "공지 제목과 내용을 모두 입력하세요.")
    else:
        with open("notices.txt", "a") as file:
            file.write(f"{title}\n{content}\n\n")
        messagebox.showinfo("Success", "공지가 등록되었습니다.")
        entry_title.delete(0, "end")
        text_content.delete("1.0", "end")

def delete_notice():
    try:
        with open("notices.txt", "r") as file:
            notices = file.readlines()
        if len(notices) == 0:
            messagebox.showinfo("Info", "삭제할 공지가 없습니다.")
        else:
            with open("notices.txt", "w") as file:
                file.writelines(notices[:-3])  
            messagebox.showinfo("Success", "가장 최근에 등록된 공지가 삭제되었습니다.")
    except FileNotFoundError:
        messagebox.showerror("Error", "삭제할 공지가 없습니다.")

def modify_notice():
    title = entry_title.get()
    content = text_content.get("1.0", "end-1c")
    if title.strip() == "" or content.strip() == "":
        messagebox.showerror("Error", "공지 제목과 내용을 모두 입력하세요.")
    else:
        try:
            with open("notices.txt", "r") as file:
                notices = file.readlines()
            if len(notices) == 0:
                messagebox.showinfo("Info", "수정할 공지가 없습니다.")
            else:
                with open("notices.txt", "w") as file:
                    modified = False
                    for i in range(len(notices)):
                        if notices[i].strip() == title:  
                            file.write(f"{title}\n{content}\n\n")
                            modified = True
                        else:
                            file.write(notices[i])
                    if not modified:
                        messagebox.showinfo("Info", "해당 공지가 존재하지 않습니다.")
                    else:
                        messagebox.showinfo("Success", "공지가 수정되었습니다.")
                        entry_title.delete(0, "end")
                        text_content.delete("1.0", "end")
        except FileNotFoundError:
            messagebox.showerror("Error", "수정할 공지가 없습니다.")

def main5():
    global entry_title, text_content

    root = Toplevel()
    root.title("교수용 공지 프로그램")

    label_title = Label(root, text="공지 제목:")
    label_title.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    entry_title = Entry(root, width=50)
    entry_title.grid(row=0, column=1, padx=5, pady=5)

    label_content = Label(root, text="공지 내용:")
    label_content.grid(row=1, column=0, padx=5, pady=5, sticky="ne")

    text_content = Text(root, width=50, height=10)
    text_content.grid(row=1, column=1, padx=5, pady=5)

    btn_add = Button(root, text="등록", command=add_notice)
    btn_add.grid(row=2, column=0, padx=5, pady=5)

    btn_delete = Button(root, text="삭제", command=delete_notice)
    btn_delete.grid(row=2, column=1, padx=5, pady=5)

    btn_modify = Button(root, text="수정", command=modify_notice)
    btn_modify.grid(row=2, column=2, padx=5, pady=5)

def main6():
    winyun = Toplevel()
    winyun.title("전주대 지도")
    img = PhotoImage(file="c:\\temp\\전주대 지도3.png")
    lll = Label(winyun, image=img)
    lll.image = img
    lll.pack()

JJ1.mainloop()
