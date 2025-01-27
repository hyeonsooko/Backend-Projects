# importing required modules
import argparse
import os

# error messages
INVALID_FILETYPE_MSG = "Error: Invalid file format. %s must be a .txt file."
INVALID_PATH_MSG = "Error: Invalid path/name. Path %s does not exist."

# file handling
def validate_file(file_name):
    """
    validate file name and path
    """
    if not valid_path(file_name):
        print(INVALID_PATH_MSG%(file_name))
        quit()
    elif not valid_filetype(file_name):
        print(INVALID_FILETYPE_MSG%(file_name))
        quit()
    return

def valid_filetype(file_name):
    # validate file type
    return file_name.endwith('.txt')

def valid_path(path):
    # validate file path
    return os.path.exists(path)

# retrieves JSON file into data
"""
data should look like this:
{
    {
        id: int
        description: str
        status: str(todo, in-progress, done)
        createdAt: Date
        updatedAt: Date
    }
}
"""

def list_task():
    return

# main function
def main():
    # create a parser object
    parser = argparse.ArgumentParser(description= "An addition program")

    # add argument
    parser.add_argument("list", nargs= 1,
                        help = "lists all tasks.")

    # parse the arguments from standard input
    args = parser.parse_args()

    # check if add argument has any input data.
    # If it has, then print sum of the given numbers
    if len(args.list) == 0:
        print(list_task())

if __name__ == "__main__":
    # calling the main function
    main()