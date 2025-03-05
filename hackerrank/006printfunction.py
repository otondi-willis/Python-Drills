"""
Input Format
The first line contains an integer n .

Output Format
Print the list of integers from  through  as a string, without spaces.

Sample input = 3
Sample output = 123

"""
if __name__ == '__main__':
    n = int(input())
    m=[]
    
    while n>0:
        m.append(n) 
        n=n-1
    for i in reversed(m):
        print(i, end="")
        