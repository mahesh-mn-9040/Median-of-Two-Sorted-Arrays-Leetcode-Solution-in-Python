
        nums1=list(map(int,input().split()))
        nums2=list(map(int,input().split()))
        mer=nums1+nums2
        mer.sort()
        x=len(mer)
        if x==1:
            return mer[0]
        elif x%2==0: #if the merged list's length is even 
            return ((mer[x//2]+mer[x//2 -1])/2)  
        else:#if the merged length is odd
            return mer[x//2 ]
