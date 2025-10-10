from fastapi import FastAPI,HTTPException,Header,Depends
from pydantic import BaseModel
class Student(BaseModel):
    student_id:str
    name:str
    marks:int
API_KEY="mysecretekey"
def verifyKey(x_api_key:str=Header(...)):
     if x_api_key!=API_KEY:
          raise HTTPException (status_code=401,detail="Incorrect Api key!")
     
app=FastAPI()

@app.get("/students/")
def getStudents():
    student_list=[] #initialize the list that is gonna hold data
    with open(r"C:\Users\palla\OneDrive\Documents\Sheridan\PROG51854PFP\fall2025\students.txt","r") as f:
        for line in f:
            line=line.strip()
            if line: #if line exists skip empty lines
                s_id,name,marks=line.split(",")
                student= Student(student_id=s_id,name=name,marks=int(marks))
                student_list.append(student)
    return {"students": student_list}

@app.post("/students/",response_model=Student,status_code=201,dependencies=[Depends(verifyKey)])
def addStudent(student:Student):
    existing_records=[]
    with open(r"C:\Users\palla\OneDrive\Documents\Sheridan\PROG51854PFP\fall2025\students.txt","r") as f:
        for line in f:
            line=line.strip()
            if line: #if line exists skip empty lines
                s_id,_,_=line.split(",")
                existing_records.append(s_id)
        if student.student_id in existing_records:
            raise HTTPException(status_code=400, detail="Student id is present already!")
    with open(r"C:\Users\palla\OneDrive\Documents\Sheridan\PROG51854PFP\fall2025\students.txt","a") as f:
        f.write(f"\n{student.student_id},{student.name},{student.marks}")
    return student

@app.put("/students/{student_id}",response_model=Student)
def updateStudent(student_id:str, updated_student:Student):
    student_found=False
    lines=[]
    #Read all the students
    with open(r"C:\Users\palla\OneDrive\Documents\Sheridan\PROG51854PFP\fall2025\students.txt","r") as f:
        for line in f:
            line=line.strip()
            if not line:
                continue
            parts=line.split(",")
            if len(parts)!=3:
                continue
            s_id,name,marks=parts
            if s_id==student_id:
                #updation
                lines.append(f"{updated_student.student_id},{updated_student.name},{updated_student.marks}\n")
                student_found=True
            else:
                lines.append(line +"\n")
            
    if not student_found:
            raise HTTPException(status_code=404,  detail="Student not found")
    with open(r"C:\Users\palla\OneDrive\Documents\Sheridan\PROG51854PFP\fall2025\students.txt","w") as f:
              f.writelines(lines)
    return updated_student

@app.delete("/students/{student_id}",status_code=204)
def deleteStudent(student_id:str):
     lines=[]
     student_found=False
     #Read all the students 
     with open(r"C:\Users\palla\OneDrive\Documents\Sheridan\PROG51854PFP\fall2025\students.txt","r") as f:
      for line in f:
            line=line.strip()
            if not line:
                continue
            parts=line.split(",")
            if len(parts)!=3:
                continue
            s_id,name,marks=parts
            if s_id==student_id:
                 student_found=True
            else:
                 lines.append(line + "\n") 
     if not student_found:
            raise HTTPException(status_code=404,  detail="Student not found")
     with open(r"C:\Users\palla\OneDrive\Documents\Sheridan\PROG51854PFP\fall2025\students.txt","w") as f:
              f.writelines(lines)
     return None







