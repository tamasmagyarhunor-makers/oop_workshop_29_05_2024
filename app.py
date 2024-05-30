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
        return "Hey pal, how are you?"

class GermanPerson():
    def say_hello():
        return "Hallo, Guten Tag!"

class SpanishPerson():
    def say_hello():
        return "Buenos días!"

class EnglishPerson():
    def say_hello():
        return "Hey pal, how are you?"
    
class AustralianPerson():
    def say_hello():
        return "Hey pal, how are you?"

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
    
    def write(self, write_object, text):
        if write_object.type == "ball pen":
            self.__turn_on(write_object)
            return text
        elif write_object.type == "ink pen":
            if self.__has_enough_ink(write_object):
                return text
            else:
                self.__refill_ink(write_object)
                return text
        elif write_object.type == 'pencil':
            if self.__sharp_enough(write_object):
                return text
            else:
                self.__sharpen(write_object)
                return text
        else:
            return "need some write object to write"
            
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


# BallPen, InkPen and Pencil
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
    

    
    
