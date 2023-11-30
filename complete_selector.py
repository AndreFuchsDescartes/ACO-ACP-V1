from tkinter import *
from tkinter import ttk
import sv_ttk
import settings

class completeSelector:
    def __init__(self,root,name,defaultvalue) -> None:
        # add frame for padding
        frame_1 = ttk.Frame(master=root)
        frame_1.pack(pady=settings.paddingY, padx=0, fill="both", expand=True)

        options = ('Bandit Archer',
                   'Theodoros',
                   'Aya',
                   'The Duelist',
                    'Abstergo Trooper',
                    'Hepzefa',
                    'Hotephres',
                    'Greek Soldier?',
                    'Jeska',
                    'Layla',
                    'Kawit',
                    'Khaliset',
                    'Rai',
                    'Roman Scout',
                    'Kensa',
                    'Nubian Soldier',
                    'Tahira',
                    'Roman Soldier',
                    'Bandit Warrior',
                    'Son of Ra',
                    
                    'Bayek')
        currentvalue = StringVar()

        ttk.Label(frame_1,text=name)
        ttk.OptionMenu(frame_1,currentvalue,options[defaultvalue],*options)

        for i, child in enumerate(frame_1.winfo_children()):
            child.grid(row=0,column=i)
            child.grid_configure(padx=20,pady=0)
        pass