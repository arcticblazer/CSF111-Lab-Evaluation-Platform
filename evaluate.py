import os
import subprocess

def checker(model_solution, test_solution):
    # Function accepts stdout results and compares them for equality
    model_solution_list = model_solution.splitlines()
    test_solution_list = test_solution.splitlines()
    
    for idx in range(len(model_solution_list)):
        model_line = model_solution_list[idx]
        test_line = test_solution_list[idx]

        if model_line.rstrip() != test_line.rstrip():
            return 0
    return 1

model_solution_file = "../Lab5/model_solution.c"
test_input_file = "../Lab5/input.txt"
submission_path = "../Lab5/submissions/"

compilation_statement = ["gcc", "-o", "model_solution", model_solution_file]
execution_statement = ["./model_solution"]


# Execute the model solution and store the result in model_solution.stdout
with open(test_input_file, "r") as infile:
    subprocess.run(compilation_statement)
    print("Model Solution Compiled")
    model_solution = subprocess.run(execution_statement, stdin = infile, stdout = subprocess.PIPE)
    print("Model Solution Executed")

print("Model Solution Result : " + str(model_solution.stdout))

# List of all submissions
submissions = os.listdir(submission_path)

marks = dict()

for ans in submissions:
    id_no = ans[:-2]

    #Error Handling
    if ans[-2:] != ".c": # If input does not end with .c
        print(ans + " wrong input format")
        continue
    if len(id_no) != 13:
        print(ans + " wrong id number format")
        continue
    
    test_compilation_statement = ["gcc", submission_path + ans]
    test_execution_statement = ["./a.out"]

    #Execute code of student and store the output of execution in test_solution.stdout
    with open(test_input_file, "r") as infile:
        subprocess.run(test_compilation_statement)        
        test_solution = subprocess.run(test_execution_statement, stdin = infile, stdout = subprocess.PIPE)

    correct = checker(model_solution = model_solution.stdout, test_solution = test_solution.stdout)

    print(id_no + " " + str(correct))

    marks[id_no] = correct

print(marks)
    

