
class ProjectBox:
    def __init__(self,name,description,deadline):
        self.name=name
        self.description=description
        self.deadline=deadline
        self.status='Ongoing'

    def display_info(self):
        return f'Project: {self.name}\nDescription: {self.description}\nDeadline: {self.deadline}\nStatus: {self.status}\n'    
    
# user1=ProjectBox("test","this is a test",2024)
# print(user1.display_info())

