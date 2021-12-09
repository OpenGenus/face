from face_recons import test
from face_recons import train
import argparse


parser = argparse.ArgumentParser(description = "Face Application - Command Line Interface")
parser.add_argument("--mode", default = False, help="Enable Command Line Interface", action='store')
parser.add_argument("--input", type=str, required=False, help="Enter the name of Test image in format: directory/image_name.jpg")
parser.add_argument("--dataset", type=str,required=False, help="Enter the name of directory for Training the model")
args, unknown = parser.parse_known_args()

if(args.mode == False):
    while True:
        try:
            choice = int(input('\n\nEnter your choice of action: \n\t1: Train the model\n\t2: Print the test images\n\t3: Print the mean face & first five eigen faces\n\t4: Reconstruct the face\n\t5: Exit\n'))
        except ValueError:
            print ("Not a number")
        if choice == 1:
            train.directory_name = input('Enter the path of directory :\n')
            train.training()
        elif choice == 2:
            test.print_test()
        elif choice == 3:
            test.print_eigen()
        elif choice == 4:
            test.image_file = input('Enter the name of image in format: directory_path/.../image_name.jpg\n')
            test.recons()
        elif choice == 5:
            print("Thank you for your visit!")
            break
        else:
            print("Invalid Mode")
else:
    train.directory_name = args.dataset
    train.training()
    test.image_file = args.input
    test.recons()
