import mysql.connector
import os
print("ZanvokDB 1.0 Beta")
print("Interface for RDBMS(Client/Server)")
print("Supported and tested on MySQL and MariaDB")
print("=" * 45)
print()
mydb = mysql.connector.connect(
    host = input("localhost"),
    user = input("root"),
    password = input("Enter your password: "),
    database = input("Connect a DataBase if you want: ")
)


mycursor = mydb.cursor()
command = ""
while command != "quit":
    command = input("ZanvokDB> ")
    if command == "zdb help":
        print("Use basic and general SQL commands")
        print("ZanvokDB uses MySQL as its base")
    elif command == "zdb version":
        print("ZanvokDB v1.0 BETA")
        print("Zanvok Corporation")
        print("=" * 10)
        print("MySQL Python Connector")
    elif command == "shell":
        print("Shell under development")
    elif command == "ping":
        os.system('ping localhost')
    elif command == "db":
        print("Popular DBMSs and RDBMs")
        print("\t PostgreSQL")
        print("\t MariaDB")
        print("\t MySQL")
        print("\t MongoDB")
        print("\t Microsoft SQL Server")
        print("\t Microsoft Access")
        print("\t LibreOffice/OpenOffice/ApacheOffice DataBase")
    elif command == "zdb developers" or command == "zdb developer":
        print("Gautham Nair")
    elif command == "commit":
        mydb.commit()
        print(mycursor.rowcount, "record(s) affected")
    elif command == "zdb":
        print("Available ZanvokDB commands:")
        print("\t 1) 'zdb help' - This displays ZanvokDB Help")
        print("\t 2) 'zdb version' - This displays the ZanvokDB version")
        print("\t 3) 'quit' - Quits the ZanvokDB")
        print("\t 4) 'exit' - Quits the ZanvokDB")
    elif command == "exit":
        break
    elif command == "quit":
        break
    elif command == "cmd":
        cmd = ""
        while cmd != "quit":
            cmd = input("> ")
            if cmd == "quit":
                break
            os.system(cmd)
    else:
        mycursor.execute(command)

        for x in mycursor:
            print(x)