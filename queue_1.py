class Queue:
    def __init__(self, elements = None):
      if(elements == None):
        self.elements = list()
      else:
        self.elements = elements
    
    def enqueue(self, item):
        self.elements.append(item)
    
    def dequeue(self):
      if(len(self.elements) > 0):
        return self.elements.pop(0)
      
    def get_size(self):
        return len(self.elements)
    
    def __str__(self):
        return str(self.elements)
    
element = Queue()
print (element)

#ADDING DATA TO QUEUE
count=1
number_of_value = eval(input("Enter the number of value you want in queue:"))
while count <= number_of_value:
   data = input(str(count) + " Actual data you want to add in queue: ")
   element.enqueue(data)
   count=count+1

print(element)

#REMOVING DATA FROM FRONT OF THE QUEUE
count = 1
number_of_del_value = eval(input("Enter the number of value you want to delete from queue:"))
while count <= number_of_del_value:
   element.dequeue()
   count=count+1

print(element)

#CURRENT STATE OF QUEUE
print(element.get_size())