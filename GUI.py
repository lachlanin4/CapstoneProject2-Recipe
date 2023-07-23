import tkinter as tk
from tkinter import ttk
from recipe import Recipe
# from recipemanager import RecipeManager
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
root.title("Recipe Menager")
listbox:None # I am not defining this variable
#lbl_recipe_listbox = tk.Label(text="Here are your recipes:")
# recipe_manager = RecipeManager() I put it in comment
# recipe_manager.recipes = ['pie', 'tart', 'lasagne']
recipes = ["carbonara", "tart", "boiled eggs"]

list_items = tk.StringVar(value=recipes) # saying the tinkter that our list is str variable

# def display_recipes(): #we don't need it here 
#     main_listbox()

#Create a Listbox
def main_listbox():
    global listbox # this variable NEED to be global - information to myslef, because I am thinking that is main variable all the time
    list_items = tk.Variable(value=recipes) #add recipe menager later
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


#this functions are until recipe meanger will be working properly. I know that I shouldn't test it in main file. I am sorry but I used to it so badly :( 
#I think that will be good base to do Recipe Menager 
# Function to add a new recipe
def add_recipe():
    title = ent_recipe.get()
    recipes.append(title)
    list_items.set(recipes)  
    main_listbox()

# Function to remove a recipe
def remove_recipe():
    global listbox
    selected_indices = listbox.curselection()
    if selected_indices:
        index_to_remove = selected_indices[0]
        recipes.pop(index_to_remove)
        list_items.set(recipes)  
        main_listbox()

# Function to edit a recipe
def edit_recipe():
    global listbox
    selected_indices = listbox.curselection()
    if selected_indices:
        index_to_edit = selected_indices[0]
        new_title = ent_recipe.get()
        recipes[index_to_edit] = new_title
        list_items.set(recipes)  
        main_listbox()

def display_recipe():
    selected_indices = listbox.curselection()
    if selected_indices:
        index = selected_indices[0]
        selected_recipe = recipes[index]



#The below is direcetory selector on uml but need to look into filedialog again


# display_recipes()
#tkinter.filedialog.askdirectory() #This pops up the file explorer
ent_recipe = tk.Entry(fg="blue",bg = "pink", width=50)
ent_recipe.pack()

# requested_recipe = ent_recipe.get()

#submit button
# btn_recipe=tk.Button(text="Submit",command="") #Do we need this button?
# btn_recipe.pack()

#recipe_display:tkinter.modal dialog box
#recipe_edit same as above

#All the buttons and packed them
btn_select_to_remove = tk.Button(text= "Remove Recipe",command=remove_recipe)
btn_select_to_remove.pack()
btn_select_to_search = tk.Button(text="Edit Recipe", command=edit_recipe)
btn_select_to_search.pack()
btn_select_to_add = tk.Button(text="Add Recipe",command=add_recipe)
btn_select_to_add.pack()
btn_select_to_display_recipe = tk.Button(text="Display Recipe",command="")
btn_select_to_display_recipe.pack()
# btn_select_to_edit_recipe = tk.Button(text="Edit Recipe", command=edit_recipe) #this button is not showing up, why?
# btn_select_to_display_recipe.pack()

# def display_recipe():


main_listbox() 
root.mainloop()
