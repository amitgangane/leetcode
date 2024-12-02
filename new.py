if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
    
result = [[i,j,k] for i in range (x+1) for j in range (j+1) for k in range (k+1) if i+j+k != n]

print(result)
