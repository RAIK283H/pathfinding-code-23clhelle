LEFT = True
RIGHT = False

def searchArr(a, n, mobile): 
    for i in range(n): 
        if a[i] == mobile: 
            return i
    
def get_mobile(arr, dir, n):
    pre_mobile = -1
    curr_mobile = -1
    for i in range(n):
        if dir[arr[i]] == RIGHT and i != 0:
            if arr[i] > arr[i - 1] and arr[i] > pre_mobile:
                curr_mobile = arr[i]
                pre_mobile = curr_mobile
        elif dir[arr[i]] == LEFT and i != n - 1:
            if arr[i] > arr[i + 1] and arr[i] > pre_mobile:
                curr_mobile = arr[i]
                pre_mobile = curr_mobile
    
    return curr_mobile if curr_mobile != -1 else 0

def determine_sjt(n):
    permutations = list(range(n))
    directions = [RIGHT] * n
  
    factorial = 1
    for i in range(1, n + 1): 
        factorial *= i 

    all_permutations = [permutations[:]]

    for _ in range(1, factorial): 
        mobile = get_mobile(permutations, directions, n) 
        if mobile == 0:
            break
        
        position = searchArr(permutations, n, mobile)
    
        # Swap based on direction
        if directions[permutations[position]] == RIGHT:
            permutations[position], permutations[position - 1] = permutations[position - 1], permutations[position]
        elif directions[permutations[position]] == LEFT:
            permutations[position], permutations[position + 1] = permutations[position + 1], permutations[position]
    
        # Change directions for elements greater than the mobile element
        for i in range(n):
            if permutations[i] > mobile:
                directions[permutations[i]] = not directions[permutations[i]]

        all_permutations.append(permutations[:])

    return all_permutations
