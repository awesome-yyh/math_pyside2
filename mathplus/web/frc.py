def circulator_to_fraction(circulator):
    """无限循环小数转分数"""
    dot = circulator.find('.')
    left_p = circulator.find('(')

    if left_p != -1:
      rigth_p = circulator.find(')')
    
      true_circulator = float(circulator[:left_p] + circulator[left_p+1:-1])

      first_shift = left_p-dot-1
      second_shift = rigth_p-left_p-1+first_shift
      
      first_base = 10**first_shift
      second_base = 10**second_shift

      denominator = second_base - first_base  #分母
      numerator = int(true_circulator*second_base) - int(true_circulator*first_base)  #分子
                  
      return [numerator,denominator]
    else:
      print('no')
      print(dot)
      little = circulator[dot+1:]
      a = 10**(len(little))
      b = int(float(circulator)*a)
      return [b,a]


def hcf(x, y):
   """该函数返回两个数的最大公约数"""
   if x > y:
       smaller = y
   else:
       smaller = x
 
   for i in range(1,smaller + 1):
       if((x % i == 0) and (y % i == 0)):
           hcf = i
   return hcf

def myfrc(circulator):
	frc = circulator_to_fraction(circulator)
	h = hcf(frc[0],frc[1])
	return str(int(frc[0]/h))+'/'+str(int(frc[1]/h))

if __name__ == '__main__':
    print(myfrc('56.2'))
    