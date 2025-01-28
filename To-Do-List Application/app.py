from flask import Flask,render_template,jsonify,request

app=Flask(__name__)

tasks=[
        {'id':1,'task':'Go to gym','done':False},
        {'id':2,'task':'Buy groceries','done':False}
       ]

# Route to render the HTML page
@app.route('/')
def home():
    return render_template('index.html',tasks=tasks)

# API to fetch all tasks
@app.route('/api/tasks', methods=['GET'])
def get_task():
    return jsonify(tasks)

# API to add a new task
@app.route('/api/tasks', methods=['POST'])
def add_task():
    task_data=request.form
    task_id=task_data.get('id',len(tasks)+1)
    task_content=task_data.get('task','Default Task')
    task_done=task_data.get('done',False)
    new_task={'id':task_id,'task':task_content,'done':task_done}
    tasks.append(new_task)
    return jsonify({'message':'Task has been added successfully.'})


##another way to add new task:
'''def add_task():
    data=request.json
    new_task={'id':data["id"],'task':data["task"],'done':data["done"]}
    tasks.append(new_task)
    return jsonify({'message':'Task has been added successfully.'})'''

# API to update a task
@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data=request.json
    for task in tasks:
        if task["id"]==task_id:
            task["done"]=data.get("done",task["done"])
            return jsonify({"message":"Task Updated successfully"})
    return jsonify({"error":"Cannot Find The Requested Task"})
    

# API to delete a task
@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    global tasks
    tasks=[task for task in tasks if task["id"]!=task_id]           #This basically means return task from tasks whose id is not same as id of the task to be deleted and assign those task to tasks. 
    return jsonify({"message":"Task Deleted Successfully."})


if __name__=="__main__":
    app.run(debug=True)

