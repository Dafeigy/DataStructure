import random
random.seed(20221215)

nums = [ i for i in range(10000)]
select = random.sample(nums, 10)
print(select)

arr = [5421, 9169, 7859, 1442, 2261, 1183, 6886, 5079, 4489, 962]

def split(arr:list,pivot, left:int,right:int):
    '''
    Split arr

    Args:
        arr: list that need to be split;
        pivot: split baseline;
        left: left index of (sub) arr;
        right: right index of (sub) arr;
    '''
    if right - left <=1:
        return
    
    pivot, next_pivot_id = arr[left],left
    for i in (left+1, right+1):
        if arr[i] <= pivot:
            next_pivot_id += 1
            arr[next_pivot_id], arr[i] = arr[i], arr[next_pivot_id]
    arr[left], arr[next_pivot_id] = arr[next_pivot_id], arr[left]
    return next_pivot_id


        


