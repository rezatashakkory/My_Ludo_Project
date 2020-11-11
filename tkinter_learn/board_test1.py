from tkinter import Tk,Button,DISABLED,Frame,X,Y,BOTH,LEFT,RIGHT,Entry,Label
from PIL import ImageTk,Image
from random import randint

# -------------- Window
# window = Tk()
# window.title("Ludo Game")
# window.geometry("600x600")

#--------------- Dice
# dice_text = "DICE"
# dice = 0
# def dice_func(dice_button):
#     global dice
#     dice = randint(1,6)
#     print(dice)
#     dice_text = str(dice)
#     dice_button.grid_forget()
#     dice_button = Button(window, text=dice_text , bg='white', padx=20, pady=20, command=lambda : dice_func(dice_button))
#     dice_button.grid(row=3 , column=3)

# dice_button = Button(window, text=dice_text , bg='white', padx=20, pady=20, command=lambda : dice_func(dice_button))
# dice_button.grid(row=3 , column=3) 

def create_board():    
    #---------------------- Board
    white_board = ImageTk.PhotoImage(Image.open('white-board.jpg'))
    red_board = ImageTk.PhotoImage(Image.open('red-board.jpg'))
    yellow_board = ImageTk.PhotoImage(Image.open('yellow-board.jpg'))
    green_board = ImageTk.PhotoImage(Image.open('green-board.jpg'))
    blue_board = ImageTk.PhotoImage(Image.open('blue-board.jpg'))
    red_home = ImageTk.PhotoImage(Image.open('red-home.jpg'))
    yellow_home = ImageTk.PhotoImage(Image.open('yellow-home.jpg'))
    green_home = ImageTk.PhotoImage(Image.open('green-home.jpg'))
    blue_home = ImageTk.PhotoImage(Image.open('blue-home.jpg'))
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

    l_rb = Label(image=red_home)
    l_rb.grid(row=0 , column=0, columnspan=2, rowspan=2)
    l_rb19 = Label(image=red_board)
    l_rb19.grid(row=2 , column=0)
    l_rb = Label(image=red_board)
    l_rb.grid(row=3 , column=1)

    # counter_red = 0
    # counter_green = 0
    # red1_login = 0
    # red2_login = 0
    # red3_login = 0
    # red4_login = 0
    # red_origin_number = 4
    # red1_loc = -1
    # red2_loc = -1
    # red3_loc = -1
    # red4_loc = -1
    # red_loc_list =[red1_loc,red2_loc,red3_loc,red4_loc]
    # green1_login = 0
    # green2_login = 0
    # green3_login = 0
    # green4_login = 0
    # green_origin_number = 4
    # counter = 0
    # green1_loc = -2
    # green2_loc = -2
    # green3_loc = -2
    # green4_loc = -2
    # green_loc_list =[green1_loc,green2_loc,green3_loc,green4_loc] 

    # def move_click(button_move, color, piece_number=0, loc=0):
    #     global counter_red,counter_green
    #     global red1_login,red2_login,red3_login,red4_login
    #     global red1_loc,red2_loc,red3_loc,red4_loc,red_loc_list
    #     global green1_login,green2_login,green3_login,green4_login
    #     global green1_loc,green2_loc,green3_loc,green4_loc,green_loc_list
    #     # print(button_move,color,piece_number,loc)
    #     if color=='red':
    #         if (loc < 19) and (dice + loc > 18):
    #             button_move.grid_forget()
    #             counter_red += 1
    #             label_win_red = Label(window, text=str(counter_red), bg='red')
    #             label_win_red.grid(row=3, column=1) 
    #             if piece_number==1:
    #                 red1_loc = -5
    #             elif piece_number==2:
    #                 red2_loc = -5
    #             elif piece_number==3:
    #                 red3_loc = -5
    #             elif piece_number==4:
    #                 red4_loc = -5
    #             # print(red_loc_list)
    #             # red_loc_list[(piece_number-1)]= -5                    ??????????????????????????????
    #         else:
    #             if ((loc+dice)%24) not in red_loc_list:
    #                 button_move.grid_forget()
    #                 loc += dice
    #                 loc = (loc%24)
    #                 red_loc_x = location_list[loc-1].grid_info()['row']
    #                 red_loc_y = location_list[loc-1].grid_info()['column']
    #                 button_move = Button(window, padx=2, pady=2, bg='red' , command=lambda : move_click(button_move, 'red', piece_number, loc))
    #                 button_move.grid(row=red_loc_x , column=red_loc_y)
    #                 if piece_number==1:
    #                     red1_loc = loc
    #                 elif piece_number==2:
    #                     red2_loc = loc
    #                 elif piece_number==3:
    #                     red3_loc = loc
    #                 elif piece_number==4:
    #                     red4_loc = loc
    #             else:
    #                 print("RED to RED nmishe ke!")
    #             red_loc_list =[red1_loc,red2_loc,red3_loc,red4_loc] 
    #             print(f'sssssss{red_loc_list}') 
    #             print(f"RED Locationssss : r1={red1_loc} r2={red2_loc} r3={red3_loc} r4={red4_loc}")
        
        
        
    #     if color=='green':
    #         if ((loc <= 23) and (dice + loc > 24))or(loc==0):
    #             button_move.grid_forget()
    #             counter_green += 1
    #             label_win_green = Label(window, text=str(counter_green), bg='green')
    #             label_win_green.grid(row=1, column=3) 
    #             if piece_number==1:
    #                 green1_loc = -6
    #             elif piece_number==2:
    #                 green2_loc = -6
    #             elif piece_number==3:
    #                 green3_loc = -6
    #             elif piece_number==4:
    #                 green4_loc = -6
    #         else:
    #             if ((loc+dice)%24) not in green_loc_list:
    #                 button_move.grid_forget()
    #                 loc += dice
    #                 loc = (loc%24)
    #                 green_loc_x = location_list[loc-1].grid_info()['row']
    #                 green_loc_y = location_list[loc-1].grid_info()['column']
    #                 button_move = Button(window, padx=2, pady=2, bg='green' , command=lambda : move_click(button_move, 'green', piece_number, loc))
    #                 button_move.grid(row=green_loc_x , column=green_loc_y)
    #                 if piece_number==1:
    #                     green1_loc = loc
    #                 elif piece_number==2:
    #                     green2_loc = loc
    #                 elif piece_number==3:
    #                     green3_loc = loc
    #                 elif piece_number==4:
    #                     green4_loc = loc
                    
    #             else:
    #                 print("GREEN to GREEN nmishe ke!")
    #             green_loc_list =[green1_loc,green2_loc,green3_loc,green4_loc] 
    #             print(f'sssssss{green_loc_list}') 
    #             print(f"GREEN Locationssss : r1={green1_loc} r2={green2_loc} r3={green3_loc} r4={green4_loc}")




    # def origin_click(button_origin, color, piece_number):        
    #     global red1_login,red2_login,red3_login,red4_login
    #     global red1_loc,red2_loc,red3_loc,red4_loc
    #     global green1_login,green2_login,green3_login,green4_login
    #     global green1_loc,green2_loc,green3_loc,green4_loc
    #     print("Dice "+str(dice))
    #     if dice==6:
    #         if color=='red':            #Va inke nobatesh
    #             if (piece_number==1)and(red2_loc!=19)and(red3_loc!=19)and(red4_loc!=19):
    #                 button_origin.grid_forget()
    #                 print("Welcome Red 1!!!")
    #                 red1_login = 1
    #                 red1_loc = 19
    #                 button_red1_move = Button(window , padx=2, pady=2, bg='red', command=lambda : move_click(button_red1_move,'red',piece_number=1,loc=red1_loc ))
    #                 button_red1_move.grid(row=2 , column=0)
    #             elif (piece_number==2)and(red1_loc!=19)and(red3_loc!=19)and(red4_loc!=19):
    #                 button_origin.grid_forget()
    #                 print("Welcome Red 2!!!")
    #                 red2_login = 1
    #                 red2_loc = 19
    #                 button_red2_move = Button(window , padx=2, pady=2, bg='red', command=lambda : move_click(button_red2_move,'red',piece_number=2,loc=red2_loc))
    #                 button_red2_move.grid(row=2 , column=0)
    #             elif (piece_number==3)and(red1_loc!=19)and(red2_loc!=19)and(red4_loc!=19):
    #                 button_origin.grid_forget()        
    #                 print("Welcome Red 3!!!")
    #                 red3_login = 1
    #                 red3_loc = 19            
    #                 button_red3_move = Button(window , padx=2, pady=2, bg='red', command=lambda : move_click(button_red3_move,'red',piece_number=3,loc=red3_loc))
    #                 button_red3_move.grid(row=2 , column=0)
    #             elif (piece_number==4)and(red1_loc!=19)and(red2_loc!=19)and(red3_loc!=19):
    #                 button_origin.grid_forget()        
    #                 print("Welcome Red 4!!!")
    #                 red4_login = 1
    #                 red4_loc = 19
    #                 button_red4_move = Button(window , padx=2, pady=2, bg='red', command=lambda : move_click(button_red4_move,'red',piece_number=4,loc=red4_loc))
    #                 button_red4_move.grid(row=2 , column=0)    
        
    #         if color=='green':
    #             if (piece_number==1)and(green2_loc!=1)and(green3_loc!=1)and(green4_loc!=1):
    #                 button_origin.grid_forget()
    #                 print("Welcome Green 1!!!")
    #                 green1_login = 1
    #                 green1_loc = 1
    #                 button_green1_move = Button(window , padx=2, pady=2, bg='green', command=lambda : move_click(button_green1_move,'green',piece_number=1,loc=green1_loc))
    #                 button_green1_move.grid(row=0 , column=4)
    #             elif (piece_number==2)and(green1_loc!=1)and(green3_loc!=1)and(green4_loc!=1):
    #                 button_origin.grid_forget()
    #                 print("Welcome Green 2!!!")
    #                 green2_login = 1
    #                 green2_loc = 1
    #                 button_green2_move = Button(window , padx=2, pady=2, bg='green', command=lambda : move_click(button_green2_move,'green',piece_number=2,loc=green2_loc))
    #                 button_green2_move.grid(row=0 , column=4)
    #             elif (piece_number==3)and(green1_loc!=1)and(green2_loc!=1)and(green4_loc!=1):
    #                 button_origin.grid_forget()        
    #                 print("Welcome Green 3!!!")
    #                 green3_login = 1
    #                 green3_loc = 1            
    #                 button_green3_move = Button(window , padx=2, pady=2, bg='green', command=lambda : move_click(button_green3_move,'green',piece_number=3,loc=green3_loc))
    #                 button_green3_move.grid(row=0 , column=4)
    #             elif (piece_number==4)and(green1_loc!=1)and(green2_loc!=1)and(green3_loc!=1):
    #                 button_origin.grid_forget()        
    #                 print("Welcome Green 4!!!")
    #                 green4_login = 1
    #                 green4_loc = 1
    #                 button_green4_move = Button(window , padx=2, pady=2, bg='green', command=lambda : move_click(button_green4_move,'green',piece_number=4,loc=green4_loc))
    #                 button_green4_move.grid(row=0 , column=4)    
        
    #     else:
    #         print("You Haven't Admission! ")

    # #----------------------- Red Button
    
    # button_red1_origin = Button(window , padx=2, pady=2, bg='red',  command=lambda : origin_click(button_red1_origin,'red',1))      # image=pixelVirtual,, text=str(red_origin_number)
    # button_red1_origin.grid(row=0, column=0)
    # button_red2_origin = Button(window , padx=2, pady=2, bg='red',  command=lambda : origin_click(button_red2_origin,'red',2))  
    # button_red2_origin.grid(row=0, column=1)
    # button_red3_origin = Button(window , padx=2, pady=2, bg='red',  command=lambda : origin_click(button_red3_origin,'red',3))  
    # button_red3_origin.grid(row=1, column=0)
    # button_red4_origin = Button(window , padx=2, pady=2, bg='red',  command=lambda : origin_click(button_red4_origin,'red',4))  
    # button_red4_origin.grid(row=1, column=1)
        
    # #-----------------------------------------------------------------

    l_yb = Label(image=yellow_home)
    l_yb.grid(row=5 , column=5, columnspan=2, rowspan=2)
    l_yb7 = Label(image=yellow_board)
    l_yb7.grid(row=4 , column=6)
    l_yb = Label(image=yellow_board)
    l_yb.grid(row=3 , column=5)
    #--------------------------------------------- Yellow Button




    #------------------------------------------------------



    l_gb = Label(image=green_home)
    l_gb.grid(row=0 , column=5, columnspan=2, rowspan=2)
    l_gb1 = Label(image=green_board)
    l_gb1.grid(row=0 , column=4)
    l_gb = Label(image=green_board)
    l_gb.grid(row=1 , column=3)
    #--------------------------------------------- Green Button
    # button_green1_origin = Button(window , padx=2, pady=2, bg='green',  command=lambda : origin_click(button_green1_origin,'green',1))  
    # button_green1_origin.grid(row=0, column=5)
    # button_green2_origin = Button(window , padx=2, pady=2, bg='green',  command=lambda : origin_click(button_green2_origin,'green',2))  
    # button_green2_origin.grid(row=0, column=6)
    # button_green3_origin = Button(window , padx=2, pady=2, bg='green',  command=lambda : origin_click(button_green3_origin,'green',3))  
    # button_green3_origin.grid(row=1, column=5)
    # button_green4_origin = Button(window , padx=2, pady=2, bg='green',  command=lambda : origin_click(button_green4_origin,'green',4))  
    # button_green4_origin.grid(row=1, column=6)



    #------------------------------------------------------

    l_bb = Label(image=blue_home)
    l_bb.grid(row=5 , column=0, columnspan=2, rowspan=2)
    l_bb13 = Label(image=blue_board)
    l_bb13.grid(row=6 , column=2)
    l_bb = Label(image=blue_board)
    l_bb.grid(row=5 , column=3)



    location_list = [l_gb1,l_wb2,l_wb3,l_wb4,l_wb5,l_wb6,l_yb7,l_wb8,l_wb9,l_wb10,l_wb11,l_wb12,
    l_bb13,l_wb14,l_wb15,l_wb16,l_wb17,l_wb18,l_rb19,l_wb20,l_wb21,l_wb22,l_wb23,l_wb24]



if __name__=='__main__':
    create_board()
# window.mainloop()



# print(location_list[22].grid_info()['row'], location_list[22].grid_info()['column'])
