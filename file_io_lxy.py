# creat a directory and add a couple of csv files and txt files 
# add another argument to decide with extention to use
# fix the print statement
# try to math the result_ID with the data_ID
# add multiplication and division
# if you can : change the output directory

import argparse        
import sys
import glob 
import os
import re
def create_arg_parser():
    parser = argparse.ArgumentParser(description='Give a short description about what your program should do')
    parser.add_argument(
        '-m','--mode',
        default="listFiles",
        choices=[
            'listFiles',
            'caculate'

        ],
        help='what do you want to do?'

    )

    parser.add_argument(
        '-c','--caculation',
        default="addition",
        choices=[
            'addition',
            'substraction',
            'multiplication',
            'division'

        ],
        help='What caculation do you want to do ?'
        )

    parser.add_argument(
        '-i','--inputPath',
        default='',
        help='Path to your directory that contains the files'
        )

    parser.add_argument(
        '-o','--outputPath',
        default='',
        help='Path to output the result'
        )

    parser.add_argument(
        '-e','--extention',
        default='txt',
        help='the file extention'
        )

    return parser


class calculations():
    def addition(x, y):
        return int(x) + int(y)

    def substration(x, y):
        return int(x) - int(y)

    def multiplication(x, y):
        return int(x) * int(y)    

    def division(x, y):
        return float(x) / float(y)

def listFiles(path,ext):
    # glob.glob will make a list of all files in directory
    # in this case we only list csv files

    files = glob.glob(path + "\\*{e}".format(e=ext))
 
    print(files)
    # return list of files
    return files


def modifyLines(path, calc,outpath,ext):
    # we create the list that contains the files in our directoty
    files = listFiles(path,ext)
    # we want to do something to all of these files
    # so we loop though the list of files
    # we use the enumerate() function to also get the index of the file
    for idx, file in enumerate(files):
        # We open the files as inputfile and we open the result file as outfile
        # the 'w' option means write,we can also supply 'a' for append
        #with 控制以下的整个块
        

        BASENAME = os.path.basename(file)
        ID = re.findall(r"\d+",BASENAME )

        with open(file,'r', encoding='UTF-8') as infile, open("{out}\\result_{n}.{e}".format(out=outpath,n=ID[0],e=ext), "w") as outfile:
            #we go through  all the lines in our infile
            for line in infile:
                # line contains a string e.g."1,9/n"
                # values is a list with two numbers[1,9]
                values = line.replace('\n', '').split(",")

                #selecting the right caculation based on the argument supplied by the -c opption
                if calc == 'addition':
                    result = calculations.addition(values[0], values[1])
                    print('adding {x} plus {y} = {r}'.format(x=values[0],
                                                         y=values[1],
                                                         r=result))
                    #writing to a file
                    outfile.write('{x}, {y}, {r}\n'.format(x=values[0],
                                                       y=values[1],
                                                       r=result))

                elif calc == "substraction":
                    # caculation the function for subtration in class caculation
                    result = calculations.substration(values[0], values[1])

                    print('adding {x} minus {y} = {r}'.format(x=values[0],
                                                         y=values[1],
                                                         r=result))
                    #writing to a file
                    outfile.write('{x}, {y}, {r}\n'.format(x=values[0],
                                                       y=values[1],
                                                       r=result))

                elif calc == "multiplication":
                    result = calculations.multiplication(values[0], values[1])

                    print('adding {x} multiply {y} = {r}'.format(x=values[0],
                                                         y=values[1],
                                                         r=result))
                    #writing to a file
                    outfile.write('{x}, {y}, {r}\n'.format(x=values[0],
                                                       y=values[1],
                                                       r=result))


                elif "division":
                    result = calculations.division(values[0], values[1])

                    print('adding {x} divided by {y} = {r}'.format(x=values[0],
                                                         y=values[1],
                                                         r=result))
                    #writing to a file
                    outfile.write('{x}, {y}, {r}\n'.format(x=values[0],
                                                       y=values[1],
                                                       r=result))       


                else:
                    print("Can't do this")



def main(argv):
    arg_parser = create_arg_parser()
    parsed_args = arg_parser.parse_args(argv)
    mode = parsed_args.mode
    if mode == "listFiles":
        listFiles(parsed_args.inputPath)
    elif mode == "caculate":
        modifyLines(parsed_args.inputPath, parsed_args.caculation, parsed_args.outputPath,parsed_args.extention)
    else:
       print("can't do this")


if __name__ == "__main__":

    print('You are running {script}'.format(script=sys.argv[0]))
    main(sys.argv[1:])



