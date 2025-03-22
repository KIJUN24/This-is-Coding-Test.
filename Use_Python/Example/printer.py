def solution(prioities, location):
    printer = [(i,p) for i, p in enumerate(prioities)]

    trun = 0

    while printer:
        job = printer.pop(0)
        if any(job[1] < other_job[1] for other_job in printer):
            # print(printer)
            printer.append(job)
        else:
            trun += 1
            if job[0] == location:
                break
        
    print(trun)
    # print(job)

solution([2,1,3,2], 0)