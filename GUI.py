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
)

#Formatting listbox so it fills screen
listbox.pack(expand=True, fill=tk.BOTH)
root.mainloop()