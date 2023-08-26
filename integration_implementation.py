from scipy.integrate import quad #single integration
from scipy.integrate import dblquad #double integration
from scipy.integrate import nquad # n time integration

def f(x):
    return x

area = quad(f,0,2)  #function,lower boundry,upper boundry    
print(area)

def f(x, y):
    return (x*y)

area = dblquad(f,0,2,0,5)  #function,lower boundry,upper boundry for x and the boundries for y    
print(area)