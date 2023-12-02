from flask import Flask, request, jsonify
import json
from datetime import datetime

app = Flask(__name__)

class Task:
    def __init__(self, task_id, description, created_at, status):
        self.task_id = task_id
        self.description = description
        self.created_at = created_at
        self.status = status

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def get_all_tasks(self):
        return self.tasks

    def update_task(self, task_id, new_task):
        for i, task in enumerate(self.tasks):
            if task.task_id == task_id:
                self.tasks[i] = new_task
                return True
        return False

    def delete_task(self, task_id):
        for i, task in enumerate(self.tasks):
            if task.task_id == task_id:
                del self.tasks[i]
                return True
        return False

# Inicializar o TaskManager
task_manager = TaskManager()

@app.route('/create_task', methods=['POST'])
def create_task():
    data = request.get_json()

    # Adicionar validações aqui

    task_id = str(len(task_manager.tasks) + 1)  # Pode ser gerado de forma mais robusta
    description = data['description']
    created_at = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status = "Pendente"

    new_task = Task(task_id, description, created_at, status)
    task_manager.add_task(new_task)

    return jsonify({"message": "Tarefa criada com sucesso", "task_id": task_id})

@app.route('/get_task/<task_id>', methods=['GET'])
def get_task(task_id):
    task = task_manager.get_task(task_id)

    if task:
        return jsonify({"task_id": task.task_id, "description": task.description,
                        "created_at": task.created_at, "status": task.status})
    else:
        return jsonify({"message": "Tarefa não encontrada"}), 404

@app.route('/get_all_tasks', methods=['GET'])
def get_all_tasks():
    tasks = [{"task_id": task.task_id, "description": task.description,
              "created_at": task.created_at, "status": task.status} for task in task_manager.get_all_tasks()]

    return jsonify({"tasks": tasks})

@app.route('/update_task/<task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.get_json()

    # Adicionar validações aqui

    task = task_manager.get_task(task_id)
    if task:
        new_task = Task(task_id, data['description'], task.created_at, data['status'])
        if task_manager.update_task(task_id, new_task):
            return jsonify({"message": "Tarefa atualizada com sucesso"})
        else:
            return jsonify({"message": "Falha ao atualizar a tarefa"}), 500
    else:
        return jsonify({"message": "Tarefa não encontrada"}), 404

@app.route('/delete_task/<task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = task_manager.get_task(task_id)
    if task:
        if task_manager.delete_task(task_id):
            return jsonify({"message": "Tarefa excluída com sucesso"})
        else:
            return jsonify({"message": "Falha ao excluir a tarefa"}), 500
    else:
        return jsonify({"message": "Tarefa não encontrada"}), 404

if __name__ == '__main__':
    app.run(debug=True)
