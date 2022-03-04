import tkinter as tk
from PIL import Image,ImageTk
from tkinter import PhotoImage, messagebox


class WrxVisualizer(tk.Tk):

    def __init__(self):
        super().__init__()
        self.title("Subaru Wrx Visualizer")
        self.geometry("400x600")
        self.iconbitmap('') #add ico icon
        self.resizable(False,False)
        self.createWidgets()

    def createWidgets(self):

        def saveProjectName():
            print("button clicked")


        #displays the defualt car model
        def addDefaultImg():
            baseImg = Image.open("images/bluebase.png")
            resized = baseImg.resize((300,200), Image.ANTIALIAS)
            newBase = ImageTk.PhotoImage(resized)

            imgBlueBase = tk.Label(self,image=newBase)
            imgBlueBase.image = newBase
            imgBlueBase.place(x=0,y=60)

    

        #handles the users choice of color selection
        def viewSelectedColor():
            choice = colorVar.get()
            if(choice == 1):
                print("you selected blue")

            elif(choice == 2):
                print("you selected black")
            else:
                print("Select a color")

        #handles the users choice of spoiler selection
        def addSpoiler():
            includeSpoiler = spoilerVar.get()
            if(includeSpoiler == 1):
                print("you selected spoiler")

            elif(includeSpoiler == 2):
                print("you selected without spoiler")
            else:
                print("Select option")

    
        #when user clicks confirm a pop up appears, if yes open a new window by running createNewWindow
        def confirmCustomizer(colorVar,spoilerVar):
            color = colorVar.get()
            spoiler = spoilerVar.get()
            
            proceed = messagebox.askyesno('Confirmation Window', 'Do you want to proceed?')
            if(proceed == True):
                finalWindow = tk.Toplevel()
                finalWindow.geometry("400x400")

                #displays blue wrx with spoiler
                if(color == 1 and spoiler == 1):
                    baseImg = Image.open("images/bluespoiler.png")
                    resized = baseImg.resize((300,200), Image.ANTIALIAS)
                    newBase = ImageTk.PhotoImage(resized)

                    imgBlueBase = tk.Label(finalWindow,image=newBase)
                    imgBlueBase.image = newBase
                    imgBlueBase.place(x=0,y=60)

                #displays blue wrx without spoiler
                elif(color == 1 and spoiler == 2):
                    baseImg = Image.open("images/bluebase.png")
                    resized = baseImg.resize((300,200), Image.ANTIALIAS)
                    newBase = ImageTk.PhotoImage(resized)
    
                    imgBlueBase = tk.Label(finalWindow,image=newBase)
                    imgBlueBase.image = newBase
                    imgBlueBase.place(x=0,y=60)

                #displays black wrx with spoiler
                elif(color == 2 and spoiler == 1):
                    baseImg = Image.open("images/blackspoiler.png")
                    resized = baseImg.resize((300,200), Image.ANTIALIAS)
                    newBase = ImageTk.PhotoImage(resized)
    
                    imgBlueBase = tk.Label(finalWindow,image=newBase)
                    imgBlueBase.image = newBase
                    imgBlueBase.place(x=0,y=60)

                #displays black wrx without spoiler
                elif(color == 2 and spoiler == 2):
                    baseImg = Image.open("images/blackbase.png")
                    resized = baseImg.resize((300,200), Image.ANTIALIAS)
                    newBase = ImageTk.PhotoImage(resized)
    
                    imgBlueBase = tk.Label(finalWindow,image=newBase)
                    imgBlueBase.image = newBase
                    imgBlueBase.place(x=0,y=60)

                exitBtn = tk.Button(finalWindow, text="Exit program", command=self.quit)
                exitBtn.place(x=100,y=400)

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
        
        
        #confirmation button
        confirmationBtn = tk.Button(self,text="Confirm Setup", command = lambda: confirmCustomizer(colorVar,spoilerVar))
        confirmationBtn.place(x=0,y=400)
        #exit button to close out of program
        exitBtn = tk.Button(self, text="Exit program", command=self.quit)
        exitBtn.place(x=100,y=400)
        

def main():
    WrxVisualizer().mainloop()

if __name__ == "__main__":
    main()
