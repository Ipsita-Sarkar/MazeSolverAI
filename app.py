#Execute this file to get the output
from tkinter import *
import logic
def path():
    window = Tk()
    window.title('MazeSolver')
    window.geometry('750x700')
    window.config(bg='#bedcfa')
    res_frame = LabelFrame(window, padx=5, pady=10, borderwidth=0)
    maze_frame = LabelFrame(window, padx=40, pady=10, borderwidth=0)
    but_frame = LabelFrame(window,padx=5,pady=5, borderwidth=5, text ='Menu', font ='bold')
    res_frame.pack()
    maze_frame.pack()
    but_frame.pack()
    res_frame.config(bg='#bedcfa')
    maze_frame.config(bg='#bedcfa')
    but_frame.config(bg='#bedcfa')

    but_list = []
    global src
    src = 0
    global dest
    dest = 1000
    global obs_list
    obs_list = []
    global d_mode
    d_mode = 0
    
    def but_mode(mode):
        global d_mode
        d_mode = mode

    def but_click(but_no):
        global d_mode
        if d_mode == 1:
            but_list[but_no].config(bg='#ffc7c7')
            global src
            src = but_no
            start_button['state'] = 'disabled'
            d_mode = 0
        if d_mode == 2:
            but_list[but_no].config(bg='#08d9d6')
            global dest
            dest = but_no
            des_button['state'] = 'disabled'
            d_mode = 0
        if d_mode == 3:
            but_list[but_no].config(bg='#ff2e63', text='#')
            global obs_list
            obs_list.append(but_no)
       

    start_button = Button(but_frame, text='Select Source',font='bold',command=lambda: but_mode(1))
    start_button.config(bg='#ffc7c7')
    des_button = Button(but_frame, text='Select Destination',font='bold',command=lambda: but_mode(2))
    des_button.config(bg='#08d9d6')
    obs_button = Button(but_frame, text='Select Obstacles',font='bold',command=lambda: but_mode(3))
    obs_button.config(bg='#ff2e63')
    start_button.grid(row=0, column=1, sticky='ew', padx=10, pady=8,ipadx=5, ipady=5)
    des_button.grid(row=0, column=2, sticky='ew', padx=10, pady=8,ipadx=5, ipady=5)
    obs_button.grid(row=0, column=3, sticky='ew', padx=10, pady=8,ipadx=5, ipady=5)
    count = 0
    for i in range(10):
        for j in range(10):
            but_list.append(Button(maze_frame,text=count, padx=10, pady=10, command=lambda x=count: but_click(x)))
            but_list[count].config(bg='#cbf1f5')
            but_list[count].grid(row=i, column=j, sticky='ew')
            count += 1

    def soln():
        parent = logic.logic(src, obs_list, dest)
        for value in parent:
            but_list[value].config(bg='#b088f9')
        but_list[src].config(bg='#ffc7c7')
    soln_button = Button(but_frame, text='Show Path',font='bold', command=soln)
    soln_button.config(bg='#b088f9')
    soln_button.grid(row=0, column=4, padx=10, pady=8,ipadx=5, ipady=5)

    def restart():
        window.destroy()
        path()
    restart_button = Button(res_frame, text='RESTART',font='bold', command=restart)
    restart_button.config(bg='#b83b5e', fg='#f4f9f9')
    restart_button.grid(row=0, column=5, padx=15, pady=8,ipadx=5, ipady=5)
    mainloop()
path()