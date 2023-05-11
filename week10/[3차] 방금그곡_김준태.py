'''
문제읽기 7:45

노래가 반복되거나 중간에 끊길 수 있어서 문자열 비교 시 유의

#TODO
노래가 재생된 시간을 구하자
8:00

#TODO
조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환한다. 재생된 시간도 같을 경우 먼저 입력된 음악 제목을 반환한다.
8:20

#TODO
문자열 비교 시 #에 주의!
8:10

완료 8:20

후기 : 좀 더 간결하게 가능할 것 같다. 홍록이가 문제 잘못 뽑았다고 할 것 같다.
'''


def cal_time(start, end):  # 음악 재생 시간 계산
    start_hour, start_min = map(int, (start.split(':')))
    end_hour, end_min = map(int, (end.split(':')))

    return (end_hour - start_hour) * 60 + (end_min - start_min)  # 총 재생 min 반환


def cal_melody(melody, play_time):  # 실제 재생된 멜로디 계산
    again = (play_time // len(melody))  # 멜로디 반복 횟수
    extra = (play_time % len(melody))  # 멜로디 남은 횟수

    return melody * again + melody[:extra]


def change_half(melody):  # #이 들어간 음 replace
    original = ['A#', 'C#', 'D#', 'F#', 'G#']
    rebuild = ['a', 'c', 'd', 'f', 'g']

    for o, r in zip(original, rebuild):
        melody = melody.replace(o, r)

    return melody


def solution(m, musicinfos):
    database = []

    for musicinfo in musicinfos:
        start, end, name, melody = musicinfo.split(',')

        melody = change_half(melody)  # 멜로디 replace

        play_time = cal_time(start, end)

        real_melody = cal_melody(melody, play_time)

        database.append([name, real_melody, play_time])  # database에 내가 들은 노래 정보 저장

    database.sort(key=lambda x: -x[2])  # 조건이 일치하는 음악이 여러 개일 때에는 라디오에서 재생된 시간이 제일 긴 음악 제목을 반환하기 위해 정렬

    m = change_half(m)  # 내가 들은 멜로디도 #음 변환

    for data in database:
        if m in data[1]:  # 멜로디를 찾으면 곡 이름 return
            return data[0]

    return '(None)'
