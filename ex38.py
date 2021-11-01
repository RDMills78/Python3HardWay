>>>class Thing(object):
    def test(message):
        print(message)

a = Thing()
a.test("hello  ")        
Tracebock (most recent call last):
    File "<stdin>" line 1, in <module>
TypeError: test() takes exactly 1 argument (2 given)    
>>>
