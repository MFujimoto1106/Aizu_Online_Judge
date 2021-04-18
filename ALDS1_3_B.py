[n, q] = list(map(int, input().split()))
names = []
times = []
for i in range(n):
    [name_i, time_i] = list(input().split())
    names.append(name_i)
    times.append(int(time_i))


accumulated_time = 0
output_names = []
output_times = []


while len(names) != 0:
    times[0] -= q
    if times[0] <= 0:
        accumulated_time += q + times[0]
        del times[0]
        output_names.append(names.pop(0))
        output_times.append(accumulated_time)
    else:
        accumulated_time += q
        names.append(names.pop(0))
        times.append(times.pop(0))

for j in range(n):
    output_j = [output_names[j], output_times[j]]
    print(' '.join(list(map(str, output_j))))
