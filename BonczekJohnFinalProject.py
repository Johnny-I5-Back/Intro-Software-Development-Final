import tkinter as tk
from tkinter import END, PhotoImage, messagebox


class WrxVisualizer(tk.Tk):

    #tkinter settings
    def __init__(self):
        super().__init__()
        self.title("Subaru Wrx Visualizer") #window title
        self.geometry("400x600") #window size
        self.configure(bg="#111111")
        self.resizable(False,False) #makes it where you cant change window dimensions
        self.createWidgets() # calls the create widgets function

    def createWidgets(self):
        """creates the widgets for the gui"""

        #displays the defualt car model
        def addDefaultImg():
            """Adds a label for the image and adds in the default model for the program"""
            img_label = tk.Label(self,width=300,height=200,bg="#111111")
            img_label.image = PhotoImage(file="images/bluebase.png")
            img_label['image'] = img_label.image
            img_label.place(x=0,y=60)

        #handles the users choice of color selection
        def viewSelectedColor():
            """displays what color the user has selected"""
            choice = colorVar.get() #gets the users radio selection choice
            displayInfo.delete('1.0',END) #deletes any text in the text box

            if(choice == 1):
                displayInfo.insert('1.0', 'You Selected Blue')
            elif(choice == 2):
                displayInfo.insert('1.0', 'You Selected Black')
            else:
                displayInfo.insert('1.0', 'Select A Color')

        #handles the users choice of spoiler selection
        def addSpoiler():
            """displays the spoiler choice the user has made"""
            includeSpoiler = spoilerVar.get()
            displayInfo.delete('1.0',END) #deletes any text currently in the text field

            if(includeSpoiler == 1):
                displayInfo.insert('1.0', 'You Selected A Spoiler')

            elif(includeSpoiler == 2):
                displayInfo.insert('1.0', 'You Selected No Spoiler')

            else:
                displayInfo.insert('1.0', 'Select An Option')

        def saveProjectName():
            """returns the name the user enters for the project"""
            return projectName.get()

        #when user clicks confirm a pop up appears, if yes a new window is created displaying the final project information
        def confirmCustomizer(colorVar,spoilerVar):
            """takes the user selection from the radio buttons and returns the final image based off of the results"""
            color = colorVar.get()
            spoiler = spoilerVar.get()
            
            #pop up that asks yes or no
            proceed = messagebox.askyesno('Confirmation Window', 'Do you want to proceed?')
            #if pop up is yes/true create a new window
            if(proceed == True):
                finalWindow = tk.Toplevel() #creates new tkinter window 
                finalWindow.geometry("400x400") #new window size
                finalWindow.configure(bg="#111111")
                finalWindow.resizable(False,False) #not resizeable

                displayProjectName = tk.Text(finalWindow) #places text filed in window
                displayProjectName.insert('1.0', saveProjectName()) #inserts the name for the project in the text field
                displayProjectName.place(x=0,y=0)

                finalinfo = tk.Text(finalWindow,bg="#111111",fg="white")
                finalinfo.place(x=0,y=20)

                #if color is equal to 1 returns blue if 2 returns black
                #if spoiler is equal to 1 returns with spoiler if 2 returns without spoiler
                #displays blue wrx with spoiler image and text
                if(color == 1 and spoiler == 1):
                    finalinfo.insert('1.0', 'You selected blue with a spoiler.')                    
                    img_label = tk.Label(finalWindow,bg="#111111",width=300,height=200)
                    img_label.image = PhotoImage(file="images/bluespoiler.png")
                    img_label['image'] = img_label.image
                    img_label.place(x=0,y=40)

                #displays blue wrx without spoiler image and text
                elif(color == 1 and spoiler == 2):
                    finalinfo.insert('1.0', 'You selected blue without a spoiler.')                    
                    img_label = tk.Label(finalWindow,bg="#111111",width=300,height=200)
                    img_label.image = PhotoImage(file="images/bluebase.png")
                    img_label['image'] = img_label.image
                    img_label.place(x=0,y=40)

                #displays black wrx with spoiler image and text
                elif(color == 2 and spoiler == 1):
                    finalinfo.insert('1.0', 'You selected black with a spoiler.')                    
                    img_label = tk.Label(finalWindow,bg="#111111",width=300,height=200)
                    img_label.image = PhotoImage(file="images/blackspoiler.png")
                    img_label['image'] = img_label.image
                    img_label.place(x=0,y=40)

                #displays black wrx without spoiler image and text
                elif(color == 2 and spoiler == 2):  
                    finalinfo.insert('1.0', 'You selected black without a spoiler.')                                     
                    img_label = tk.Label(finalWindow,bg="#111111",width=300,height=200)
                    img_label.image = PhotoImage(file="images/blackbase.png")
                    img_label['image'] = img_label.image
                    img_label.place(x=0,y=40)
                
                #if a user does not submit any options it returns the base model of the car image and text
                else:
                    finalinfo.insert('1.0', 'You selected no options, showing base model.')                    
                    img_label = tk.Label(finalWindow,bg="#111111",width=300,height=200)
                    img_label.image = PhotoImage(file="images/bluebase.png")
                    img_label['image'] = img_label.image
                    img_label.place(x=0,y=40)

                #creates and styles exit button
                exitBtn = tk.Button(finalWindow, text="Exit program",bg="red", fg="white", padx=5,pady=5, command=self.quit)
                exitBtn.place(x=0,y=250)

                #creates a button to return back to main screen by closing(destroying) this window
                returnBackBtn = tk.Button(finalWindow, text="Go Back", bg="green", fg="white",padx=5,pady=5,command=lambda: finalWindow.destroy())
                returnBackBtn.place(x=100,y=250)

                finalWindow.mainloop()

            #if user clicks no on the pop up, the pop up closes and returns to the main gui window
            else:
                self.quit

        

        #ask user to enter name of project
        promptLbl = tk.Label(self,bg="#111111",fg="white",text="Choose a name for the project press button to 'save'.")
        promptLbl.place(x=0,y=0)

        #input field for project name
        projectName = tk.Entry(self,bg="#222222",fg="white")
        projectName.place(x=0,y=20)
        
        #save project name button calls the function that stores the name
        saveProjectBtn = tk.Button(self,bg="green", fg="white", text="Click to Save Name",command=saveProjectName)
        saveProjectBtn.place(x=0,y=40)

        #add the default image called above
        addDefaultImg()

        #color prompt
        colorlbl = tk.Label(self,bg="#111111",fg="white", text="Choose the base color: ")
        colorlbl.place(x=0,y=225)

        #creates a radio button for the color choices
        colorVar = tk.IntVar(self) #creates a variable called colorVar that is an integer value for the radio select buttons
        blue = tk.Radiobutton(self,text="Blue", variable=colorVar,value=1,bg="white",command=viewSelectedColor)
        blue.place(x=0,y=250)
        black = tk.Radiobutton(self,text="Black", variable=colorVar,value=2,bg="white",command=viewSelectedColor)
        black.place(x=0,y=275)


        #spoiler prompt
        spoilerSelectLbl = tk.Label(self,bg="#111111",fg="white",text="Add Spoiler: ")
        spoilerSelectLbl.place(x=0,y=300)

        #creates the radio buttons for the spoiler choice
        spoilerVar = tk.IntVar(self) #creates a variable called spoilerVar that is an integer value
        withSpoiler = tk.Radiobutton(self,text="With Spoiler", variable=spoilerVar,value=1,bg="white",command=addSpoiler)
        withSpoiler.place(x=0,y=325)
        withoutSpoiler = tk.Radiobutton(self,text="Without Spoiler", variable=spoilerVar,value=2,bg="white",command=addSpoiler)
        withoutSpoiler.place(x=0,y=350)

        #displays the information when a user selects an option from the radio buttons
        displayInfo = tk.Text(self,height=2,bg="#222222",fg="white")
        displayInfo.place(x=0,y=400)
        
        
        #confirmation button calls the function that creates a new window and displays final image
        confirmationBtn = tk.Button(self,text="Confirm Setup", bg="green", fg="white", padx=5, pady=5, command = lambda: confirmCustomizer(colorVar,spoilerVar))
        confirmationBtn.place(x=0,y=450)

        #exit button to close out of program
        exitBtn = tk.Button(self, text="Exit program", bg="red",fg="white", padx=5,pady=5, command=self.quit)
        exitBtn.place(x=100,y=450)
        
def main():
    WrxVisualizer().mainloop()

#calls main
if __name__ == "__main__":
    main()
