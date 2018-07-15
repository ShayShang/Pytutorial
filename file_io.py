"""
this script have two options
a）list the files in a directory

b）modify these files by applying a caculation
    There are two options for the caculation
    -addition
    -subtraction
"""



# import os  # Operating system
# import configparser  # parsing arguments from a configuration file
import argparse        #this will import the argparse module
import sys
import glob            #this module will help you to list files in directory


def create_arg_parser():
    """"
    Creates and returns the ArgumentParser object.
    """
    parser = argparse.ArgumentParser(description='Give a short description about what your program should do')
    parser.add_argument(
        # you must use a short version and a long version -m and --mode
        '-m', '--mode',
        # you can ,but have to supply a default value
        default="info",
        #the choise are important to limit the possibilities for wrong input
        choices=[
            'listFiles',
            'calculate'
        ],
        #give a short help about this argument
        help='What do you want to do?'
    )
    parser.add_argument(
        '-c', '--calculation',
        default="addition",
        choices=[
            'addition',
            'substraction'
        ],
        help='What calculation do you want to do?'
    )
    parser.add_argument(
        '-i', '--inputPath',
        default="",
        help='Path to your directory that contains the files'
    )
    return parser


class calculations():
    def addition(x, y):
        return int(x) + int(y)

    def substration(x, y):
        return int(x) - int(y)


def listFiles(path):
    # glob.glob will make a list of all files in directory
    # in this case we only list csv files
    files = glob.glob(path + "\\*.csv")
    print(files)
    # return list of files
    return files


def modifyLines(path, calc):
    # we create the list that contains the files in our directoty
    files = listFiles(path)
    # we want to do something to all of these files
    # so we loop though the list of files
    # we use the enumerate() function to also get the index of the file
    for idx, file in enumerate(files):
        # We open the files as inputfile and we open the result file as outfile
        # the 'w' option means write,we can also supply 'a' for append
        #with 控制以下的整个块
        with open(file) as infile, open("result_{n}.csv".format(n=idx), "w") as outfile:
            #we go through  all the lines in our infile
            for line in infile:
                # line contains a string e.g."1,9/n"
                # values is a list with two numbers[1,9]
                values = line.replace('\n', '').split(",")

                #selecting the right caculation based on the argument supplied by the -c opption
                if calc == 'addition':
                    result = calculations.addition(values[0], values[1])
                elif calc == "substraction":
                    # caculation the function for subtration in class caculation
                    result = calculations.substration(values[0], values[1])
                else:
                    print("Can't do this")

                print('adding {x} plus {y} = {r}'.format(x=values[0],
                                                         y=values[1],
                                                         r=result))

                #writing to a file
                outfile.write('{x}, {y}, {r}\n'.format(x=values[0],
                                                       y=values[1],
                                                       r=result))


def main(argv):
    """
    the main function sends  the different attribute to the corresponding functions

    """

    # getting the information from the command line
    # create the argument paraser/reader function
    arg_parser = create_arg_parser()
    # evaluate the argument list in argv and save them in parsed_args
    parsed_args = arg_parser.parse_args(argv)

    mode = parsed_args.mode
    if mode == "listFiles":
    #parsed_args.input is your directory that you secified with i-option
        listFiles(parsed_args.inputPath)
    else:  # elif mode == "modifyLines":
    # we call modifylines function with the inputpath and caculation we want to do
        modifyLines(parsed_args.inputPath, parsed_args.calculation)


if __name__ == "__main__":
    #we cll the main() function
    #the content of sys.argv[1:] '=' '-m listfiles -c subtraction -i D:/tables'
    print('You are running {script}'.format(script=sys.argv[0]))
    main(sys.argv[1:])
