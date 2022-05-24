class school:
  def __init__(self, name, location, numberOfStudents,numberOfTeachers,phase):
    self.name = name
    self.location = location
    self.studentNumber = numberOfStudents
    self.teacherNumber = numberOfTeachers
    self.phase = phase
    self.teachersNeeded = (self.studentNumber/16)
    self.staffList = {}
    self.tutors = []

  def __repr__(self):
    description = "Welcome to {}, located in {}. We are a {} school. Our current student numbers are {}, and our teacher numbers are {}.".format(self.name, self.location, self.phase, self.studentNumber, self.teacherNumber)
    return description

  def teacherCheck(self):
    if self.teacherNumber < self.teachersNeeded:
      needed = round(self.teachersNeeded - self.teacherNumber)
      print("{school} is understaffed, you need to recruit {number} teachers".format(school = self.name, number = needed))
    elif self.teacherNumber == self.teachersNeeded:
      print("Your school has enough teachers, but you might consider adding in some more")
    else:
      remove = round(self.teacherNumber - self.teachersNeeded)
      print("{school} has too many teachers, you need to remove {remove} teachers".format(school = self.name, remove = remove))

  def tutorList(self):
    for tutor in self.tutors:
      print("{tutor} is a tutor at {school}.".format(tutor = tutor, school = self.name))
  
  def teacherList(self):
    print("Currently, {staffAmount} teachers work at {school}. \nThe staff recently employed at {school} are: ".format(staffAmount = self.teacherNumber, school =  self.name))
    #display teacher dictionary in readable format
    for teacher, subject in self.staffList.items():
      print("{staff}, {subject} teacher.".format(staff = teacher, subject = subject))

class teacher:
  #auto assume teacher is male and a tutor, if not, enter false for these values
  def __init__(self, name, subject, yearsTeaching, isTutor = True, isMale = True):
    self.name = name
    self.subject = subject
    self.yearsTeaching = yearsTeaching
    self.isTutor = isTutor
    self.classes = []
    if isMale:
      self.pronoun = "He"
    else:
      self.pronoun = "She"
  
  def __repr__(self):
    intro = "{} is a {} teacher. {} has taught for {} years. ".format(self.name, self.subject, self.pronoun, self.yearsTeaching) 
    if self.isTutor:
      intro += "{} is a tutor".format(self.name)
    else:
      intro += "{} is not a tutor".format(self.name)
    return intro

  def employmentAnniversary(self):
    self.yearsTeaching += 1
    print("{name} is celebrating a work anniversary. {pronoun} has now been teaching for {years}".format(name = self.name, pronoun = self.pronoun, years = self.yearsTeaching))

  def changeTutor(self, school = school):
    if self.isTutor:
      self.isTutor = False
      print("{name} is no longer a tutor".format(name = self.name))
    else:
      self.isTutor = True
      print("{name} is now a tutor".format(name = self.name))

  def employ(self, school):
    school.teacherNumber += 1
    print("{school} just hired a new {subject} teacher. Now {school} has {teacherNumber} teachers".format(subject = self.subject, school = school.name, teacherNumber = school.teacherNumber))
    #Add the staff member to the school teacher list
    school.staffList[self.name] = self.subject
    if self.isTutor:
      school.tutors.append(self.name)

#store all teachers and schools in a list to access them from each others class
schools = []
teachers = []

school1 = school("Eastview", "Kent", 406, 20, "Secondary")
school2 = school("Westside", "Bromley", 1268, 200, "All through school")
schools.extend([school1,school2])

#create teacher and add them to teacher list
teacher1 = teacher("Mr Tony", "History", 4)
teacher2 = teacher("Mr Bebbington", "Computer Science", 3)
teacher3 = teacher("Mrs Anders", "English", 12, isMale = False)
teacher4 = teacher("Mr Bailie", "Maths", 2, isTutor = False)
teacher5 = teacher("Mrs Wills", "Art", 20, isMale = False)
teacher6 = teacher("Mr Button", "Civics", 15, isTutor = False)
teachers.extend([teacher1, teacher2, teacher3, teacher4, teacher5, teacher6])

#display all created instances
for school in schools:
  print(school, "\n")
for teacher in teachers:
  print(teacher, "\n")

#test functions
teacher1.employ(school1)
teacher2.employ(school1)
teacher3.employ(school1)
teacher4.employ(school2)
teacher5.employ(school2)
teacher6.employ(school1)

school1.teacherList()
school2.tutorList()
teacher2.changeTutor()
school1.teacherCheck()
teacher4.employmentAnniversary()

