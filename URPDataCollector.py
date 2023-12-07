import string
import tkinter as tk
from PIL import ImageTk, Image
import os
from datetime import date
import time
from random import sample


class ExperimentalTrial():
    def __init__(self):
        self.participantID = ""

        today = date.today()
        self.date = today

        self.condition = ""


class MatrixTask():
    def __init__(self):
        self.responses = []


class ArithmeticTask():
    def __init__(self):
        self.responses = []


class LinguisticTask():
    def __init__(self):
        self.responses = []


class EndOfExperimentSurvey():
    def __init__(self):
        self.responses = []


class BinaryChoice():
    def __init__(self):
        self.response = ""
        self.start = 0
        self.end = 0
        self.time = 0


# Matrix Reasoning key [B,A,D,A,C,B,D,A]
# Arithmetic Reasoning key [b,d,a,a,b,d,c,d]
# Linguistic Reasoning key [c,a,d,d,c,a,a,d]

class ImageSlideshow(tk.Tk):
    def __init__(self, image_folder):
        super().__init__()

        self.slideNumber = 1

        # Set the window title
        self.title(" ")

        # Get the list of image file names in the folder
        self.image_folder = image_folder
        self.image_files = os.listdir(image_folder)

        # Create an empty list to store the ImageTk objects
        self.image_tk = []

        # Load the images and create ImageTk objects
        for file in self.image_files:
            image = Image.open(os.path.join(image_folder, file))
            image = image.resize((800, 600))
            self.image_tk.append(ImageTk.PhotoImage(image))

        # Create a label to display the images
        self.image_label = tk.Label(self, image=self.image_tk[0])
        self.image_label.pack()

        # Set a timer to change the image every 2 seconds
        # self.change_image causes it to go to the next slide
        self.current_image = 0

        self.bind("a", self.next_imageA)
        self.bind("b", self.next_imageB)
        self.bind("c", self.next_imageC)
        self.bind("d", self.next_imageD)
        self.bind("<space>", self.next_imageSpace)
        self.bind("0", self.next_zero)
        self.bind("1", self.next_one)
        self.bind("2", self.next_two)
        self.bind("3", self.next_three)


    def next_imageA(self, event):
        if self.slideNumber in [6,7,8,9,10,11,12,13,19,20,21,22,23,24,25,26,32,33,34,35,36,37,38,39,44,48,49]:
            if self.slideNumber in [6,7,8,9,10,11,12,13]:
                matrix.responses.append("a")
            elif self.slideNumber in [19,20,21,22,23,24,25,26]:
                arithmetic.responses.append("a")
            elif self.slideNumber in [32,33,34,35,36,37,38,39]:
                linguistic.responses.append("a")
            elif self.slideNumber == 44:
                BC.response = "A"
                BC.end = time.time()
                BC.time = round(BC.end-BC.start, 3)
            elif self.slideNumber == 48:
                EOE.responses.append("a")
            elif self.slideNumber == 49:
                EOE.responses.append("a")
            self.current_image += 1
            self.slideNumber += 1
            self.image_label.configure(image=self.image_tk[self.current_image])


    def next_imageB(self, event):
        if self.slideNumber in [6,7,8,9,10,11,12,13,19,20,21,22,23,24,25,26,32,33,34,35,36,37,38,39,44,48,49]:
            if self.slideNumber in [6,7,8,9,10,11,12,13]:
                matrix.responses.append("b")
            elif self.slideNumber in [19,20,21,22,23,24,25,26]:
                arithmetic.responses.append("b")
            elif self.slideNumber in [32,33,34,35,36,37,38,39]:
                linguistic.responses.append("b")
            elif self.slideNumber == 44:
                BC.response = "B"
                BC.end = time.time()
                BC.time = round(BC.end-BC.start, 3)
            elif self.slideNumber == 48:
                EOE.responses.append("b")
            elif self.slideNumber == 49:
                EOE.responses.append("b")
            self.current_image += 1
            self.slideNumber += 1
            self.image_label.configure(image=self.image_tk[self.current_image])



    def next_imageC(self, event):
        if self.slideNumber in [6,7,8,9,10,11,12,13,19,20,21,22,23,24,25,26,32,33,34,35,36,37,38,39,48,49]:
            if self.slideNumber in [6,7,8,9,10,11,12,13]:
                matrix.responses.append("c")
            elif self.slideNumber in [19,20,21,22,23,24,25,26]:
                arithmetic.responses.append("c")
            elif self.slideNumber in [32,33,34,35,36,37,38,39]:
                linguistic.responses.append("c")
            elif self.slideNumber == 48:
                EOE.responses.append("c")
            elif self.slideNumber == 49:
                EOE.responses.append("c")
            self.current_image += 1
            self.slideNumber += 1
            self.image_label.configure(image=self.image_tk[self.current_image])



    def next_imageD(self, event):
        if self.slideNumber in [6,7,8,9,10,11,12,13,19,20,21,22,23,24,25,26,32,33,34,35,36,37,38,39,49]:
            if self.slideNumber in [6,7,8,9,10,11,12,13]:
                matrix.responses.append("d")
            elif self.slideNumber in [19,20,21,22,23,24,25,26]:
                arithmetic.responses.append("d")
            elif self.slideNumber in [32,33,34,35,36,37,38,39]:
                linguistic.responses.append("d")
            elif self.slideNumber == 49:
                EOE.responses.append("d")
            self.current_image += 1
            self.slideNumber += 1
            self.image_label.configure(image=self.image_tk[self.current_image])


    def next_imageSpace(self, event):
        if self.slideNumber in [1, 2, 3, 4, 5, 14, 15, 16, 17, 18, 27, 28, 29, 30, 31, 42, 43]:
            if self.slideNumber == 42:
                BC.start = time.time()
            self.current_image += 1
            self.slideNumber += 1
        # This achieves the loading animation
        elif self.slideNumber == 40:
            self.current_image += 1
            self.slideNumber += 1
            self.image_label.configure(image=self.image_tk[self.current_image])
            time.sleep(3)
            self.current_image += 1
            self.slideNumber += 1
        self.image_label.configure(image=self.image_tk[self.current_image])

    def next_zero(self, event):
        if self.slideNumber in [45,46,47]:
            EOE.responses.append("0")
            self.current_image += 1
            self.slideNumber += 1
            self.image_label.configure(image=self.image_tk[self.current_image])

    def next_one(self, event):
        if self.slideNumber in [45,46,47]:
            EOE.responses.append("1")
            self.current_image += 1
            self.slideNumber += 1
            self.image_label.configure(image=self.image_tk[self.current_image])

    def next_two(self, event):
        if self.slideNumber in [45,46,47]:
            EOE.responses.append("2")
            self.current_image += 1
            self.slideNumber += 1
            self.image_label.configure(image=self.image_tk[self.current_image])

    def next_three(self, event):
        if self.slideNumber in [45,46,47]:
            EOE.responses.append("3")
            self.current_image += 1
            self.slideNumber += 1
            self.image_label.configure(image=self.image_tk[self.current_image])


ET = ExperimentalTrial()
matrix = MatrixTask()
arithmetic = ArithmeticTask()
linguistic = LinguisticTask()
BC = BinaryChoice()
EOE = EndOfExperimentSurvey()

# reads in the condition.txt document which determines the condition the participant experinences
with open("Condition.txt", "a+") as cond:
    condList = cond.read()
    conditionCodes = condList.split(",")

    # grabs the last number in the list and uses it to determine the condition
    # 1 = control
    # 0 = experimental
    currentCondition = conditionCodes[len(conditionCodes)-1]

    if currentCondition == "1":
        ET.condition = "Control"
        slideshow = ImageSlideshow("ControlCondition")
    else:
        ET.condition = "Experimental"
        slideshow = ImageSlideshow("ExperimentalCondition")

    # Edits the condition.txt file and puts back every number in order except the one used
        # Removes all text from the document
    cond.truncate(0)
        # Puts back all the values except the last one
    for i in range(len(conditionCodes)-1):
        if i != len(conditionCodes)-2:
            cond.write(conditionCodes[i] + ",")
        else:
            cond.write(conditionCodes[i])

cond.close()

# Start the slideshow
slideshow.mainloop()

# An ID is a 5 character combination of any alphanumeric characters.
IDCharPool = list(string.ascii_lowercase + string.ascii_uppercase + string.digits)
ET.participantID = sample(IDCharPool, 5)
IDstring = ""
for item in ET.participantID:
    IDstring += str(item)
ET.participantID = IDstring

# gets a list of all taken ID's
ID = open("participantIDs.txt", "r+")
IDList = ID.read()
individualIDs = IDList.split(",")

# generates a new ID until an available one is found
while ET.participantID in individualIDs:
    ET.participantID = sample(IDCharPool)
    IDstring = ""
    for item in ET.participantID:
        IDstring += str(item)
    ET.participantID = IDstring

# writes the newly taken ID to the participant ID file
ID.write(str(ET.participantID)+",")
ID.close()

# Constructs the string to be written into the text file (The data to be logged)
toReturn = "[ID: "+str(ET.participantID)+", Date: "+str(ET.date)+", Condition: "+ET.condition+", Binary Choice: "+str(BC.response)
toReturn += ", BC Response Time: "+str(BC.time)+", Distress Level: "+str(EOE.responses[0])+", Clarity Of Instructions: "
toReturn += str(EOE.responses[1])+", Clarity Of Choice Matrix: "+str(EOE.responses[2])+", Sex: "+str(EOE.responses[3])
toReturn += ", Age: "+str(EOE.responses[4])+", Matrix Reasoning Responses: "+str(matrix.responses)
toReturn += ", Arithmetic Reasoning Responses: "+str(arithmetic.responses)+", Linguistic Reasoning Responses: "
toReturn += str(linguistic.responses)+"]"

# Writes the data to the file
f = open("data.txt", "a")
f.write(toReturn)
f.close()


