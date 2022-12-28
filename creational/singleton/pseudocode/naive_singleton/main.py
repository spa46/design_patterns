from Singleton import Singleton 

if __name__ == '__main__':
  s1 = Singleton()
  s2 = Singleton()

  if s1 is s2:
    print('Success')
  else:
    print('Fail')