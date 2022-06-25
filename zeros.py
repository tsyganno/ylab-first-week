def zeros(n):
    count = 0
    while n >= 5:
        n //= 5
        count += n
    return count


print(zeros(12))
print(zeros(0))
print(zeros(6))
print(zeros(30))
