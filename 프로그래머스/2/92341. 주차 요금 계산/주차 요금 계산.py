import math
def solution(fees, records):
    answer = []

    P = dict()
    R = dict()

    for i in records:
        car_time, car_num, car_state = i.split()
        if car_state == "IN":
            P[car_num] = car_time
        else:
            time = P[car_num]
            acctime = (int(car_time[:2]) - int(time[:2])) * 60 + (int(car_time[3:5]) - int(time[3:5]))

            del P[car_num]

            R[car_num] = R.get(car_num, 0) + acctime

    for car_num in P:
        time = P[car_num]
        car_time = "23:59"
        acctime = (int(car_time[:2]) - int(time[:2])) * 60 + (int(car_time[3:5]) - int(time[3:5]))

        R[car_num] = R.get(car_num, 0) + acctime

    for car_num in R:
        acctime = R[car_num]

        result = 0
        if acctime <= fees[0]:
            result = fees[1]
        else:
            result = fees[1] + math.ceil((acctime - fees[0])/fees[2]) * fees[3]
        R[car_num] = result

    T = sorted(R)
    for i in T:
        answer.append(R[i])
    return answer