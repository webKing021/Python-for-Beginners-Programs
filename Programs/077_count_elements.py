# WAP to Count for how many times the elements are repeated in dict.
d = {1:1, 2:2, 3:2, 4:3}
cnt = {}
for i in d.values():
    if i in cnt:
        cnt[i] = cnt[i] + 1
    else:
        cnt[i] = 1
print(cnt)


