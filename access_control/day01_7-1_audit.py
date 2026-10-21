from rbac import check_permission, ROLES, USERS                  # 판정 함수와 역할 · 사용자 정보를 불러온다
from access_log import LOG                                       # access_log.py 의 기록 목록을 불러온다

allowed = 0                                                      # 허용 건수
denied = 0                                                       # 거부 건수
counts = {}                                                      # "사용자 허용" · "사용자 거부" → 건수
used = {}                                                        # 역할 → 실제로 쓴 권한 목록

# ← 1부: 기록을 하나씩 다시 판정하며 건수와 쓴 권한 모으기
for num, time, user, resource, action in LOG:                    # 1. 기록 한 줄에서 다섯 값을 꺼낸다
    ok, reason = check_permission(user, resource, action)        # 2. 판정해 결과와 이유를 나눠 받는다
    if ok:                                                       # 3. 허용이면
        allowed = allowed + 1                                    #    허용 건수를 1 늘린다
        key = user + " 허용"                                      #    "사용자 허용" 글자를 만든다
        counts[key] = counts.get(key, 0) + 1                     #    그 건수를 1 늘린다
        role = USERS[user]["role"]                               #    그 사용자의 역할을 꺼낸다
        if role not in used:                                     # 4. used 에 이 역할이 아직 없으면
            used[role] = []                                      #    빈 목록을 먼저 만든다
        used[role].append(resource + ":" + action)               #    "자원:행위" 글자를 목록에 더한다
    else:                                                        # 5. 거부이면
        denied = denied + 1                                      #    거부 건수를 1 늘린다
        print("[거부]", num, time, user, resource, action, reason)   #    번호 · 시각 · 사용자 · 자원 · 행위 · 이유를 출력한다
        key = user + " 거부"                                      #    "사용자 거부" 글자를 만든다
        counts[key] = counts.get(key, 0) + 1                     #    그 건수를 1 늘린다

print("허용", allowed, "거부", denied)                           # 전체 건수를 출력한다
print(counts)                                                    # 사용자별 건수를 출력한다

# ← 2부: 쓰이지 않은 권한 출력하기
for role, perms in ROLES.items():                                # 6. 역할과 권한 목록을 하나씩 꺼낸다
    for perm in perms:                                           # 7. 그 목록의 권한을 하나씩 꺼낸다
        if perm not in used.get(role, []):                       #    그 역할이 쓴 권한 목록에 없으면
            print("쓰이지 않음", role, perm)                      #    쓰이지 않은 권한으로 출력한다