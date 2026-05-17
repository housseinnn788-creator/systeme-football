# =========================
# ROUND ROBIN
# =========================

def round_robin(processes, burst_time, quantum):

    n = len(processes)

    remaining = burst_time[:]

    waiting_time = [0] * n

    time = 0

    print("\n===== ROUND ROBIN =====")

    while True:

        done = True

        for i in range(n):

            if remaining[i] > 0:

                done = False

                if remaining[i] > quantum:

                    print(f"{processes[i]} : {time} -> {time + quantum}")

                    time += quantum

                    remaining[i] -= quantum

                else:

                    print(f"{processes[i]} : {time} -> {time + remaining[i]}")

                    time += remaining[i]

                    waiting_time[i] = time - burst_time[i]

                    remaining[i] = 0

        if done:
            break

    average = sum(waiting_time) / n

    print("\nWaiting Time:")
    for i in range(n):
        print(processes[i], "=", waiting_time[i])

    print("Average Waiting Time =", average)


# =========================
# SRTF
# =========================

def srtf(processes, burst_time):

    n = len(processes)

    remaining = burst_time[:]

    complete = 0

    time = 0

    minm = 999999

    shortest = 0

    finish_time = 0

    waiting_time = [0] * n

    print("\n===== SRTF =====")

    while complete != n:

        minm = 999999

        for j in range(n):

            if remaining[j] > 0 and remaining[j] < minm:

                minm = remaining[j]

                shortest = j

        print(f"{processes[shortest]} : {time} -> {time+1}")

        remaining[shortest] -= 1

        minm = remaining[shortest]

        if minm == 0:
            minm = 999999

        if remaining[shortest] == 0:

            complete += 1

            finish_time = time + 1

            waiting_time[shortest] = finish_time - burst_time[shortest]

            if waiting_time[shortest] < 0:
                waiting_time[shortest] = 0

        time += 1

    average = sum(waiting_time) / n

    print("\nWaiting Time:")

    for i in range(n):
        print(processes[i], "=", waiting_time[i])

    print("Average Waiting Time =", average)


# =========================
# MAIN
# =========================

processes = ["P1", "P2", "P3"]

burst_time = [10, 5, 8]

quantum = 2

round_robin(processes, burst_time, quantum)

srtf(processes, burst_time)