import datetime
# Object Oriented Programming
## A - Abstraction
## 
## P - Polymorphism
## I - Inheritance
## E - Encapsulation* 

# * you might find different interpretations of it


# Inheritance and Polymorphism
## Inheritance
### DRY - dont repeat yourself 
### Not using Inheritance
class AmericanPerson():
    def say_hello():
        return "Hey pal, how are you?" # 1.

class GermanPerson():
    def say_hello():
        return "Hallo, Guten Tag!"

class SpanishPerson():
    def say_hello():
        return "Buenos días!"

class EnglishPerson():
    def say_hello():
        return "Hey pal, how are you?" # 2.
    
class AustralianPerson():
    def say_hello():
        return "Hey pal, how are you?" # 3.

### Using Inheritance
class Person():
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        return "Hey pal, how are you?"

class AmericanPerson(Person):
    pass

class EnglishPerson(Person):
    pass

class AustralianPerson(Person):
    pass

## Polymorphism
class GermanPerson(Person):
    def say_hello(self):
        return "Hallo, Guten Tag!"
    
### Liskovs example
class Animal():
    def breath_air():
        pass

class Mammal(Animal):
    def breath_air():
        pass
    pass

class Fish():
    pass

class GoldFish(Mammal): # breaking the principle

    pass

gold_fish = GoldFish()
gold_fish.breath_air() # => it would break

# ===================== BREAK ====================== # 














# Abstraction and Encapsulation
## Abstraction
### no Abstraction
# what are the problems here when we don't use Abstraction?
class WriteObject():
    def __init__(self, type):
        self.type = type

class Notebook():
    def __init__(self, write_object):
        self.write_object = write_object
    
    def write(self, text):
        if self.write_object.type == "ball pen":
            self.__turn_on(write_object)
            return text
        elif self.write_object.type == "ink pen":
            if self.__has_enough_ink(write_object):
                return text
            else:
                self.__refill_ink(write_object)
                return text
        elif self.write_object.type == 'pencil':
            if self.__sharp_enough(write_object):
                return text
            else:
                self.__sharpen(write_object)
                return text
        else:
            raise Exception("need some write object to write")
            
    # private methods
    def __sharpen(write_object):
        # sharpen the pencil
        pass

    def __refill_ink(write_object):
        # refill ink
        pass

    def __sharp_enough(write_object):
        # check if pencil is sharp enough
        pass


    def __has_enough_ink(write_object):
        # check if ink pen it has enough ink
        pass

    def __turn_on(write_object):
        #press the top of the ball pen to turn it on
        pass 

# example
write_object = WriteObject('pencil')
notebook = Notebook(write_object)
notebook.write(notebook.write_object, 'My daily memos')

### with Abstraction

class WriteObject(): # abtract
    def __init__(self):
        raise Exception('WriteObject cant be instantiated')
    
    def write(self, text):
        raise Exception('WriteObject cant write, please instantiate a Pencil, Ink Pen or Ball Pen')
    
class Pencil(WriteObject):
    def __init__(self):
        pass

    def write(self, text):
        if self.__sharp_enough():
            return text
        else:
            self.__sharpen()
            return text
        
    # private
    def __sharp_enough(self):
        # check if the pencil is sharp enough
        pass

    def __sharpen(self):
        # sharpen the pencil
        pass

class BallPen(WriteObject):
    def __init__(self):
        pass

    def write(self, text):
        self.__turn_on()
        return text
    
    #private
    def __turn_on():
        # turn on the ball pen
        pass


class InkPen(WriteObject):
    def __init__(self):
        pass

    def write(self, text):
        if self.__has_enough_ink():
            return text
        else:
            self.__refill_ink()
            return text
        
    #private

    def __has_enough_ink(self):
        # check if there is enough ink
        pass

    def __refill_ink(self):
        # refill the ink
        pass


# BallPen, InkPen and Pencil => WriteObject 
class Notebook():
    def __init__(self, write_object):
        self.write_object = write_object

    def write(self, text):
        return self.write_object.write(text)












## Encapsulation
class MobilePhone():
    def __init__(self, memory: int, cores :int, colour: str):
        self.__memory = memory
        self.__cores = cores
        self.__colour = colour
    
    # __memory 
    
    def get_memory(self):
        return self.__memory
    
    def launch_application(self, application):
        self.__start_application(self.__memory / 10, application)

    def __set_memory(self, memory):
        self.__memory = memory

    def __start_application(self, memory_count, application):
        pass
        # allocate memory_count and start application


# exclusion
class Post():
    def __init__(self, id, content):
        self.id = id
        self.content = content

    

        # getters and setters
        # getter to read a property
        # setter to set/change a property
    

    
# SOLID principles
## Single Responsibility principle
## Open/Closed principle
## Liskov's substitution principle
## Interface seggregation principle
## Dependency Inversion principle


## Single Responsibility principle

### not singularly responsible
### singularly responsible

class Account():
    # only the accountants in the business are responsible for requiring features for the Account object.
    pass

#### 

class Transaction():
    def __init__(self, sum, type):
        transactions = []
        self.sum = sum
        self.type = type
        self.date = datetime.now()
        # function
        # function

class StatementPrinter():
    def __init__(self):
        return
    
    def print_statement(self, transaction):
        # make a new statement string to store statement data
        # add header
        # iterate over transactions data
        # add transaction data for each transaction object to the string
        # add footer
        # return or print statement string
        return

class BankAccount():
    def __init__(self):
        self.balance = 0
        self.transactions = Transaction()
        self.printer = StatementPrinter()

    def withdraw(self, sum):
        # do the checks
        # make new transaction data
        # withdraw
        return

    def deposit(self, sum):
        # do the checks
        # make new transaction data
        # self.transactions.add()
        # {'type': 'deposit', 'sum': sum, 'date': datetime.now()} => new Transaction(sum, type)
        # deposit
        return
    
    def print_statement(self, transaction):
        # ....
        # self.printer.print_statement(transaction)
        return
    

  ## Open/Closed principle

  ## Liskov's substitution principle

class HTTPRequest():
    pass

class HTTPResponse():
    pass

class JSONResponse(HTTPResponse):
    pass

class Application():
    users = []
    def send_response(res :HTTPResponse): # HTTPResponse
       res.data.users = users
       return res
    

    

class SomeOtherApplication():

    def deal_with_response():
        response = JSONResponse()
        send_response(response)

  ## Interface seggregation principle

class Animal(): # abstract or built in an unusable way, only to force behaviour on its child classes
    def __init__(self):
        raise Exception('Animal class its meant to be abstract, not to be instantiated')
    
    def move(self):
        raise Exception('move() hasnt been implemented, please implement it!')
    
    # def fly(self):
    #     raise Exception('please implement the fly method')

class Bird(Animal):
    def __init__(self):
        pass

    def fly(self):
        return 'it flies'
    
class Hawk(Bird):
    pass

class Mammal(Animal):
    pass

class Zebra(Mammal):
    def __init__(self):
        pass

    def move():
        return 'it moves'
    
    # def fly(self):
    #     return 'fly'



animal = Zebra() # => 


  ## Dependency Inversion principle
  ### Classes should depend on Abstractions not concretions

  ### Depency Inversion principle NOT respected
class Base64Hasher():
    # hashing password with 64bit security
    pass

class Base128Hasher():
    pass

class Base256Hasher():
    pass

if date < '2024':
    use PasswordService2024

if date < '2025':
    use PasswordService2025


# tighly coupled
class PasswordService():
    def __init__(self):
        self.hasher = Base64Hasher()

    def hash_password(self, string):
        return self.hasher.hash(string)
    

  ### Depency Inversion principle respected

class BaseHasher():

    def hash_password():
        raise Exception('you have implement the hash_password method()')
    

#### 2023
hasher = Base64Hasher() # => BaseHasher

password_service = PasswordService(hasher)
password_service.hash_password('admin123')

#### 2024

hasher = Base128Hasher() # => BaseHasher

password_service = PasswordService(hasher)
password_service.hash_password('admin123')

#### 2025

hasher = Base256Hasher() # => BaseHasher

password_service = PasswordService(hasher)
password_service.hash_password('admin123')


class PasswordService():
    def __init__(self, hasher = Base256Hasher()):
        self.hasher = hasher

    def hash_password(self, string):
        return self.hasher.hash(string)
    
