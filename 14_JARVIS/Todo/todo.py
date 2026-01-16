import json
import sys
import os

from utils.common import speak
from utils.common import listen_for_something
from utils.common import resource_path

file = resource_path(os.path.join("Todo" , "todo.txt"))
def addTask():
    try:
        print("Sir , Please tell me your task")
        speak("Sir , Please tell me your task")
        task = listen_for_something("Listening for task...")
        # task = input("task = ")
        if task == 'exit': 
            print("Process aborted")
            return
        obj = {
            "task": task,
            "status": "Not completed",
        }

        tasks = []
        with open(file, "a+") as g:
            g.seek(0)
            for line in g:
                tasks.append(json.loads(line))

        for t in tasks:
            if t["task"].lower() == task.lower():
                print("Task already existed")
                return
        tasks.append(obj)
        with open(file, "w") as f:
            for t in tasks:
                f.write(json.dumps(t) + "\n")

        print("Task added successfully")

    except Exception as e:
        print("error in adding task:", e)

def toogle(status):
    return "completed" if status.lower() == 'not completed' else 'not completed'

def updateTask():
    list = ReadTasks()
    if(len(list) == 0): return
    print("Which task do you want to update")
    speak("Which task do you want to update")
    task = listen_for_something("Listening for task...")
    # task = input("ENter task = ")
    if task == 'exit':
        print("The process is aborted")
        return
    match = False
    for i in list:
        if(i['task'].lower() == task.lower()):
            i['status'] = toogle(i['status'])
            match = True
            break
    if(not match) : return
    print(list)
    with open(file , 'a+') as f:
        f.seek(0)
        for t in list:
            f.write(json.dumps(t) + "\n")
    return

def DeleteTask():
    list = ReadTasks()
    if(len(list) == 0) : return
    print("Which task do you want to delete")
    speak("Which task do you want to delete")
    task = listen_for_something("Listening for task...")
    if task == 'exit':
        print("The process is aborted")
        return
    match = False
    for i in list:
        if(i['task'].lower() == task.lower()):
            list.remove(i)
            match = True
            break
    if(not match) : return   
    with open(file , 'w') as f:
        for t in list:
            f.write(json.dumps(t) + "\n")
    return

def ReadTasks():
    try:
        list = []
        length = 125
        with open(file , 'a+') as f:
            f.seek(0)
            line = f.readline()
            while (line != ''):
                list.append(json.loads(line))
                line = f.readline()
        if(len(list) == 0):
            print("Sir, you dont have added any task yet")
            speak("Sir, you dont have added any task yet")
            return []
        else:
            print("\n" + "="*length) 
            print("📌 TODO List".center(length)) 
            print("="*length)
            for index,item in enumerate(list, start=1):
                a = str(index)+". "+item['task']
                print(f"{a:<50}" , end="")
                if index%3 == 0 : print()
            print()
            print("="*length)
            speak("The tasks has been shown on screen")
        return list
    except Exception as e:
        print(e)
        print("Please add a task first")
        speak("Please add a task first")

def clearTasks():
    open(file , 'w').close()

if __name__ == "__main__":
    # ReadTasks()
    updateTask()
    # DeleteTask()
    