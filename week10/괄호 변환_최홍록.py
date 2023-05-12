def solution(p):
    leng=len(p)
    counter=0
    counter_list=[]
    for i in range(leng):
        if p[i]=="(":
            counter+=1
        elif p[i]==")":
            counter-=1
        counter_list.append(counter)
    if all(i >= 0 for i in counter_list):
        return p
    answer = recursive(p, counter_list)
    return answer

def is_good(counter_list):
    if all(i >= 0 for i in counter_list):
        return True
    else: 
        return False

def recursive(w, counter_list):
    if is_good(counter_list) or len(w)==0:
        return w
    leng=len(w)
    u_list=[]
    v_list=[]
    for i in range(leng):
        if counter_list[i]==0:
            u_list = counter_list[:i+1]
            v_list = counter_list[i+1:]
            u = w[:i+1]
            v = w[i+1:]

            if is_good(u_list):
                return(u + recursive(v, v_list))
            else:
                temp = "(" + recursive(v, v_list) +")"
                translate_table = str.maketrans('()', ')(')
                # if len(temp)>2:
                #     # u_split=u.split('')
                #     u_split=list(u)
                #     u_split=u_split[1:-1]
                #     for i in range(len(u_split)):
                #         if u_split[i]=="(":
                #             u_split[i]=")"
                #         elif u_split[i]==")":
                #             u_split[i]="("
                #     u = "".join(u_split)
                # else:
                #     return "()"
                # return temp+u
                return temp + u[1:-1].translate(translate_table)

