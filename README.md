# Template assignment (Python)

This is a template to create Python autograded assignments for [github classroom](https://classroom.github.com/classrooms)

## Instructions for students

- Implement your solutions in `assignment.py`
- The tests in `test_assignment.py` can be inspected but do not modify them
- We expected you to follow the [ACM Code of Ethics](https://www.acm.org/code-of-ethics)


## Instructions for teachers 

(Delete this section of the README in the final assignment)

### Setting up your classroom 

- [Create a github organization](https://docs.github.com/en/organizations/collaborating-with-groups-in-organizations/creating-a-new-organization-from-scratch) to host your assignments
- [Create your classroom using the recently created organization](https://docs.github.com/en/education/manage-coursework-with-github-classroom/teach-with-github-classroom/manage-classrooms)
- (Optionally) Upload your roster of students


### Setting up the starter-code for your assignment 

- Create the **private** repository for your assignments [using this repository as template](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template)
- Modify `assignment.py` and `test_assignment.py` to suit your needs
- Modify `requirements.txt` with the libraries needed to evaluate the codes
- Modify `.github/classroom/autograding.json` to set your tests
- (Optionally) If you added new files that need to be tested then modify `.github/workflow/classroom.yaml` accordingly (see comment on line 6)


### Creating the assignment in github classroom (everytime you )

- Select your classroom in the [github classroom interface](https://classroom.github.com/classrooms)
- Click the green "New assignment" button. Set a title and deadline. Choose an individual or group/team assignment
- Leave the repository as private: that way only you and the group/team members can see the student's repository
- Add your repository (starter code) as template repository. 
- Do not add autograding tests with the interface (they are already on your repo)
- A link to distribute the assignment will be created. When students accept the assignment through the link a repository will be created in the organization