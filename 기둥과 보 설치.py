def solution(n, build_frame):
    def pillar_install_possible(map_, pillar_x_y):
        x, y = pillar_x_y
        
        if y == n: #바닥이면
            return True

        if map_[y+1][x][0]:# 밑에 기둥 있으면
            return True 
        if map_[y][x][1]: #보가 있으면
            return True
        if map_[y][x-1][1]: #하나 옆에 보가 있으면
            return True

        return False


    def bo_install_possible(map_, bo_x_y):
        x, y = bo_x_y
        
        if y == n or x == n: #맨 오른쪽이나 바닥에는 보 설치 불가
            return False

        if map_[y+1][x][0] or map_[y+1][x+1][0]: #왼쪽이나 오른쪽에 기둥이 있다면 설치가능
            return True

        if x>0 and x<n and map_[y][x-1][1] and map_[y][x+1][1]: #같은 높이에 양쪽으로 보가 있다면 설치가능
            return True

        return False


    def pillar_destroy_possible(map_, pillar_x_y):
        x, y = pillar_x_y
        
        # 위에 쌓인 기둥 있으면 아웃  
        if map_[y-1][x][0]:
            return False

        # 보가 있다면 서로 이어져 있지 않으면 아웃
        if map_[y-1][x][1]:

            if x == 0:  # 인덱스 오류 예외
                return False
            if not map_[y-1][x-1][1]:
                return False

        return True


    def bo_destroy_possible(map_, bo_x_y):
        x, y = bo_x_y

        #다음 중 하나라도 해당되는 부분이 있다면 out

        # 보가 떠받치던 기둥이 있었다면,
        if map_[y][x][0]:
            # 옆의 다른 보가 기둥을 지탱해주지 않으면 아웃
            if (not map_[y][x-1][1]):
                return False

        # 오른쪽에 보가 떠받치던 기둥이 있었다면,
        if map_[y][x+1][0]:
            #
            if (x+1 > n) or (not map_[y][x+1][1]):
                return False

        # 이어진 보(con)가 있다면, con이 다른 기둥위에 있지 않으면 아웃
        if (x+1)<n and map_[y][x+1][1]:
            if not map_[y+1][x+1][0]:
                return False

        # 이어진 보(con)가 왼쪽에 있다면, con이 다른 기둥위에 있지 않으면 아웃
        if x>0 and map_[y][x-1][1]:
            if not map_[y+1][x-1][0]:
                return False

        return True

    map_ = [[[False, False] for _ in range(n+1)] for _ in range(n+1)]

    for req in build_frame:
        x, y , bo_pillar, install = req
        y = n - y
        if bo_pillar == 0 :  # 기둥일 경우
            if install:
                if pillar_install_possible(map_, [x, y]):
                    map_[y][x][0] = True
            else:  # destroy
                if pillar_destroy_possible(map_, [x, y]):
                    map_[y][x][0] = False

        else:  # 보일 경우
            if install:
                if bo_install_possible(map_, [x, y]):
                    map_[y][x][1] = True
            else:
                if bo_destroy_possible(map_, [x, y]):
                    map_[y][x][1] = False

    answer = []
    for y in range(n+1):
        for x in range(n+1):
            p, bo = map_[y][x]
            if p:
                answer.append([x, n-y, 0])
            if bo:
                answer.append([x, n-y, 1])
    return sorted(answer)


if __name__ == "__main__":
    # map_ = (solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
    #       2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
    # for r in map_:
    #     print(r)
    print(solution(5, [[1, 0, 0, 1], [1, 1, 1, 1], [2, 1, 0, 1], [
          2, 2, 1, 1], [5, 0, 0, 1], [5, 1, 0, 1], [4, 2, 1, 1], [3, 2, 1, 1]]))
    print(solution(5,[[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))