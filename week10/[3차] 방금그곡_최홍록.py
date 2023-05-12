def solution(m, musicinfos):
    music_list=[]
    m = m.replace("A#","a").replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g")
    for item in musicinfos:
        splited = item.split(",")
        start_time = splited[0].split(":")
        end_time = splited[1].split(":")
        title = splited[2]
        splited[3] = splited[3].replace("A#","a").replace("C#", "c").replace("D#", "d").replace("F#", "f").replace("G#", "g")
        total_played_time = 60*(int(end_time[0])-int(start_time[0])) + (int(end_time[1])-int(start_time[1]))
        music_leng = len(splited[3])
        total_song_played = ""
        for i in range(total_played_time//music_leng):
            total_song_played = total_song_played + splited[3]
        total_song_played = total_song_played + splited[3][:total_played_time%music_leng]
        music_list.append((total_song_played, title, total_played_time, start_time))   
    answer_list = []
    for music in music_list:
        if m in music[0]:
            # return music[1]
            answer_list.append(music) 
    if len(answer_list)==1:
        return answer_list[0][1]
    else:
        case_many = []
        maximum = 0
        for i in range(len(answer_list)):
            if maximum < answer_list[i][2]:
                maximum = answer_list[i][2]
        for i in range(len(answer_list)):
            if maximum == answer_list[i][2]:
                case_many.append((answer_list[i][1], answer_list[i][3]))
        if len(case_many) == 1:
            return case_many[0][0]
        elif len(case_many) > 1:
            early_hour = 24
            early_minute = 60
            for i in range(len(case_many)):
                if int(case_many[i][1][0]) <= int(early_hour):
                    early_hour = case_many[i][1][0]
                    if int(case_many[i][1][1]) < int(early_minute):
                        early_minute = case_many[i][1][1]
            for i in range(len(case_many)):
                if case_many[i][1][0] == early_hour and case_many[i][1][1] == early_minute:
                    return case_many[i][0]
    return ("(None)")
