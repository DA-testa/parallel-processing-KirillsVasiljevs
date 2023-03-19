# python3
# Kirills Vasiljevs 221RDB427

def parallel_processing(n, m, data):
    output = []
    threads = []
    for i in range(n):
        threads.append(0)
    i = 0
    seconds = 0
    while i < m:
        free_thread_count = threads.count(0)
        if free_thread_count > 0:
            free_thread = threads.index(0)
            threads[free_thread] = data[i]
            output.append([free_thread, seconds])
            i += 1
        else:
            seconds += 1
            for j in range(n):
                threads[j] -= 1

    return output


def main():
    thread_and_job_count = list(map(int, input().split()))
    # n - thread count
    n = thread_and_job_count[0]
    # m - job count
    m = thread_and_job_count[1]

    # second line - data
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))
    assert len(data) == m

    # print out the results, each pair in it's own line
    result = parallel_processing(n, m, data)

    # threads take jobs
    for i, j in result:
        print(i, j)

    


if __name__ == "__main__":
    main()