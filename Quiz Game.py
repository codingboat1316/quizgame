import tkinter as tk
from tkinter import StringVar
from tkinter import messagebox 


root = tk.Tk()
root.geometry('800x500')
root.title("Quiz game created by Zeal soni")


questions = ["1.Which was the first country to host the Asian Games ?","2.Free throw is associated with ?",
             "3.Humayun was born in the year ?","4.Who invented the 3D printer?",
             "5.What is the maximum number of Members in Loc Sabha ?"]
options = [['China','Japan','India','Korea','India'],['Volleyball','Basketball','Hockey','Football','Basketball'],
           ['1408','1708','1608','1508','1508'],['Chuck Hull','Christiaan Huygens','Nick Holonyak','Elias Howe','Chuck Hull'],
           ['532','552','542','512','552']]


frame = tk.Frame(root, padx=10, pady=10,bg='#fff')
questionlabel = tk.Label(frame,height=5, width=50,bg='purple',fg="#fff", 
                          font=('Arial', 20),wraplength=500)
questionlabel.grid(row=0, column=0)


val1 = StringVar(frame)
val2 = StringVar(frame)
val3 = StringVar(frame)
val4 = StringVar(frame)

option1 = tk.Radiobutton(frame, bg="#fff",fg='orange', variable=val1, font=('Arial', 20),
                         command = lambda : Answer(option1))
option1.grid(sticky= 'W', row=1, column=0)

option2 = tk.Radiobutton(frame, bg="#fff", variable=val2, font=('Arial', 20), 
                         command = lambda : Answer(option2))
option2.grid(sticky= 'W', row=2, column=0)

option3 = tk.Radiobutton(frame, bg="#fff", fg='orange',variable=val3, font=('Arial', 20), 
                         command = lambda : Answer(option3))
option3.grid(sticky= 'W', row=3, column=0)

option4 = tk.Radiobutton(frame, bg="#fff", variable=val4, font=('Arial', 20), 
                         command = lambda : Answer(option4))
option4.grid(sticky= 'W', row=4, column=0)


buttonnext = tk.Button(frame, text='Next',bg='purple', font=('Arial', 20), 
                        command = lambda : NextQuestion())
buttonnext.grid(row=6, column=0)

frame.pack(fill="both", expand="true")

index = 0
correct = 0


def disableButtons(state):
    option1['state'] = state
    option2['state'] = state
    option3['state'] = state
    option4['state'] = state



def Answer(radio):
    global correct, index
    
    
    if radio['text'] == options[index][4]:
        correct +=1
        print("Correct!")
        messagebox.showinfo("","correct!")

    else:
        print("Incorrect!")
        messagebox.showinfo("","Incorrect!")


    index +=1
    disableButtons('disable')
    

def NextQuestion():
    global index, correct

    if buttonnext['text'] == 'Play again':
        correct = 0
        index = 0
        questionlabel['bg'] = 'purple'
        buttonnext['text'] = 'Next'
        

    if index == len(options):
       questionlabel['text'] = str(correct) + " / " + str(len(options))
       buttonnext['text'] = 'Play again'
       if correct >= len(options)/2:
           questionlabel['bg'] = 'black'
           messagebox.showinfo("","good job!! Congratulation!! you win the game.")

       else:
            questionlabel['bg'] = 'red'
            messagebox.showinfo("","oops!! you loss the game.")
            



    else:
        questionlabel['text'] = questions[index]
        
        disableButtons('normal')
        option = options[index]
        option1['text'] = option [0]
        option2['text'] = option [1]
        option3['text'] = option [2]
        option4['text'] = option [3]
        val1.set(option [0])
        val2.set(option [1])
        val3.set(option [2])
        val4.set(option [3])

        if index == len(options) - 1:
            buttonnext['text'] = 'Check the Results'


NextQuestion()

root.mainloop()
