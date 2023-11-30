from tkinter import *
from tkinter import ttk
import sv_ttk
import settings

class CompleteSlider:
    def __init__(self,root,name,maxValue,minValue,defaultValue) -> None:

        # add frame for padding
        frame_1 = ttk.Frame(master=root)
        frame_1.pack(pady=settings.paddingY, padx=0, fill="both", expand=True)

        slider = StringVar()
        slider.set('%d' % float(defaultValue))
        
        ttk.Label(frame_1,text=name)
        ttk.Scale(frame_1, value=defaultValue, from_=minValue, to_=maxValue, length=500, command=lambda s:slider.set('%d' % float(s)))
        ttk.Label(frame_1, textvariable=slider)

        for i, child in enumerate(frame_1.winfo_children()):
            child.grid(row=0,column=i)
            child.grid_configure(padx=20,pady=0)

        pass
    

