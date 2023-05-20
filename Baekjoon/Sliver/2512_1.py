# Sliver 3
# 예산 풀이 1


def reqsort(n, m, req):
    req.sort()
    maxReq = m // n
    preReq = 0

    if sum(req) > m:
        while True:
            req_small = list(filter(lambda x: preReq <= x < maxReq, req))
            preReq = maxReq
            if len(req_small) > 0:
                m = m - sum(req_small)
                n -= len(req_small)
                maxReq = m // n
                # print(m,maxReq)
            elif len(req_small) == 0:
                break
        print(maxReq)

    else:
        print(max(req))


n = int(input())
request = list(map(int, input().split()))
m = int(input())
reqsort(n, m, request)