LEFT = True
RIGHT = False
  

def searchArr(a, n, mobile): 
    for i in range(n): 
        if a[i] == mobile: 
            return i + 1
    
def get_mobile(arr, dir, n):
    pre_mobile = 0
    curr_mobile = 0
    for i in range(n):
        if dir[arr[i] - 1] == RIGHT and i != 0:
            if arr[i] > arr[i - 1] and arr[i] > pre_mobile:
                curr_mobile = arr[i]
                pre_mobile = curr_mobile
        
        if dir[arr[i] - 1] == LEFT and i != n - 1:
            if arr[i] > arr[i + 1] and arr[i] > pre_mobile:
                curr_mobile = arr[i]
                pre_mobile = curr_mobile
    
    if curr_mobile == 0 and pre_mobile == 0:
        return 0
    else:
        return curr_mobile

def determine_sjt(n):
    permutations = [0] * n
    for i in range(n):
        permutations[i] = i + 1
  
    directions = [RIGHT] * n
  
    factorial = 1
    for i in range(1, n + 1): 
        factorial = factorial * i 

    all_permutations = []
    all_permutations.append(permutations[:]) 

    # generating permutations 
    for i in range(1, factorial): 
        mobile = get_mobile(permutations, directions, n) 
        position = searchArr(permutations, n, mobile) 
    
        # swapping the elements according to direction
        if directions[permutations[position - 1] - 1] == RIGHT: 
            permutations[position - 1], permutations[position - 2] = permutations[position - 2], permutations[position - 1] 
    
        elif directions[permutations[position - 1] - 1] == LEFT: 
            permutations[position], permutations[position - 1] = permutations[position - 1], permutations[position] 
    
        # changing directions
        for i in range(n): 
            if permutations[i] > mobile: 
                if directions[permutations[i] - 1] == LEFT: 
                    directions[permutations[i] - 1] = RIGHT 
                elif directions[permutations[i] - 1] == RIGHT: 
                    directions[permutations[i] - 1] = LEFT 

        all_permutations.append(permutations[:])

    if not all_permutations:
        return -1
    else:
        return all_permutations

