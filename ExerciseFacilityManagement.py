import random, time

class Gym:
    def __init__(self):  # 샤워실, 운동 공간, 운동 기구, 회원 정보, 예약 슬롯 등 초기화
        self.showerRooms = {"샤워실 1": ["샤워실 1"], "샤워실 2": ["샤워실 2"], "샤워실 3": ["샤워실 3"], "샤워실 4": ["샤워실 4"]}
        self.areas = ["유산소실", "근력운동실", "전신운동실", "상체운동실", "하체운동실"]
        self.equipment = {"유산소실": ["트레드밀", "사이클", "런닝머신", "스텝퍼"],
            "근력운동실": ["벤치프레스", "레그프레스", "플랭크보드", "덤벨"],
            "전신운동실": ["스미스머신", "슬램볼", "케틀벨", "웨이트벤치"],
            "상체운동실": ["바벨", "벤치", "플라이머신", "케이블머신"],
            "하체운동실": ["더스트랩", "스텝박스", "레그컬 머신", "스쿼트랙"]}
        self.members = {}  # 회원 정보 저장을 위한 딕셔너리
        self.reservationSlots = {"운동기구": {}, "샤워실": {}}  # 예약 현황 저장을 위한 딕셔너리
        self.broken_equipment = set()   # 고장난 운동기구 목록을 저장할 집합

    def add_member(self, user_id, name):  # 회원 ID와 이름을 받아서 회원 정보에 추가
        self.members[user_id] = name

    def reserveEquipment(self, area, equipment, user_id, duration=60):  # 회원 ID 입력 후 존재하는지 확인
        if user_id not in self.members:
            print(user_id,'님은 존재하지 않는 회원 ID입니다.')
            return

        if equipment in self.equipment.get(area, []):  # 해당기구가 지정영역에 있는지 확인
            if equipment not in self.reservationSlots["운동기구"]:  # 운동기구가 예약슬롯에 없으면 예약
              self.reservationSlots["운동기구"][equipment] = {"user_id": user_id, "duration": duration, "endTime": self.calculate_endTime(duration)}
              print(equipment,'예약 완료. 최대',duration,'분까지 사용 가능합니다.')
            else:
              print(equipment,'은(는) 이미 예약되어 있습니다.')
        else:
            print(equipment,'은(는)',area,'에 존재하지 않습니다.')

        if area not in self.areas:
            print(area,'은(는) 존재하지 않는 운동 공간입니다.')
            return

    def reserve_showerRoom(self, showerRoom, user_id, duration=30):  # 회원 ID 입력 후 존재하는지 확인
        if user_id not in self.members:
            print(user_id,'님은 존재하지 않는 회원 ID입니다.')
            return

        if showerRoom in self.showerRooms:  # 샤워실 존재 확인
            if showerRoom not in self.reservationSlots["샤워실"]:  # 샤워실이 예약슬롯에 없으면 예약
                self.reservationSlots["샤워실"][showerRoom] = {"user_id": user_id, "duration": duration, "endTime": self.calculate_endTime(duration)}
                print(showerRoom,'예약 완료. 최대',duration,'분까지 사용 가능합니다.')
            else:
                print(showerRoom,'은(는) 이미 예약되어 있습니다.')
        else:
            print(showerRoom,'은(는) 존재하지 않습니다.')

    def calculate_endTime(self, duration):  # 예약 종료 시간 계산
        current_time = time.localtime()  # 현재 시간
        endTime = time.strftime('%H:%M', time.localtime(time.mktime(current_time) + duration * 60)) # 종료시간 = 현재시간 + 예약시간
        return endTime
        
    def complete_workout(self, user_id):  # 무작위 보상을 선택하여 사용자에게 제공
        if user_id in self.members:
            reward = random.choice(["무료 pt 1회", "닭가슴살 3개", "단백질 쉐이크", "샐러드 2개", "문화상품권 1장","운동용품 할인권", "건강 보조제", "스파 이용권"])
            print(user_id,'님의 <오늘 운동 완료> 이벤트 참여가 완료되었습니다. 보상은',reward,'입니다.')
        else:
            print(user_id,'님은 존재하지 않는 회원 ID입니다.')

    def broken_equipment_report(self, equipment):
        if any(equipment in equipments for equipments in self.equipment.values()):  # 운동 기구가 있다면 해당 운동 기구를 고장 신고 목록에 추가 후 출력 
            self.broken_equipment.add(equipment)
            print(equipment,'운동기구의 고장 신고가 접수되었습니다.')
        else:
            print(equipment,'은(는) 존재하지 않는 운동기구입니다.')

    def display_equipmentStatus(self):  # 운동기구 이용 현황 출력
        print('운동기구 이용 현황:')
        for key, value in self.reservationSlots["운동기구"].items():
            print(f'{key}: {value["user_id"]} 님 예약 중')

    def display_showerRoomStatus(self):  # 샤워실 이용 현황 출력
        print('샤워실 이용 현황:')
        for key, value in self.reservationSlots["샤워실"].items():
            print(f'{key}: {value["user_id"]} 님 예약 중')

    def cancel_equipmentReservation(self, equipment):  # 운동기구 예약 취소
        if equipment in self.reservationSlots["운동기구"]:
            del self.reservationSlots["운동기구"][equipment]
            print(equipment,'예약이 취소되었습니다.')
        else:
            print(equipment,'에 대한 예약을 찾을 수 없습니다.')

    def cancel_showerRoomReservation(self, showerRoom):  # 샤워실 예약 취소
        if showerRoom in self.reservationSlots["샤워실"]:
            del self.reservationSlots["샤워실"][showerRoom]
            print(showerRoom,'예약이 취소되었습니다.')
        else:
            print(showerRoom,'에 대한 예약을 찾을 수 없습니다.')

    def recommend_exercise(self):  # 무작위 운동 공간, 운동 기구 선택하여 사용자에게 추천
        area = random.choice(self.areas)
        equipment = random.choice(self.equipment[area])
        print('오늘의 추천 운동은',area,'의',equipment,'입니다.')

gym = Gym()
while True:
    print("\n =============== 메 뉴 ================")
    print(" 1. 회원 정보")
    print(" 2. 회원 리스트")
    print(" 3. 운동기구 예약")
    print(" 4. 샤워실 예약")
    print(" 5. 운동 완료 및 보상")
    print(" 6. 운동기구 고장 신고")
    print(" 7. 운동기구 이용 현황")
    print(" 8. 샤워실 이용 현황")
    print(" 9. 운동 기구 예약 취소")
    print(" 10. 샤워실 예약 취소")
    print(" 11. 운동 추천")
    print(" 12. 종료")
    print(" ========================================")
    menu = input('메뉴번호 선택 : ')

    if menu == '1':
        id = input('회원 ID: ')
        name = input('이름: ')
        gym.add_member(id, name)
    elif menu == '2':
        for key, value in gym.members.items():
            print(key, value)
    elif menu == '3':
        area = input('운동 공간: ')
        equipment = input('운동기구: ')
        id = input('회원 ID: ')
        gym.reserveEquipment(area, equipment, id)
    elif menu == '4':
        showerRoom = input('샤워실: ')
        user_id = input('회원 ID: ')
        gym.reserve_showerRoom(showerRoom, user_id)
    elif menu == '5':
        user_id = input('회원 ID: ')
        gym.complete_workout(user_id)
    elif menu == '6':
        equipment = input('고장난 운동기구: ')
        gym.broken_equipment_report(equipment)
    elif menu == '7':
        gym.display_equipmentStatus()
    elif menu == '8':
        gym.display_showerRoomStatus()
    elif menu == '9':
        equipment = input('운동기구 이름: ')
        gym.cancel_equipmentReservation(equipment)
    elif menu == '10':
        showerRoom = input('샤워실 이름: ')
        gym.cancel_showerRoomReservation(showerRoom)
    elif menu == '11':
        gym.recommend_exercise()
    elif menu == '12':
        print('감사합니다')
        break
    else:
        print('잘못된 메뉴번호 선택입니다. 다시 선택해주세요.') 
