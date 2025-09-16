'''#left hand increasing tringale code 
* 
* * 
* * *
* * * *'''
# n = 4
# for i in range (0,n):
#     for j in range (0,i+1):
#         print('*',end=" ")
#     print()






'''
left hand ulta ok triangle code
* * * * 
* * * 
* *
*
'''
# n = 4
# for i in range(1,n+1):
#     for j in range(i,n+1):
#        print('*',end =" ")
#     print()









'''#right hand ulta triangle 
# - - - - *
# - - - * *
# - - * * *
# - * * * *'''
# n = 4 
# for i in range(1,n+1):
    # for j in range(i,n+1):
    #     print('-',end = " ")
#     for k in range(0,i):
#         print("*",end = ' ')
#     print()
  







'''decreasing  trianglr right hand side
* * * * 
- * * * 
- - * *
- - - *

'''
# n = 4 
# for i in range(1,n+1):

#     for  j in range(0,i-1):
#         print('-',end = " ")
#     for k in range(i,n+1):
#         print('*',end = " ")
#     print()
        
   




'''hill pattern
      * 
    * * * 
  * * * * * 
* * * * * * * 
'''
# n = 4
# for i in range(1,n+1):
#     for j in range (i,n):
#         print(" ",end = " ")
#     for k in range (0,i):
#         print("*",end = " ")
    
#     for r in range(0,i-1):
#         print("*",end = ' ')
#     print()
    





'''decreasing hill pattern
 * * * * * * * 
  * * * * * 
    * * * 
      *  '''
n = 4 
for i in range (1,n+1):
    for j in range (0,i-1):
        print(" ",end  = " ")
    for k in range(i,n+1):
        print("*",end= " ")
    for r in range (i,n):
        print("*",end = " ")
    print()







'''diamond pattern
      * 
    * * * 
  * * * * * 
* * * * * * * 
* * * * * * * 
  * * * * * 
    * * * 
      * 
'''
# n = 4
# for i in range(1,n+1):
#     for j in range (i,n):
#         print(" ",end = " ")
#     for k in range (0,i):
#         print("*",end = " ")
    
#     for r in range(0,i-1):
#         print("*",end = ' ')
#     print()   
# for i in range (1,n+1):
#     for j in range (0,i-1):
#         print(" ",end  = " ")
#     for k in range(i,n+1):
#         print("*",end= " ")
#     for r in range (i,n):
#         print("*",end = " ")
#     print()