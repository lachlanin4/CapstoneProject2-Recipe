from recipe import Recipe
import tkinter as tk
#Below is all test code

r1 = Recipe("Lasagne")
r1.set_description("Layers of pasta cheese and tomato sauce")
print(r1.get_description())
r1.set_no_servings(5)
r1.set_ingredients("tomato")
r1.set_ingredients("tomato")
r1.set_ingredients("cheese")
print(r1.get_ingredients())
r1.remove_ingredient(2)
print(r1.get_ingredients())
r1.display_ingredients()


window =tk.Tk()
label = tk.Label(text = r1.get_ingredients())
label.pack()
label2 = tk.Label(text = r1.display_ingredients()) #tkinter needs text= to display so this did not work
label2.pack()
window.mainloop()
