
# coding: utf-8

# # Finding Pi to the Nth Digit.
# #### Here a user enters a number and Pi is generated to that decimal places. Limit is set to

# Creating Generator Function calc_pi

# In[19]:


def calc_pi(limitnumber):
    """ 
    Print out decimal places of PI until it reaches the limiting number
    """
    
    a, b, c, d, e, f=1, 0, 1, 1, 3, 3
    
    counter=0
    decimal_place=limitnumber
    
    while counter != decimal_place + 1:
        if 4 * a + b - c < e * c:
                yield e
                if counter == 0:
                        yield '.'
                            
                if decimal_place == counter:
                        print('')
                        break
                        
                counter += 1
                eb = 10 * (b - e * c)
                e = ((10 * (3 * a + b)) // c) - 10 * e
                a *= 10
                b = eb
        else:
                eb = (2 * a + b) * f
                ee = (a * (7 * d) + 2 + (b * f)) // (c * f)
                a *= d
                c *= f
                f += 2
                d += 1
                e = ee
                b = eb




# In[53]:


def display_pi_digits():
    pi_digits=calc_pi(int(input('Enter the number of decimals of pi you want to calculate, max is 40:')))
    
    g=0
    
    while g<50:
        for dig in pi_digits:
            print(dig, end='')
            g+=1
            if g ==50:
                break


# In[54]:


display_pi_digits()


# In[52]:




