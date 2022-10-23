floors, height, diameter, n, sum, pipes = int(input()), int(input()), int(input()), int(input()), 0, []
for i in range(n):
    if int(input()) == diameter: pipes.append(int(input()))
if len(pipes) == 1: print(pipes[0])
else:
    while len(pipes) > 1:
        pipes = sorted(pipes)
        s = pipes.pop(0)+pipes.pop(0)
        sum += s
        pipes.append(s)
print(sum)
