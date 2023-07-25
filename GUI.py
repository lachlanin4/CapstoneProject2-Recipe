import tkinter as tk
from tkinter import ttk
#from recipe import Recipe
from recipemanager import RecipeManager
import tkinter.filedialog
#from recipemanager import Recipe

"""
# class Main_Application(tk.Frame):
#     def __init__(self,parent,*args,**kwargs):
#         tk.Frame.__init__(self,parent,*args,**kwargs)
#         self.parent = parent

# if __name__ == "__main__":
#     root = tk.Tk()
#     Main_Application(root).pack(side="top", fill="both", expand=True)
#     root.mainloop()
"""


root = tk.Tk()
recipe_manager = RecipeManager()
recipe_manager.recipes = ['pie', 'tart', 'lasagne']

def display_recipes():
    main_listbox()

#Create a Listbox
def main_listbox():
    list_items=tk.Variable(value= recipe_manager.recipes)
    listbox = tk.Listbox(
        master=main_frame,
        height = 10,
        listvariable = list_items,
        selectmode=tk.SINGLE
    )
    #Formatting listbox so it fills screen
    listbox.pack(expand=True,fill=tk.BOTH, side=tk.LEFT)

    scrollbar = ttk.Scrollbar(
        master=main_frame,
        orient=tk.VERTICAL,
        command=listbox.yview
    )
    listbox["yscrollcommand"] = scrollbar.set
    scrollbar.pack(side=tk.LEFT,expand=True, fill=tk.Y)


    def items_selected(event):
        #gets selected item
        selected_indices  = listbox.curselection()
        selected_recipes=",".join([listbox.get(i) for i in selected_indices])
        msg=f"You selected: {selected_recipes}"
        chosen_item = tk.Label(text=msg)
        chosen_item.pack()

    listbox.bind('<<ListboxSelect>>', items_selected)


#The below is direcetory selector on uml but need to look into filedialog again
entire_frame= tk.Frame(master=root,relief=tk.RIDGE,borderwidth=10)
entire_frame.pack()
entire_frame.place(relx=0.5,rely=0.5,anchor=tk.CENTER)
title_frame = tk.Frame(master=entire_frame,relief=tk.RIDGE, borderwidth=10)
title_frame.pack()
editing_frame = tk.Frame(master=entire_frame, relief=tk.RIDGE, borderwidth=5)
editing_frame.pack()
main_frame = tk.Frame(master=entire_frame,relief=tk.RIDGE, borderwidth=5)
main_frame.pack()
recipe_frame= tk.Frame(master=entire_frame,relief=tk.RIDGE,borderwidth=5)
recipe_frame.pack()



#Recipes is the title that is going to go above everything
lbl_recipe_listbox = tk.Label(master=title_frame,text="Recipes")
lbl_recipe_listbox.pack(padx=5,pady=5)
display_recipes()
#tkinter.filedialog.askdirectory() #This pops up the file explorer



#recipe_display:tkinter.modal dialog box
#recipe_edit same as above

#All the buttons and packed them
btn_select_to_remove = tk.Button(master=editing_frame,text= "Remove Recipe",command="")
btn_select_to_remove.grid(row=0,column=0)
btn_select_to_search = tk.Button(master=editing_frame,text="Search",command="")
btn_select_to_search.grid(row=0,column=2)
btn_select_to_add = tk.Button(master=editing_frame,text="Add Recipe",command="")
btn_select_to_add.grid(row=0,column=1)
btn_select_to_display_recipe = tk.Button(master=recipe_frame,text="Display Recipe",command="")
btn_select_to_display_recipe.grid(row=0,column=0)
btn_select_to_edit_recipe = tk.Button(master=recipe_frame,text="Edit Recipe", command="")
btn_select_to_edit_recipe.grid(row=0,column=1)

#Ent_recipe is going to go with when user wants to add recipe name, add ingredients, add instructions
ent_recipe = tk.Entry(master=editing_frame,fg="blue",bg = "pink", width=30)
#ent_recipe.pack()
requested_recipe = ent_recipe.get()

btn_recipe=tk.Button(master=editing_frame, text="Submit",command="")
#btn_recipe.pack()

# def display_recipe():


    
root.mainloop()
