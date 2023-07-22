import tkinter as tk
from tkinter import ttk
from recipe import Recipe
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
#lbl_recipe_listbox = tk.Label(text="Here are your recipes:")
recipe_manager = RecipeManager()
recipe_manager.recipes = ['pie', 'tart', 'lasagne']

def display_recipes():
    main_listbox()

#Create a Listbox
def main_listbox():
    list_items=tk.Variable(value= recipe_manager.recipes)
    listbox = tk.Listbox(
        root,
        height = 10,
        listvariable = list_items,
        selectmode=tk.SINGLE
    )
    #Formatting listbox so it fills screen
    listbox.pack(expand=True,fill=tk.BOTH, side=tk.LEFT)

    scrollbar = ttk.Scrollbar(
        root,
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


display_recipes()
tkinter.filedialog.askdirectory()
ent_recipe = tk.Entry(fg="blue",bg = "pink", width=50)
ent_recipe.pack()

requested_recipe = ent_recipe.get()

btn_recipe=tk.Button(text="Submit",command="")
btn_recipe.pack()

#recipe_display:tkinter.modal dialog box
#recipe_edit same as above

#All the buttons and packed them
btn_select_to_remove = tk.Button(text= "Remove Recipe",command="")
btn_select_to_remove.pack()
btn_select_to_search = tk.Button(text="Search",command="")
btn_select_to_search.pack()
btn_select_to_add = tk.Button(text="Add Recipe",command="")
btn_select_to_add.pack()
btn_select_to_display_recipe = tk.Button(text="Display Recipe",command="")
btn_select_to_display_recipe.pack()
btn_select_to_edit_recipe = tk.Button(text="Edit Recipe", command="")
btn_select_to_display_recipe.pack()

# def display_recipe():


    
root.mainloop()
