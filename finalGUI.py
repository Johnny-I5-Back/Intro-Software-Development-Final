import tkinter as tk
from PIL import ImageTk,Image
from tkinter import messagebox

class WrxVisualizer(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Subaru Wrx Visualizer")
        self.geometry("400x600")
        self.iconbitmap('') #add ico icon
        self.createWidgets()

    def createWidgets(self):

        def saveProjectName():
            print("button clicked")

        def confirmCustomizer():
            proceed = messagebox.askyesno('Yes|No', 'Do you want to proceed?')
            if(proceed == True):
                print("openign new window")
            else:
                self.quit

        def addDefaultImg():
            baseImg = Image.open("images/bluebase.png")
            resized = baseImg.resize((300,200), Image.ANTIALIAS)
            newBase = ImageTk.PhotoImage(resized)

            imgBlueBase = tk.Label(self,image=newBase)
            imgBlueBase.image = newBase
            imgBlueBase.place(x=0,y=60)

        def viewSelectedColor():
            choice = colorVar.get()
            if(choice == 1):
                print("you selected blue")

            elif(choice == 2):
                print("you selected white")
            else:
                print("Select a color")

        def addSpoiler():
            includeSpoiler = spoilerVar.get()
            if(includeSpoiler == 1):
                print("you selected spoiler")

            elif(includeSpoiler == 2):
                print("you selected without spoiler")
            else:
                print("Select option")

        # def confirmAllResults():
        # def exitProgram():
        # def showFinalResult():


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
        white = tk.Radiobutton(self,text="White", variable=colorVar,value=2,command=viewSelectedColor)
        white.place(x=0,y=275)


        #spoiler prompt
        spoilerSelectLbl = tk.Label(self,text="Add Spoiler: ")
        spoilerSelectLbl.place(x=0,y=300)

        spoilerVar = tk.IntVar(self)
        withSpoiler = tk.Radiobutton(self,text="With Spoiler", variable=spoilerVar,value=1,command=addSpoiler)
        withSpoiler.place(x=0,y=325)
        
        withoutSpoiler = tk.Radiobutton(self,text="Without Spoiler", variable=spoilerVar,value=2,command=addSpoiler)
        withoutSpoiler.place(x=0,y=350)
        

        #confirmation button
        confirmationBtn = tk.Button(self,text="Confirm Setup", command=confirmCustomizer)
        confirmationBtn.place(x=0,y=400)
        #exit button to close out of program
        exitBtn = tk.Button(self, text="Exit program", command=self.quit)
        exitBtn.place(x=100,y=400)
        


def main():
    WrxVisualizer().mainloop()

if __name__ == "__main__":
    main()
