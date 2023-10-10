import queue

# 우선순위 큐에 데이터 넣기: 튜플형식 = (우선순위, 넣을 데이터)
wait_queue = queue.PriorityQueue() # 채점을 기다리는 큐 : 우선순위 큐
judge_queue = queue.Queue() # 채점 
judging_q = set()
history = [] # 채점 기록
url_check = set()

Q = int(input()) # 명령의 개수 

for _ in range(Q):
    line = input()
    code = int(line.split()[0]) # 어떤 액션을 취할지를 나타내는 정보 저장
    # 첫번째 명령은 항상 코드트리 채점기 준비: 100 N u0 (준비, 채점기 개수, 초기 url)

    if code == 100:
        N = int(line.split()[1]) # 채점기 개수
        judger = [n+1 for n in range(N)]
        s_url = line.split()[-1]
        wait_queue.put((1, 0, s_url)) #우선순위, 시간, url
        url_check.add(s_url)

    elif code == 200: # 200 t p u 형태: t초에 채점 우선순위가 p이며 url이 u인 문제에 대해 채점 요청 들어온 것을 의미 
        _, t, p, u = line.split()
        if u  not in url_check:
            wait_queue.put((int(p),int(t), u)) # 우선순위, 시간, url 
            url_check.add(u)

    elif code == 300: # 300 t 형태 : t초에 채점 대기 큐에서 즉시 채점 가능 경우 우선순위 가장 높은 채점 task 골라 진행
        if not wait_queue.empty(): 

            p, q_time, url = wait_queue.get()
            domain = url.split('/')[0]

            t = int(line.split()[-1])

            flag = False

            if q_time == 0:
                flag=True
            
            if domain not in judging_q:
                for h in history: 
                    if domain in h[2]:
                        start, end = h[0], h[1]
                        available= start + 3*(end-start)
                        if t > available: 
                            flag=True
                            pass
                        else: 
                            wait_queue.put((p, q_time, url))
                if flag:
                    check = False
                    for i in range(len(judger)):
                        if judger[i] != -1 and check==False:
                            check=True
                            judge_queue.put((t, url, judger[i]))
                            judging_q.add(url.split('/')[0])
                            judger[i] = -1 #사용 중인 채점기 -1로 표시
                            if url in url_check:
                                url_check.remove(url)
                        elif check: 
                            pass
            else:
                wait_queue.put((p,q_time, url))


    elif code == 400: # t초에 Jid번 채점기가 진행하던 채점이 종료되고 쉬는 상태로 / 만약 Jid가 채점 하는 것이 없으면 명령 무시
        end_time = int(line.split()[1])
        j = int(line.split()[-1])
        
        if judger[j-1] != -1: #채점 중인게 없으면 
            pass
        else:
            start_time, end_url, jid = judge_queue.get()
            history.append((start_time, end_time, end_url, jid))
            if end_url.split()[0] in judging_q:
                judging_q.remove(end_url.split()[0])

            #print(history)
            judger[j-1] = j #다시 사용 가능하도록 만들기

    elif code == 500: # 시간 t에 채점 대기 큐에 있는 채점 task의 수 출력
        print(wait_queue.qsize())

# 8
# 100 3 bleidx/815674522
# 200 53065 3 hrslhvcfxyvfswxvhy/512312385
# 200 187125 2 bleidx/193792752
# 300 370883
# 400 413702 2
# 300 505542
# 300 671907
# 500 688062