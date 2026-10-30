def exception_id(source):
    """"예외 3번" 모양 문자열에서 예외 번호(3)를 꺼내 숫자로 리턴한다."""
    number_text = source.replace("예외 ", "")
    number_text = number_text.replace("번", "")                  # "번" 을 지운 문자열을 number_text 에 다시 담는다
    return int(number_text)                                      # number_text 를 숫자로 바꿔 리턴한다


def count_users_by_role(users):
    """역할마다 사용자가 몇 명인지 센 딕셔너리를 리턴한다(재직 여부와 상관없이 센다). 예: {"finance": 1, "sales": 2}"""
    counts = {}
    for info in users.values():
        role = info["role"]
        old_count = counts.get(role, 0)                          # 지금까지 센 수를 꺼낸다 (처음이면 0)
        counts[role] = old_count + 1                             # 1을 더해 다시 담는다
    return counts


def make_plan(finding, method, target, impact):
    """회수 대상을 복사해 method · target · impact 키를 추가한 계획 한 건을 리턴한다. impact 는 이 회수로 사라지는 (사용자, 권한)의 수다."""
    plan = finding.copy()
    plan["method"] = method
    plan["target"] = target
    plan["impact"] = impact
    return plan


def build_plan(finding, method, users, roles, role_counts):
    """회수 방법에 맞게 지울 대상(target)과 영향(impact)을 정해 계획 한 건을 리턴한다."""
    info = users[finding["user"]]
    if method == "예외 삭제":
        target = exception_id(finding["source"])
        return make_plan(finding, method, target, 1)
    if method == "역할 해제":
        role_permissions = roles[info["role"]]                   # 그 사용자의 역할에 든 권한 리스트
        impact = len(role_permissions)                           # 영향은 그 역할에 든 권한 수
        return make_plan(finding, method, finding["user"], impact)
    impact = role_counts[info["role"]]                           # 역할에서 권한 빼기: 영향은 그 역할을 가진 사용자 수
    return make_plan(finding, method, info["role"], impact)


def plan_revocation(findings, users, roles):
    """회수 대상마다 회수 방법을 정해 계획 리스트를 리턴한다. 실제로는 아무것도 지우지 않는다."""
    role_counts = count_users_by_role(users)
    plans = []
    for finding in findings:
        info = users[finding["user"]]
        if "예외" in finding["source"]:                          # source 안에 "예외" 가 있으면
            method = "예외 삭제"                                 # 방법은 예외 삭제
        elif not info["employed"]:                               # 그렇지 않고 재직 중이 아니면
            method = "역할 해제"                                 # 방법은 역할 해제
        else:                                                    # 그렇지 않으면
            method = "역할에서 권한 빼기"                        # 방법은 역할에서 권한 빼기
        plan = build_plan(finding, method, users, roles, role_counts)
        plans.append(plan)
    return plans