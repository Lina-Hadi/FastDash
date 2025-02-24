from fastapi import APIRouter 
from fastapi import FastAPI
from models.sql_model import Todo
import all_routes
import operations.to_do as db


todo_route = APIRouter()

# create a new todo
@todo_route.post(all_routes.todo_create)
def new_todo(doc: Todo):
    doc = dict(doc)
    todo: str = doc['todo']
    res = db.create_to_do(todo)
    return res

@todo_route.get_all(all_routes.todo_all)
def all_todos():
    res = db.get_all()
    return res

@todo_route.get_one(all_routes.todo_one)
def todo_one(_id: int):
    res = db.update_todo(_id, title)
    return res

@todo_route.patch(all_routes.todo_update)
def todo_update(_id: int, doc: Todo):
    doc = dict(doc)
    title: str = doc['todo']
    res = db.get_one(_id)
    return res

@todo_route.delete(all_routes.todo_delete)
def todo_delete(_id: int, doc: Todo):
    res = db.delete_todo(_id)
    return res