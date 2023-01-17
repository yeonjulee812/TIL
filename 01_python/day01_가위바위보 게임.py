# 가위바위보 게임 틀 구현
import random

# 필요한 변수 선언 (가위바위보 리스트, 유저/컴퓨터 승 카운트, 판 수)
di = {1:'가위', 2:'바위', 3:'보'}
computer_win_count = 0
user_win_count = 0
game = 1
computer = random.randint(1, 3)

# 종료하기를 입력하거나, 5판을 하기 전까지 무한반복
while True:
    menu = int(input('메뉴를 입력하세요(1: 게임하기, 2: 종료하기): '))
    # 5판 후에는 반복문 종료
    if game == 6:
        break
    
    # 게임하기
    if menu == 1:
        while game < 6:
            user = int(input(f'{game}번째 게임 !\n어떤 것을 내실래요? (1. 가위 / 2. 바위 / 3. 보): '))
            
            # 가위, 바위, 보가 아닌 수를 입력한 경우
            if user not in di.keys():
                print(f'(1. 가위 / 2. 바위 / 3. 보) 중 하나만 입력해주세요! {game}번째 게임을 다시 시작합니다.')
                pass
            
            # 정상적으로 가위, 바위, 보 중 하나를 입력한 경우
            else:
                game += 1

                if computer == user:
                    print(f'비겼습니다!')
                
                elif computer == 1:
                    if user == 2:
                        user_win_count += 1
                        print(f'유저의 승리!')
                    else:
                        computer_win_count += 1
                        print(f'컴퓨터의 승리!')
                
                elif computer == 2:
                    if user == 3:
                        user_win_count += 1
                        print(f'유저의 승리!')
                    else:
                        computer_win_count += 1
                        print(f'컴퓨터의 승리!')
                
                elif computer == 3:
                    if user == 1:
                        user_win_count += 1
                        print(f'유저의 승리!')
                    else:
                        computer_win_count += 1
                        print(f'컴퓨터의 승리!')
                
                print(f'현재 컴퓨터: {computer_win_count}승 / 유저: {user_win_count}승 입니다')
                print('------------------------------------------------------------------------------')

        if user_win_count > computer_win_count:
            print('축하합니다!!! 유저의 승리입니다 !!!\n 프로그램을 종료합니다...')
        elif user_win_count == computer_win_count:
            print('비겼습니다. 아쉬우니 한 판 더??')
        else:
            print('아쉽네요 ㅠ 컴퓨터의 승리입니다 !\n 프로그램을 종료합니다...')
        break

    # 종료하기
    elif menu == 2:
        print('프로그램을 종료합니다')
        break

    # 잘못된 입력 - 안내문 표시 후 다시 반복
    else:
        print('똑바로 입력하쇼')
        pass