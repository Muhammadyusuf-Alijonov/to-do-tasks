import pymongo
import time

client = pymongo.MongoClient("mongodb+srv://alijanovm01:passInha2304@cluster0.ossutgo.mongodb.net/?retryWrites=true&w=majority")
db = client['tasks']
collection = db['taskcoll']
time_epoch = time.time()
current_time = time.ctime(time_epoch)


class Tasks:
    def insert(self):
        title = str(input("Enter title for your task: "))
        task = str(input("Enter your task: "))
        collection.insert_one({"Title": title, "Task": task, "Time added": current_time})

    def display(self):
        result = collection.find({}, {"_id": 0, "Title": 1, "Task": 1, "Time added": 1})
        for data in result:
            print(data)

    def delete(self):
        delete_task = str(input("Enter title of task you would liek to delete: "))
        collection.delete_one({"Title": delete_task})
        print("Task deleted!")


task = Tasks()
while True:
    program = int(input("1. Display all tasks.\n2. Insert new task.\n3. Delete task\n0. Exit program. "))
    match program:
        case 1:
            task.display()
        case 2:
            task.insert()
        case 3:
            task.delete()
        case 0:
            print("Exiting program...")
            break
