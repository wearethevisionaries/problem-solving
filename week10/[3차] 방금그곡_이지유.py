'''
12:30 [START]
12:40 [APPROACH] String + Sorting
13:08 [WA] fix get duration logic
13:19 [WA] change get content_length location (has to be after encoding)
13:25 [AC]
'''

def solution(m, musicinfos):
    answer = []
    sharps_dict = {
        'A#': 'a',
        'C#': 'c',
        'D#': 'd',
        'F#': 'f',
        'G#': 'g'
    }

    # ----- Compute -----
    # Encode contents of target.
    for key, value in sharps_dict.items():
        m = m.replace(key, value)

    for musicinfo in musicinfos:
        time1, time2, title, contents = musicinfo.split(',')
        
        # Get duration of source.
        time1_h, time1_m = map(int, (time1.split(':')))
        time2_h, time2_m = map(int, (time2.split(':')))
        duration = (time2_h * 60 + time2_m) - (time1_h * 60 + time1_m)
        
        # Encode contents of source.
        for key, value in sharps_dict.items():
            contents = contents.replace(key, value)
        
        # Get played contents of source.
        content_length = len(contents)
        contents = contents * (duration // content_length) + contents[:(duration % content_length)]

        # Append source information.
        if m in contents:
            answer.append([title, duration])

    # ----- Output -----
    if not answer:
        return '(None)'
    
    answer.sort(key=lambda x: -x[-1])

    return answer[0][0]
