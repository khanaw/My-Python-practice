
# coding: utf-8

# # Fibonacci Sequence Generator
# 
# ### Enter a number and generate its Fibonacci Number  to that number
#  The limit is set to 250. You can increase the limit but may get errors. Use recursion to obtain better results at higher numbers. If you wanted to find 1500, it would be better to run the number in increments of 250 to 1500
# 
# A quick note: if you want to see the 22nd term in the fibonacci it will be the fibonacci number for 21. Thus if you wanted to see the fibonaci number for 22, which is term 23, you would have to enter 23
# #### Info on Fibonacci can be found here https://en.wikipedia.org/wiki/Fibonacci_number

# In[8]:


def fibonacci(num):
    """ 
    Return the next and current terms in a fibonnacie sequence
    """
    
    #if the number is 1 return terms 1,0
    if num == 1:
        return[1,0]
    #case for above 1
    else:
        term=fibonacci(num -1)
        term=[term[0] +term[1],term[0]]
        return term


# In[9]:


def valid_integer():
    """
    Obtain a positive integer less than 200
    """
    
    while True:
        num=int(input('Enter the term in the Fibonacci Sequence you want to see: '))
        try:
            if num>=250:
                print('Enter a number smaller than 250')
            elif num>0:
                return num
                break
            else:
                print('Enter a positive number')
        except:
            print('Enter an integer')


# In[10]:


def get_fibonacci():
    num=valid_integer()
    print(fibonacci(num)[1])


# In[ ]:


## call the get_fibonacci() function to obtain the term you want to see
get_fibonacci()

