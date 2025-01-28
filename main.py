# importing required modules
import argparse
import json
import datetime

# create JSON file
def create_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)

# retrieves JSON file into data
def get_data():
    try:
        with open('data.json', 'r') as file:
            try:
                data = json.load(file)
                return data
            except:
                return False
    except:
        create_data([])
        with open('data.json', 'r') as file:
            try:
                data = json.load(file)
                return data
            except:
                return False

# update JSON file from data     
def update_data(data):
    with open('data.json', 'w') as file:
        json.dump(data, file, indent=4)


# adding a new task
def add(des: str):
    data = get_data()
    data.append({
                    "id": len(data) + 1,
                    "description": f"{des}",
                    "status": "todo",
                    "createdAt": datetime.datetime.now().strftime("%x"),
                    "updatedAt": datetime.datetime.now().strftime("%x")
                })
    update_data(data)
    return print(f"Task added succesfully (ID: {len(data)})")

# updating a task
def update(id, des):
    data = get_data()
    if len(data) < id:
        return print("task does not exist")
    for i in data:
        if i["id"] == id:
            i["description"] = des
            update_data(data)
            return print(f"Task updated successfully (ID: {id})")
    return print(f"Task does not exist (ID: {id})")

# delete a task
def delete(id):
    data = get_data()
    if len(data) < id:
        return print(f"Task does not exist (ID: {id})")
    for i in range(len(data)):
        if data[i]["id"] == id:
            data.pop(id-1)
            for j in range(i, len(data)):
                data[j]["id"] = data[j]["id"] - 1
            update_data(data)
            return print(f"Task deleted successfully (ID: {id})")
    return print(f"Task does not exist (ID: {id})")

# marking a task as in progress or done
def in_progress(id):
    data = get_data()
    if len(data) < id:
        return print(f"Task does not exist (ID: {id})")
    for i in data:
        if i["id"] == id:
            if (i["status"] == "in-progress"):
                return print(f"Task is already in progress (ID: {id})")
            else:
                i["status"] = "in-progress"
                update_data(data)
                return print(f"Task status updated successfully (ID: {id})")
    return print(f"Task does not exist (ID: {id})")

def done(id):
    data = get_data()
    if len(data) < id:
        return print(f"Task does not exist (ID: {id})")
    for i in data:
        if i["id"] == id:
            if (i["status"] == "done"):
                return print(f"Task is already done (ID: {id})")
            else:
                i["status"] = "done"
                update_data(data)
                return print(f"Task status updated successfully (ID: {id})")
    return print(f"Task does not exist (ID: {id})")

# list all tasks
def list():
    try:
        data = get_data()
        if(data):
            for id in data:
                print(id["description"])
        else:
            print("there is no data.")
    except:
        print("error listing tasks.")

# Listing tasks by status
def list_done():
    try:
        data = get_data()
        if (data):
            for id in data:
                if (id["status"] == "done"):
                    print(id["description"])
            return print("There is no tasks done.")
        else:
            print("there is no data.")
    except:
        print("error listing finished tasks")

def list_todo():
    try:
        data = get_data()
        if (data):
            for id in data:
                if (id["status"] == "todo"):
                    print(id["description"])
            return print("There is no tasks to do.")
        else:
            print("there is no data.")
    except:
        print("error listing finished tasks")

def list_in_progress():
    try:
        data = get_data()
        if (data):
            for id in data:
                if (id["status"] == "in-progress"):
                    print(id["description"])
            return print("There is no tasks in progress.")
        else:
            print("there is no data.")
    except:
        print("error listing finished tasks")

# main function
def main():
    # create a parser object
    parser = argparse.ArgumentParser(description= "A task tracker program.")

    # add argument
    parser.add_argument("-l", "--list",
                        help = "lists all tasks.")
    parser.add_argument("-a", "--add", type = str, nargs = 1,
                        metavar = "description", default = None,
                        help = "add a task in a list.")
    # parse the arguments from standard input
    args = parser.parse_args()

    # check if add argument has any input data.
    if args.list:
        return list()

if __name__ == "__main__":
    # calling the main function
    main()