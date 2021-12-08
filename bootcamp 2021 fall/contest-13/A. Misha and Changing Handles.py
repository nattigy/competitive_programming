def mishaAndChangingHandles(requests):
    req_maps = {}
    for request in requests:
        changed = False
        for key in req_maps:
            if req_maps[key] == request[0]:
                req_maps[key] = request[1]
                changed = True
                break
        if not changed:
            req_maps[request[0]] = request[1]
    
    print(len(req_maps))
    for key in req_maps:
        print(key, req_maps[key])

num_req = int(input())
requests = []
for _ in range(num_req):
    requests.append(list(input().split()))

mishaAndChangingHandles(requests)
