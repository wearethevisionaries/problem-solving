# 05.12 16:00 날라감...

# melody # 바꿔준다.
def change_melody(music):
    replace_dict = {'A#':'a',
                   'C#':'c',
                   'D#':'d',
                   'F#':'f',
                   'G#':'g'}
    for ori, new in replace_dict.items():
        music = music.replace(ori, new)
    return music

# 걸린 시간을 '분'으로 측정 해준다.
def calculate_minute_spent(start, end):
    start_time = int(start.split(':')[0]) * 60 + int(start.split(':')[1])
    end_time = int(end.split(':')[0]) * 60 + int(end.split(':')[1])
    return  end_time - start_time
    

def solution(m, musicinfos):
    answer = ''
    heard_melody = change_melody(m)
    play_list = []
    for i, info in enumerate(musicinfos):
        start, end, name, melody = info.split(',')
        
        # 걸린 시간 계산한다.
        play_time = calculate_minute_spent(start, end)
        
        # #음을 바꿔준 멜로디 시간 계산한다.
        changed_melody = change_melody(melody)
        melody_time = len(changed_melody)
        
        # melody 시간이 음악 재생 시간 보다 짧을 경우 반복된 부분 중 추가된 길이만큼 더해준다.
        remain_time = play_time % melody_time
        if melody_time > play_time:
            real_melody = changed_melody[:remain_time]
        else:
            real_melody = changed_melody*(play_time//melody_time) + changed_melody[:remain_time]
            
        # 들은 멜로디(heard_melody) 가 실제 재생된 멜로디(real_melody) 에 포함될 경우만 저장한다.
        if heard_melody in real_melody:
            play_list.append([play_time, name, real_melody, i])
    
    # 들은 음악 중에 재생 시간이 가장 긴 것 역순으로 나열하여 제일 긴 음악 반환한다.
    # 먼저 입력된 순서대로 그다음 정렬을 해준다.
    if len(play_list) == 0:
        return '(None)'
    else:
        sorted_play_list = sorted(play_list, key=lambda x:(-x[0], x[3]))
        return sorted_play_list[0][1]