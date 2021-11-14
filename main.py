from flask import Flask, json, jsonify, request

app = Flask(__name__)


tasks = [
    
    {
        "id" : 1,
        "name" : "Miheal",
        "contact": "iluvuniccorns27",
        "done": False
    }  ,
    {
        "id" : 2,
        "name" : "Amy",
        "contact": "Kevin Hart",
        "done": False 
    },    
]


@app.route("/add-data", methods=["POST"])
def addTask():
    if not request.json:
        return jsonify({
        
        "status": "Error",
        "message": "Please provide data in required format."
        
        })
    task = {
        "id" : tasks[-1]["id"]+1,
        "name": request.json["name"],
        "contact": request.json["contact"],
        "done": False
    }
    
    tasks.append(task)
    
    return jsonify({
        
        "status": "Success",
        "message": "Task added succsesfully! :)"
        
        })

if(__name__ == "__main__"):
    app.run(debug=True)