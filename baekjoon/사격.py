target_cnt, bullet_cnt, cutoff_score = map(int, input().split())
target_list = list(map(int, input().split()))
# 걍 제일 높은거 하나 맞추면 되잖아 ???
# 문제가 왜 이따구
# 가 아니였고 실력은 항상 늠
# 완전탐색!
level = 1
score = 0
target_list.sort(reverse=True)
for i in range(1, 100000001):
    level = i
    for _ in range(bullet_cnt):
        for t in target_list:
            if level >= t:
                level += t
                score += t
                break
    if score >= cutoff_score:
        print(i)
        exit()
    score = 0
