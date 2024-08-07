def myDecorator(func) :
    def nestedfunc() :
       print("Sugar Added From Decorators")

       func()
       
       print('=' * 30)

    return nestedfunc
@myDecorator      
def make_tea():
  print("Tea Created")

@myDecorator
def make_coffe():
  print("Coffe Created")

make_tea()
make_coffe()
