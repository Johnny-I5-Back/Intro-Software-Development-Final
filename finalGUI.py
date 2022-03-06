import tkinter as tk
from tkinter import END, PhotoImage, messagebox


class WrxVisualizer(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Subaru Wrx Visualizer")
        self.geometry("400x600")
        self.resizable(False,False)
        self.createWidgets()

    def createWidgets(self):

        def saveProjectName():
            print("button clicked")


        #displays the defualt car model
        def addDefaultImg():
            img_label = tk.Label(self,width=300,height=200)
            img_label.image = PhotoImage(file="images/bluebase.png")
            img_label['image'] = img_label.image
            img_label.place(x=0,y=60)

        #handles the users choice of color selection
        def viewSelectedColor():
            choice = colorVar.get()
            displayInfo.delete('1.0',END)

            if(choice == 1):
                displayInfo.insert('1.0', 'You Selected Blue')
            elif(choice == 2):
                displayInfo.insert('1.0', 'You Selected Black')
            else:
                displayInfo.insert('1.0', 'Select A Color')

        #handles the users choice of spoiler selection
        def addSpoiler():
            includeSpoiler = spoilerVar.get()
            displayInfo.delete('1.0',END)

            if(includeSpoiler == 1):
                displayInfo.insert('1.0', 'You Selected A Spoiler')

            elif(includeSpoiler == 2):
                displayInfo.insert('1.0', 'You Selected No Spoiler')

            else:
                displayInfo.insert('1.0', 'Select An Option')

    
        #when user clicks confirm a pop up appears, if yes open a new window by running createNewWindow
        def confirmCustomizer(colorVar,spoilerVar):
            color = colorVar.get()
            spoiler = spoilerVar.get()
            
            proceed = messagebox.askyesno('Confirmation Window', 'Do you want to proceed?')
            if(proceed == True):
                finalWindow = tk.Toplevel()
                finalWindow.geometry("400x400")
                finalinfo = tk.Text(finalWindow)
                finalinfo.place(x=0,y=20)

                #displays blue wrx with spoiler
                if(color == 1 and spoiler == 1):                    
                    img_label = tk.Label(finalWindow,width=300,height=200)
                    img_label.image = PhotoImage(file="images/bluespoiler.png")
                    img_label['image'] = img_label.image
                    img_label.place(x=0,y=60)

                #displays blue wrx without spoiler
                elif(color == 1 and spoiler == 2):
                    img_label = tk.Label(finalWindow,width=300,height=200)
                    img_label.image = PhotoImage(file="images/bluebase.png")
                    img_label['image'] = img_label.image
                    img_label.place(x=0,y=60)

                #displays black wrx with spoiler
                elif(color == 2 and spoiler == 1):
                    img_label = tk.Label(finalWindow,width=300,height=200)
                    img_label.image = PhotoImage(file="images/blackspoiler.png")
                    img_label['image'] = img_label.image
                    img_label.place(x=0,y=60)

                #displays black wrx without spoiler
                elif(color == 2 and spoiler == 2):                   
                    img_label = tk.Label(finalWindow,width=300,height=200)
                    img_label.image = PhotoImage(file="images/blackbase.png")
                    img_label['image'] = img_label.image
                    img_label.place(x=0,y=60)

                else:
                    img_label = tk.Label(finalWindow,width=300,height=200)
                    img_label.image = PhotoImage(file="images/bluebase.png")
                    img_label['image'] = img_label.image
                    img_label.place(x=0,y=60)


                exitBtn = tk.Button(finalWindow, text="Exit program",bg="red", fg="white", padx=5,pady=5, command=self.quit)
                exitBtn.place(x=0,y=250)

                finalWindow.mainloop()
            else:
                self.quit

    
        promptLbl = tk.Label(self,text="To begin, choose a name for this project.")
        promptLbl.place(x=0,y=0)

        projectName = tk.Entry(self)
        projectName.place(x=0,y=20)

        saveProjectBtn = tk.Button(self, text="Save",command=saveProjectName)
        saveProjectBtn.place(x=0,y=40)

        #add the default image
        addDefaultImg()

        #color prompt
        colorlbl = tk.Label(self, text="Choose the base color: ")
        colorlbl.place(x=0,y=225)

        colorVar = tk.IntVar(self)
        blue = tk.Radiobutton(self,text="Blue", variable=colorVar,value=1,command=viewSelectedColor)
        blue.place(x=0,y=250)
        black = tk.Radiobutton(self,text="Black", variable=colorVar,value=2,command=viewSelectedColor)
        black.place(x=0,y=275)


        #spoiler prompt
        spoilerSelectLbl = tk.Label(self,text="Add Spoiler: ")
        spoilerSelectLbl.place(x=0,y=300)

        spoilerVar = tk.IntVar(self)
        withSpoiler = tk.Radiobutton(self,text="With Spoiler", variable=spoilerVar,value=1,command=addSpoiler)
        withSpoiler.place(x=0,y=325)
        
        withoutSpoiler = tk.Radiobutton(self,text="Without Spoiler", variable=spoilerVar,value=2,command=addSpoiler)
        withoutSpoiler.place(x=0,y=350)

        #selection
        displayInfo = tk.Text(self,height=2)
        displayInfo.place(x=0,y=400)
        
        
        #confirmation button
        confirmationBtn = tk.Button(self,text="Confirm Setup", bg="green", fg="white", padx=5, pady=5, command = lambda: confirmCustomizer(colorVar,spoilerVar))
        confirmationBtn.place(x=0,y=450)

        #exit button to close out of program
        exitBtn = tk.Button(self, text="Exit program", bg="red",fg="white", padx=5,pady=5, command=self.quit)
        exitBtn.place(x=100,y=450)
        

def main():
    WrxVisualizer().mainloop()

if __name__ == "__main__":
    main()
