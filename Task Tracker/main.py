# importing required modules
import json
import datetime
import click

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
def _add(des: str):
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
def _update(id, des):
    data = get_data()
    if len(data) < id:
        return print("task does not exist")
    for i in data:
        if i["id"] == id:
            i["description"] = des
            i["updatedAt"] = datetime.datetime.now().strftime("%x")
            update_data(data)
            return print(f"Task updated successfully (ID: {id})")
    return print(f"Task does not exist (ID: {id})")

# delete a task
def _delete(id):
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
def _in_progress(id):
    data = get_data()
    if len(data) < id:
        return print(f"Task does not exist (ID: {id})")
    for i in data:
        if i["id"] == id:
            if (i["status"] == "in-progress"):
                return print(f"Task is already in progress (ID: {id})")
            else:
                i["status"] = "in-progress"
                i["updatedAt"] = datetime.datetime.now().strftime("%x")
                update_data(data)
                return print(f"Task status updated successfully (ID: {id})")
    return print(f"Task does not exist (ID: {id})")

def _done(id):
    data = get_data()
    if len(data) < id:
        return print(f"Task does not exist (ID: {id})")
    for i in data:
        if i["id"] == id:
            if (i["status"] == "done"):
                return print(f"Task is already done (ID: {id})")
            else:
                i["status"] = "done"
                i["updatedAt"] = datetime.datetime.now().strftime("%x")
                update_data(data)
                return print(f"Task status updated successfully (ID: {id})")
    return print(f"Task does not exist (ID: {id})")

# list all tasks
def _list():
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
def _list_done():
    c = 0
    try:
        data = get_data()
        if (data):
            for id in data:
                if (id["status"] == "done"):
                    print(id["description"])
                    c += 1
            if c == 0:
                return print("There is no tasks done.")
        else:
            print("there is no data.")
    except:
        print("error listing finished tasks")

def _list_todo():
    c = 0
    try:
        data = get_data()
        if (data):
            for id in data:
                if (id["status"] == "todo"):
                    print(id["description"])
                    c += 1
            if c == 0:
                return print("There is no tasks to do.")
        else:
            print("there is no data.")
    except:
        print("error listing finished tasks")

def _list_in_progress():
    c = 0
    try:
        data = get_data()
        if (data):
            for id in data:
                if (id["status"] == "in-progress"):
                    print(id["description"])
                    c += 1
            if c == 0:
                return print("There is no tasks in progress.")
        else:
            print("there is no data.")
    except:
        print("error listing finished tasks")

# main function
@click.group()
def main():
    pass

@main.command()
@click.argument('description')
def add(description):
    _add(description)

@main.command()
@click.argument('id', type = int)
def delete(id):
    _delete(id)

@main.command()
@click.argument('id', nargs=1)
@click.argument('des', nargs=1)
def update(id, des):
    _update(int(id), des)

@main.command()
@click.argument('id', nargs=1)
def mark_in_progress(id):
    _in_progress(int(id))

@main.command()
@click.argument('id', nargs=1)
def mark_done(id):
    _done(int(id))

@main.command()
@click.option('--option', default=None)
def list(option):
    if (option == None):
        _list()
    elif (option == "todo"):
        _list_todo()
    elif (option == "in-progress"):
        _list_in_progress()
    elif (option == "done"):
        _list_done()
    else:
        click.echo("Not a valid option")

if __name__ == "__main__":
    # calling the main function
    main()