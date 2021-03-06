# bruteforce & recursion
import copy


def solution(n, weak, dist):
    answer = 15
    dist.sort(reverse=True)

    tmp = copy.copy(weak)
    for w in weak:
        tmp.append(w + n)
    # dist 큰 친구부터 투입. d 로 남은 remain 최대한 커버칠 수 있는 만큼 커버치고, 남은 remain return => 부분해가 최적해가 아닌듯하다. 폐기.
    def backtrack(remain, st, cnt):
        # return 조건 : remain 이 없을 때
        nonlocal answer
        if not remain:
            if cnt < answer:
                answer = cnt
                return

        elif cnt == len(dist):
            return

        else:
            d = dist[cnt]
            cnt += 1

            left_forbidden = [st - x if st - x >= 0 else st - x + n for x in range(d+1)]
            right_forbidden = [st + x if st + x < n else st + x - n for x in range(d+1)]

            left = [x for x in remain if x not in left_forbidden]
            right = [x for x in remain if x not in right_forbidden]

            st ~ st + d

            if not left:
                backtrack(left, None, cnt)
            for st in left:
                backtrack(left, st, cnt)

            if not right:
                backtrack(right, None, cnt)
            for st in right:
                backtrack(right, st, cnt)  # backtrack 안에 이렇게 backtrack 이 많으면 2^8 이 아니라 len(dist)^8 이 되어버린다.

    for i, st in enumerate(weak):
        backtrack(weak, st, 0)  # 탐색할 공간,


    if answer == 15:
        return -1
    else:
        return answer


if __name__ == "__main__":
    print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
    print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))
