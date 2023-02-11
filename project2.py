#this program is to give summary about your alphabetical usage

print("welcome to the program")
def project2():
             from collections import Counter
             a = input("type anything:")
             my_counter = Counter(a)
             print (my_counter)
             continue_program = input("Do you want to continue the program? (y/n): ")
             while continue_program.lower() == "y":
              return project2()
             else:
              print("\n***THANK YOU***\n")
                  
project2()