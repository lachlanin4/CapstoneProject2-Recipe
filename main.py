import tkinter as tk
import tkinter.ttk as ttk

class MainWindow(tk.Tk):
    def __init__(self):
        super().__init__()

        self.invitation = "Recipe Manager"

        frame_main = ttk.Frame()
        frame_main.pack(fill=tk.BOTH, expand=True)

        btn_show_invitation = ttk.Button(frame_main, text="Welcome in Recipe Manager!", command=self.show_invitation)
        btn_show_invitation.pack(padx=10, pady=10)

    def show_invitation(self):
        invitation_window = InvitationWindow(self, invitation=self.invitation)


class InvitationWindow(tk.Toplevel):
    def __init__(self, master, invitation):
        super().__init__(master)

        self.invitation = invitation


        frame_main = tk.Frame(self)
        frame_main.pack(fill=tk.BOTH, expand=True)

        lbl_invitation = tk.Label(frame_main, text=f"{self.invitation}")
        lbl_invitation.pack(padx=50, pady=50)

        # Define recipe_frame and add buttons
        self.recipe_frame = ttk.Frame(self)
        self.recipe_frame.pack(fill=tk.BOTH, expand=True)

        btn_select_to_display_recipe = ttk.Button(master=self.recipe_frame, text="Display Recipe", command=self.display)
        btn_select_to_display_recipe.pack(padx=10, pady=10)

        btn_select_to_add_recipe = ttk.Button(master=self.recipe_frame, text="Add Recipe", command=self.add)
        btn_select_to_add_recipe.pack(padx=10, pady=10)

        btn_select_to_edit_recipe = ttk.Button(master=self.recipe_frame, text="Edit Recipe", command=self.edit)
        btn_select_to_edit_recipe.pack(padx=10, pady=10)

        btn_select_to_remove_recipe = ttk.Button(master=self.recipe_frame, text="Remove Recipe", command=self.remove)
        btn_select_to_remove_recipe.pack(padx=10, pady=10)


    def display(self):
        print("Display Recipe button clicked!")
    
    def add(self):
        print("Add Recipe button clicked!")

    def edit(self):
        print("Edit Recipe button clicked!")

    def remove(self):
        print("Remove Recipe button clicked!")



if __name__ == "__main__":
    main_window = MainWindow()
    main_window.title("Main Window")

    main_window.mainloop()