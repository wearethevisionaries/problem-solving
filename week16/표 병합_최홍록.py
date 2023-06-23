def solution(commands):
    answer = []
    darray = [[""]*5 for i in range(2)]
    check = []
    isthere = []
    # print(darray)
    for command in commands:
        splited = command.split(" ")
        if splited[0] == "PRINT":
            # print(splited)
            r = int(splited[1])
            c = int(splited[2])
            if darray[r][c] == "":
                answer.append("EMPTY")
            else:
                answer.append(darray[r][c])
            # for row in darray:
            #    print(row)
        elif splited[0] == "UPDATE" and len(splited) == 4:
            # print(splited)
            r = int(splited[1])
            c = int(splited[2])
            darray[r][c] = splited[3]
            # print(check)
            if (r,c) in isthere:
                for element in check:
                    if (r,c) in element:
                        for (r1,c1) in element:
                            # print(r1,c1)
                            darray[r1][c1] = splited[3]
            # for row in darray:
            #    print(row)
        elif splited[0] == "UPDATE" and len(splited) == 3:
            # print(splited)
            for i, row in enumerate(darray):
                for j, column in enumerate(row):
                    if column == splited[1]:
                        darray[i][j] = splited[2]
            # for row in darray:
            #    print(row)
        elif splited[0] == "MERGE":
            # print(splited)
            if (int(splited[1]), int(splited[2])) not in isthere and (int(splited[3]), int(splited[4])) not in isthere:
                isthere.append((int(splited[1]), int(splited[2])))
                isthere.append((int(splited[3]), int(splited[4])))
                check.append([(int(splited[1]), int(splited[2])),(int(splited[3]), int(splited[4]))])
                darray[int(splited[3])][int(splited[4])] = darray[int(splited[1])][int(splited[2])]
                # print(1)
            elif (int(splited[1]), int(splited[2])) in isthere and (int(splited[3]), int(splited[4])) not in isthere:
                isthere.append((int(splited[3]), int(splited[4])))
                for i, item in enumerate(check):
                    if (int(splited[1]), int(splited[2])) in item:
                        check[i].append((int(splited[3]), int(splited[4])))
                darray[int(splited[3])][int(splited[4])] = darray[int(splited[1])][int(splited[2])]
                # print(2)
            elif (int(splited[3]), int(splited[4])) in isthere and (int(splited[1]), int(splited[2])) not in isthere:
                isthere.append((int(splited[1]), int(splited[2])))
                for i, item in enumerate(check):
                    if (int(splited[3]), int(splited[4])) in item:
                        check[i].append((int(splited[1]), int(splited[2])))
                darray[int(splited[1])][int(splited[2])] = darray[int(splited[3])][int(splited[4])]
                # print(3)
            elif (int(splited[1]), int(splited[2])) in isthere and (int(splited[3]), int(splited[4])) in isthere:
                for item in check:
                    if (int(splited[3]), int(splited[4])) in item:
                        temp = item
                        check.remove(item)
                        for (r,c) in item:
                            darray[r][c] = darray[int(splited[1])][int(splited[2])]
                temp1=[]
                for i, item2 in enumerate(check):
                    if (int(splited[1]), int(splited[2])) in item2:
                        temp1=item2
                        check[i] = item2+temp
                if len(check)==0 or len(temp1)==0:
                    check.append(temp) 
                # print(4)
            # print(check)
            # for row in darray:
            #    print(row)
        elif splited[0] == "UNMERGE":
            # print(splited)
            for item in check:
                if (int(splited[1]), int(splited[2])) in item:
                    item.remove((int(splited[1]), int(splited[2])))
                    for element in item:
                        isthere.remove(element)
                        # print(element)
                        darray[element[0]][element[1]] = ""
                    check.remove(item)
        #     for row in darray:
        #        print(row)
        # print("___________________________")
    # for row in darray:
    #     print(row)
    return answer

print(solution(["UPDATE 1 1 menu", "MERGE 1 1 1 2", "MERGE 1 1 1 3", "MERGE 1 1 1 4", "MERGE 1 2 1 3", "UPDATE 1 1 hansik", "PRINT 1 1", "PRINT 1 2", "PRINT 1 3", "PRINT 1 4"]))