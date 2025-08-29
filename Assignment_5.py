try:
    what=input("what you want to perform: \n 1.Create a Dictonary of student marks: \n 2.Demonstrate List Slicing: ")
    what=int(what)
    if what==1:
        # Task 1: Create a Dictonary of student marks
            student_rec = {'Arka': '90', 'Joy': '95'}
            student = input("Enter the Student's name: ")
            take = student in student_rec
            if take == True:
                marks = student_rec[student]
                print("{}'s marks: {}".format(student, marks))
            else:
                print("Student Not found")
    elif what==2:
        # Task 2: Demonstrate List Slicing
        number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        z=[]
        for i in range(5):
            i=number[i]
            z.append(i)
        print("Original list: {} \nExtracted first five elements: {}".format(number,z))
        z.reverse()
        print("Reversed extracted Elements: ",z)
    else:
         print("Enter valid choice")
except ValueError:
    print("Enter a number")