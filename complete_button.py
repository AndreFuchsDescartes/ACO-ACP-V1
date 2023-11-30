from tkinter import *
from tkinter import ttk
import sv_ttk
import settings

class CompleteButton:
    def __init__(self,root, name,defaultValue) -> None:
        # add frame for padding
        frame_1 = ttk.Frame(master=root)
        frame_1.pack(pady=settings.paddingY, padx=0, fill="both", expand=True)

        value = StringVar()
        value.set(defaultValue)

        ttk.Label(frame_1,text=name)
        ttk.Checkbutton(frame_1,state=defaultValue,variable=value)
        ttk.Label(frame_1,textvariable=value)

        for i, child in enumerate(frame_1.winfo_children()):
            child.grid(row=0,column=i)
            child.grid_configure(padx=20,pady=0)

        
        pass