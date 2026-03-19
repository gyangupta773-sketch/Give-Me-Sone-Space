def sum_n(n):
    return n * (n + 1) // 2 # integer result

print("Sum of the first n numbers (n=5):", sum_n(5))

def array_sum(a):
    total = 0
    for i in a :
        total += i
        return total
    
    #Examples   
    a = [12, 3, 4, 15]
    print("Array Sum:", array_sum(a))

def sum(n):
    if n <= 0:
        return n 
    return n + sum(n - 1 )

    print("Recursive sum (n=5):", sum(5))