# 5분: 문제 다 읽음
# 11분: ,을 기준으로 split
#      노래가 얼마나 재생됐는지 계산
#      재생시간 차이로 노래를 추가하려고 했는데 그럼 이중 반복문 써야될거같아서 취소
# 23분: 노래 두번 반복해서 find해보려고 했는데 안됨
#       # 처리를 어떻게 해야할지 고민
#       반복 안되면 그냥 find하면 되는데 반복되는곳 처리를 어떻게 해야할지 고민
# 39분: 시간에 맞게 노래를 늘리고 줄여봤는데 # 처리를 아직 못함
#       끝자리만 #이 아닌지만 확인하면 되는거 아닐까 -> 아니다
#       find(m)이랑 find(m + #)이랑 두개 다 검색해볼까 둘 다 잡히면 아닌걸로
# 46분: 일단 테스트 케이스는 맞게 띄우는거 같다 이 값을 저장해서 return하면 맞게 나올듯
# 51분: 테스트 케이스는 다 맞았다, 제출결과는 50% 맞았다
#       sorted하는 부분에서 뭔가 잘못된듯?
# 52분: sorted 하는 부분을 수정해서 60%가 됐다 이제 아이디어 한계인듯
# 60분: GG

# 다른 사람의 해설을 보고 추가한 부분
# 왜 이생각을 못했을까
def change_melody(music):
    replace_dict = {"C#": "c",
                    "D#": "d",
                    "F#": "f",
                    "G#": "g",
                    "A#": "a"}
    
    for origin, new in replace_dict.items():
        music = music.replace(origin, new)
    
    return music

def solution(m, musicinfos):
    ans = []
    diffs = []
    
    for i in range(len(musicinfos)):
        sep = musicinfos[i].split(',')
        diff_hour = int(sep[1][:2]) - int(sep[0][:2])
        diff_minute = int(sep[1][3:]) - int(sep[0][3:])
        diff = diff_hour * 60 + diff_minute
        diffs.append(diff)
    
    for i, diff in enumerate(diffs):
        sep = musicinfos[i].split(',')
        music = change_melody(sep[-1])
        
        cut = diffs[i] // len(music)
        add = diffs[i] % len(music)
        music = music * cut + music[:add]
        
        m = change_melody(m)
        
        if m in music:
            ans.append((diffs[i], i, sep[2]))
            
    ans = sorted(ans, key=lambda x: (-x[0], x[1]))
    if ans: return ans[0][-1]
    else: return "(None)"
