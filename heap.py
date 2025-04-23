heap = ['최소힙:']


def heap_push(item):
    heap.append(item)  # 1. 일단 맨 끝에 넣는다

    child = len(heap) - 1  # 자기자신은 방금 붙인 걔
    parent = child // 2  # 부모는 반토막 index
    print("부모",len, child//2)

    # 루트 노드가 아닌 한 + 최소힙이지만 부모가 크다면 바꿔야하니까?
    while parent and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]  # 스왑
        child = parent  # 이제 아이가 부모가 되고
        parent = child // 2  # 부모는 아이 index의 반토막


def heap_pop():
    if len(heap) == 1:
        print('힙이 비어있어 삭제가 불가능합니다!')
        return

    result = heap[1]
    heap[1] = heap[-1]
    heap.pop()

    parent = 1
    child = parent * 2  # 일단 좌측 child 기준으로 잡고

    if child + 1 <= len(heap) - 1:  # 우측이 트리상에서 존재하는 경우 +
        if heap[child] > heap[child + 1]:  # 좌측이 우측보다 더 큰 경우
            child += 1  # 우측 자식 기준으로 자식의 자격을 바꿈
            # 왜냐면 자리 바꿀때 더 작은 값이 최소힙의 경우 우선순위가 높아서

    while child <= len(heap) - 1 and heap[parent] > heap[child]:
        heap[parent], heap[child] = heap[child], heap[parent]
        parent = child
        child = parent * 2
        if child + 1 <= len(heap) - 1:
            if heap[child] > heap[child + 1]:
                child += 1

    return result


heap_push(33)
print(heap)
heap_push(12)
print(heap)
heap_push(7)
print(heap)
heap_push(19)
heap_push(21)
print(heap)
heap_push(5)
print(heap)
heap_push(8)
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(heap_pop())
print(heap)
print(2//2)