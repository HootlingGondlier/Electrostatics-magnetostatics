import math
def electrostaticForce():
  k=1/(4*math.pi*8.854187817e-12)
  i=input('What to find F,q,Q,r: ')
  if i == 'F':
    q=float(input('Enter value of charge: '))
    Q=float(input('Enter value of test charge: '))
    r=float(input('Enter value of distance between two charge: '))
    F = (k*q*Q)/r
    return print('The force is: ',F)

  elif i == 'q':
    Q=float(input('Enter value of test charge: '))
    r=float(input('Enter value of distance between two charge: '))
    F=float(input('Enter value of coulomb force: '))
    q=(F*r)/(k*Q)
    return print('The charge is: ',q)

  elif i == 'Q': 
      r=float(input('Enter value of distance between two charge: '))
      F=float(input('Enter value of coulomb force: '))
      q=float(input('Enter value of charge: '))
      Q=(F*r)/(k*q)
      return print('The test charge is: ',Q)

  elif i == 'r':
        q=float(input('Enter value of charge: '))
        Q=float(input('Enter value of test charge: '))
        F=float(input('Enter value of coulomb force: '))
        r=(k*q*Q)/F
        return print('The distance between two charge particle is: ',r)

  else:
    return 'invalid syntax'

electrostaticForce()