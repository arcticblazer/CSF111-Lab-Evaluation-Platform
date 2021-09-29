**CS F111 Lab Evaluation Script**

Input :
 - model_solution_file : Path to model solution
 - test_input_file : Input to be tested on
 - submission_path : Path to folder containing solution of students

Working : 
The script evaluates the model solution on provided input file and stores the output.
Then all submissions are iterated over and executed, results of which are compared using checker.
Checker compares results line for line stripping the spaces in the end.

To Do - 
 - Generalize to allow multiple questions
 - More sophisticated solution checker and more error handling?
 - Plagerism Checker?
 - Storing the results in desired format
 - Store the list of students that didn't get answers correct for manual checking