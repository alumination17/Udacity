
"""You can use this class to represent how classy someone or something is.
"Classy" is interchangable with "fancy". If you add fancy-looking items, you will increase your "classiness".
Create a function in "Classy" that takes a string as input and adds it to the "items" list.
Another method should calculate the "classiness" value based on the items. The following items have classiness points associated with them:
"tophat" = 2, "bowtie" = 4, "monocle" = 5
Everything else has 0 points. Use the test cases below to guide you!"""

class Classy(object):
    
    def __init__(self):
        self.items = []
        self.classiness = 0

    def addItem(self, item):
        self.items.append(item)

    def getClassiness(self):
        for i in self.items:

            if i == 'tophat':
                self.classiness += 2
                self.items.pop(0)
            elif i == 'bowtie':
                self.classiness += 4
                self.items.pop(0)
            elif i == 'monocle':
                self.classiness += 5
                self.items.pop(0)
            else:
                self.classiness += 0
                self.items.pop(0)

        self.items.pop(0) if self.items else False
        return self.classiness
             
# Test cases
me = Classy()

# Should be 0
print (me.getClassiness())
# print(me.items)

me.addItem("tophat")
# Should be 2
print (me.getClassiness())
# print(me.items)

me.addItem("bowtie")
# Should be 6
# print (me.getClassiness())
# print(me.items)

me.addItem("jacket")
# Should be still 6
# print (me.getClassiness())
# print(me.items)

me.addItem("monocle")
# Should be 11
print (me.getClassiness())
# print(me.items)

me.addItem("bowtie")
# Should be 15
print (me.getClassiness())
# print(me.items)