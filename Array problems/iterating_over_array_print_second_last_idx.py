n = int(input())
arr = map(int, input().split())
arr = list(set(arr))
print(sorted(arr)[-2])