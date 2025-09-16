'''
& & & & 
&     & 
&     &
& & & &    hollow square'''
# n = 4
# for i in range (1,n+1):
#     for j in range (1,n+1):
#         if(i==1 or i==n or j==1 or j==n):
#             print("&",end = " ")
#         else:
#             print(" ",end = " ")
#     print()

'''

*
* *
*   *
*     *
* * * * *
hollow triangle

'''
# n = 5
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         if (i==j or j==1 or i ==n ):
#             print("*", end = " ")
#         else:
#             print(' ',end =" ")
#     print()


'''
# # # # # 
#     #   
#   #
# #
#
hollow reversed triangle '''
# n = 5
# for i  in range (1,n+1):
#     for j in range(1,n+1):
#         if(i == 1 or j ==1 or i+j == n+1):
#             print('#',end = " ")
#         else:
#             print(' ',end = " ")
#     print()

'''      * 
      *   * 
    *       *
  *           *
* * * * * * * * * upper hill pattern'''
n = 5
for i in range (1,n+1):
    for j in range(1,n):
        if(i+j == 6 or i == 5 ):
            print("*",end = " ")
        else:
            print(" ",end=" ")
    for k in range (1,i+1):
        if(i==k or i == 5):
            print("*",end = " ")
        else:
            print(" ",end=" ")
    print()
        
   