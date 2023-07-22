import tkinter as tk
#from recipe import Recipe
from recipemanager import RecipeManager
#from recipemanager import Recipe


# class Main_Application(tk.Frame):
#     def __init__(self,parent,*args,**kwargs):
#         tk.Frame.__init__(self,parent,*args,**kwargs)
#         self.parent = parent

# if __name__ == "__main__":
#     root = tk.Tk()
#     Main_Application(root).pack(side="top", fill="both", expand=True)
#     root.mainloop()
recipe_manager = RecipeManager()
recipe_manager.recipes = ['pie', 'tart', 'lasagne']
#Create the root
root = tk.Tk()
root.title('Listbox')

#Create a Listbox
list_items=tk.Variable(value= recipe_manager.recipes)
listbox = tk.Listbox(
    root,
    height = 10,
    listvariable = list_items,
    selectmode=tk.SINGLE
)
#Formatting listbox so it fills screen
listbox.pack(expand=True, fill=tk.X)

"""
##This was meant to let you select the recipe but listbox.curselection() returns a tuple making it difficult
# def items_selected(event):
#     #gets selected item
#     selected_recipe  = listbox.curselection()
#     tk.Label(text=(f"You have selected{recipe_manager.recipes[selected_recipe[0]]}"))
#listbox.bind('<<ListboxSelect>>', callback)
"""
requested_recipe = tk.Entry(fg="blue",bg = "pink", width=50)
requested_recipe.pack()

root.mainloop()
