import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext #Imports tkinter
from CODEX_MMO import * #Imports all from the file, CODEX_MMO


def apply_filters():    
    primary_filter = primary_var.get() #This is used 
    secondary_filter = secondary_var.get()

    text_box.insert(tk.END, f"Primary filter: {primary_filter}\n")
    text_box.insert(tk.END, f"Secondary filter: {secondary_filter}\n") #This bit allows the user to see what filter options they've chosen, or chosen prior
    text_box.insert(tk.END, "Filtered creatures:\n")

    if primary_filter == "Location":
        for x in sortlist:
            if x == 55:
                break
            mmonumber = x
            sortkey_x = mmolist[mmonumber] #This acts like the sublist commmand to filter through lists of lists, super handy
            sortkey_y = sortkey_x[0] #The big distinction is that sublist doesnt allow the interaction of other lists further embedded within lists without affecting all lists
            if secondary_filter in sortkey_y: #Instead of checking a specific variable, this identifies if the secondary variable is in the list at all.
                text_box.insert(tk.END, sortkey_x[2])
                if x == 55:
                    break

    if primary_filter == "Type": #This is just a basic check to make sure the filter matches a cretaures variables before printing
        for x in sortlist:
            if x == 55:
                break
            mmonumber = x
            sortkey_x = mmolist[mmonumber]
            sortkey_y = sortkey_x[1]
            if sortkey_y[1] == secondary_filter:
                text_box.insert(tk.END, sortkey_x[2]) #This lets the variables be printed into the tkinter textbox
                if x == 55:
                    break

    if primary_filter == "CR": 
        for x in sortlist:
            if x == 55:
                break
            mmonumber = x
            sortkey_x = mmolist[mmonumber]
            sortkey_y = sortkey_x[1]
            if sortkey_y[0] == secondary_filter:
                text_box.insert(tk.END, sortkey_x[2])
                if x == 55:
                    break

app = tk.Tk()
app.title("D&D Codex")
app.geometry("600x400")

primary_options = ["Location", "Type", "CR"] 

primary_var = tk.StringVar()
primary_dropdown = ttk.Combobox(app, textvariable=primary_var, values=primary_options)
primary_dropdown.grid(row=0, column=0, padx=10, pady=10)

secondary_options = { #These are the variables available in the dropdown boxs
    "Location": ["Anywhere", "Battlefields", "Cave", "Coastal", "Deserts and plains",
                         "Demon army", "Devil army", "Dungeons", "Edge of civilisation",
                         "Elemental plains", "Forest", "Grassland", "Hills", "Jungle",
                         "Labratories", "Mountain", "Rivers and lakes", "Ruins", "Swamps",
                         "Tundra", "Urban", "Underdark", "Underground", "Underwater","Divine Realms"], #I have chosen to put each on seperate lines for easier viewing and editing
    "Type": ["Aberration", "Beast", "Celestial", "Dragon", "Elemental",
                     "Fey", "Fiend", "Giant", "Humanoid", "Monstrosity",
                     "Ooze", "Plant", "Undead"],
    "CR": ["CR 0", "CR 1/8", "CR 1/4", "CR 1/2", "CR 1", "CR 2", "CR 3",
    "CR 4", "CR 5", "CR 6", "CR 7", "CR 8", "CR 9", "CR 10", "CR 11",
    "CR 12", "CR 13", "CR 14"]
}

secondary_var = tk.StringVar()
secondary_dropdown = ttk.Combobox(app, textvariable=secondary_var, values=[])
secondary_dropdown.grid(row=0, column=1, padx=10, pady=10)

def update_secondary_dropdown(event):
    selected_primary = primary_var.get()
    if selected_primary in secondary_options:
        secondary_dropdown['values'] = secondary_options[selected_primary]
    else:
        secondary_dropdown['values'] = []

primary_dropdown.bind("<<ComboboxSelected>>", update_secondary_dropdown) 

text_box = scrolledtext.ScrolledText(app, wrap=tk.WORD, width=100, height=30)
text_box.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

apply_button = tk.Button(app, text="Apply Filters", command=apply_filters)
apply_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)



app.mainloop()

#End of Script
