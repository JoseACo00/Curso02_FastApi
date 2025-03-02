from pymongo import MongoClient

#Base de datos local
# db_client = MongoClient()

#BASE DE DATOS REMOTAS
db_client = MongoClient("mongodb+srv://alexcoca100:alexcoca100@pythonfastapi.qmkwz.mongodb.net/?retryWrites=true&w=majority&appName=PythonFastAPI").FastAPI