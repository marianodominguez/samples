def subArraySum(arr, n, s):
    for i in range(n):
        j=i+1
        while i<j:
            psum=sum(arr[i:j])
            if psum<s:
                j+=1
            if psum==s:
                return [i+1,j]
            if psum>s:
                j=i
array=[1,2,3,4,5,6,7,8,9,10]
n=len(array)-1
print(subArraySum(array,n,15))
