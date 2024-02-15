from project_box import ProjectBox
import sqlite3

conn=sqlite3.connect("project_box.db")
cursor =conn.cursor()

cursor.execute("""
       CREATE TABLE IF NOT EXISTS ProjectsBox (
               id INTIGER PRYMARY KEY,
               name TEXT NOT NULL,
               description TEXT,
               deadline TEXT,
               status TEXT NOT NULL
       )
""")
conn.commit()

def add_project():
    name=input("Project name: ")
    description=input("Enter the project description: ")
    deadline=input("Enter the deadline: ")
    
    cursor.execute("INSERT INTO ProjectsBox (name, description, deadline, status) VALUES (?, ?, ?, ?)",
                   (name,description,deadline,"Ongoing"))
    conn.commit()
    
    return f'Project successfully added!\n'
    
def list_projects():
    cursor.execute("SELECT * FROM ProjectsBox")
    projects=cursor.fetchall()

    for project in projects:
        print(f"Project {project[0]}")
        print(f"Name {project[1]}")
        print(f"Description {project[2]}")
        print(f"Deadline {project[3]}")
        print(f"status {project[4]}")
        print()
        
def main():
    while True:
        print("1. Add project")
        print("2. Projects list")
        print("3. Exit")
        choice= input("Pick an option: ")
        print()

        if choice == "1":
            add_project()
        elif choice =="2":
            list_projects()
        elif choice =="3":
            break
        else:
            return("Invalid option. Try again.\n")            
    


if __name__=="__main__":
    main()