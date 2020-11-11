from tkinter import Tk,Button,DISABLED,Frame,X,Y,BOTH,LEFT,RIGHT,Entry,Label
from PIL import ImageTk,Image
from random import randint

# 3. Place() #the best method over Pack() and Grid()
# def showGrid():
    # print(l_wb22.grid_info()['row'],l_wb22.grid_info()['column'] )

window = Tk()
window.title("Ludo Game")
window.geometry("600x600")


white_board = ImageTk.PhotoImage(Image.open('white-board.jpg'))
red_board = ImageTk.PhotoImage(Image.open('red-board.jpg'))
yellow_board = ImageTk.PhotoImage(Image.open('yellow-board.jpg'))
green_board = ImageTk.PhotoImage(Image.open('green-board.jpg'))
blue_board = ImageTk.PhotoImage(Image.open('blue-board.jpg'))

l_wb2 = Label(image=white_board)
l_wb2.grid(row=1 , column=4)
l_wb3 = Label(image=white_board)
l_wb3.grid(row=2 , column=4)
l_wb4 = Label(image=white_board)
l_wb4.grid(row=2 , column=5)
l_wb5 = Label(image=white_board)
l_wb5.grid(row=2 , column=6)
l_wb6 = Label(image=white_board)
l_wb6.grid(row=3 , column=6)
# l_wb = Label(image=white_board)
# l_wb.grid(row=4 , column=6)
l_wb8 = Label(image=white_board)
l_wb8.grid(row=4 , column=5)
l_wb9 = Label(image=white_board)
l_wb9.grid(row=4 , column=4)
l_wb10 = Label(image=white_board)
l_wb10.grid(row=5 , column=4)
l_wb11 = Label(image=white_board)
l_wb11.grid(row=6 , column=4)
l_wb12 = Label(image=white_board)
l_wb12.grid(row=6 , column=3)
# l_wb = Label(image=white_board)
# l_wb.grid(row=6 , column=2)
l_wb14 = Label(image=white_board)
l_wb14.grid(row=5 , column=2)
l_wb15 = Label(image=white_board)
l_wb15.grid(row=4 , column=2)
l_wb16 = Label(image=white_board)
l_wb16.grid(row=4 , column=1)
l_wb17 = Label(image=white_board)
l_wb17.grid(row=4 , column=0)
l_wb18 = Label(image=white_board)
l_wb18.grid(row=3 , column=0)
# l_wb = Label(image=white_board)
# l_wb.grid(row=2 , column=0)
l_wb20 = Label(image=white_board)
l_wb20.grid(row=2 , column=1)
l_wb21 = Label(image=white_board)
l_wb21.grid(row=2 , column=2)
l_wb22 = Label(image=white_board)
l_wb22.grid(row=1 , column=2)
l_wb23 = Label(image=white_board)
l_wb23.grid(row=0 , column=2)
l_wb24 = Label(image=white_board)
l_wb24.grid(row=0 , column=3)




l_rb = Label(image=red_board)
l_rb.grid(row=0 , column=0)
l_rb19 = Label(image=red_board)
l_rb19.grid(row=2 , column=0)
l_rb = Label(image=red_board)
l_rb.grid(row=3 , column=1)

a_red = 19
red_login = 0
def red_click(button_red1):        
    global a_red,red_login
    dice = randint(1,6)
    print(dice, a_red)
    if (dice==6) and (red_login==0):
        print("Welcome Red!!!")
        red_login = 1
        a_red = 19
        button_red1.grid_forget()
        button_red1 = Button(window , padx=5, pady=5, bg='red',  command=lambda : red_click(button_red1))      # image=pixelVirtual,
        button_red1.grid(row=2, column=0)
        
        
    if red_login==1 :
        red_loc_x = location_list[(a_red-1)%24].grid_info()['row']
        red_loc_y = location_list[(a_red-1)%24].grid_info()['column']
        button_red1 = Button(window, padx=5, pady=5, bg='red' , command=lambda : red_click(button_red1))
        button_red1.grid(row=red_loc_x , column=red_loc_y)






button_red1 = Button(window, text='4' , padx=5, pady=5, bg='red',  command=lambda : red_click(button_red1))      # image=pixelVirtual,
button_red1.grid(row=0, column=0)











l_yb = Label(image=yellow_board)
l_yb.grid(row=6 , column=6)
l_yb7 = Label(image=yellow_board)
l_yb7.grid(row=4 , column=6)
l_yb = Label(image=yellow_board)
l_yb.grid(row=3 , column=5)

l_gb = Label(image=green_board)
l_gb.grid(row=0 , column=6)
l_gb1 = Label(image=green_board)
l_gb1.grid(row=0 , column=4)
l_gb = Label(image=green_board)
l_gb.grid(row=1 , column=3)

l_bb = Label(image=blue_board)
l_bb.grid(row=6 , column=0)
l_bb13 = Label(image=blue_board)
l_bb13.grid(row=6 , column=2)
l_bb = Label(image=blue_board)
l_bb.grid(row=5 , column=3)

location_list = [l_gb1,l_wb2,l_wb3,l_wb4,l_wb5,l_wb6,l_yb7,l_wb8,l_wb9,l_wb10,l_wb11,l_wb12,
l_bb13,l_wb14,l_wb15,l_wb16,l_wb17,l_wb18,l_rb19,l_wb20,l_wb21,l_wb22,l_wb23,l_wb24]

# print(location_list[22].grid_info()['row'], location_list[22].grid_info()['column'])

window.mainloop()

# import tkinter as tk
# import random

# # --- function ---

# def move():
#     #b.place_forget() # it seems I don't have to use it 
#                       # to hide/remove before I put in new place
    
#     new_x = random.randint(0, 100)
#     new_y = random.randint(0, 150)
#     b.place(x=new_x, y=new_y)

#     # b['height'] = random.randint(1, 10)

# # --- main ---

# root = tk.Tk()

# b = tk.Button(root, text='Move it', command=move)
# b.place(x=0, y=0)

# root.mainloop()