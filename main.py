import test
import train

while True:
    try:
        choice = int(input('\n\nEnter your choice of action: \n\t1: Train the model\n\t2: Print the test images\n\t3: Print the mean face & first five eigen faces\n\t4: Reconstruct the face\n\t5: Exit\n'))
    except ValueError:
        print ("Not a number")
    
    if choice == 1:
        train.training()
    elif choice == 2:
        test.print_test()
    elif choice == 3:
        test.print_eigen()
    elif choice == 4:
        test.recons()
    elif choice == 5:
        print("Thank you for your visit!")
        break
    else:
        print("Invalid Mode")
