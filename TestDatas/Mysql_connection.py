import mysql.connector

def get_values():
    connection = mysql.connector.connect(host="localhost", user="3306", password="Muruga@3", database = "automation_testing")
