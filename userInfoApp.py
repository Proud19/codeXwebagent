import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class UserInfoApp:
    def __init__(self, root, on_submit):
        self.root = root
        self.on_submit = on_submit
        self.root.title("User Information")

        # Create frames
        self.user_info_frame = ttk.Frame(self.root)
        self.user_info_frame.pack(padx=10, pady=10, fill='x', expand=True)

        self.login_frame = ttk.Frame(self.root)

        # User Info Page
        self.create_user_info_page()

        self.root.mainloop()

    def create_user_info_page(self):
        # User information fields
        fields = [
            ("Age", tk.Entry),
            ("Gender", ttk.Combobox, {"values": ["Male", "Female", "Other"]}),
            ("Interests", tk.Entry),
            ("Location (country)", tk.Entry),
            ("Education level", tk.Entry),
            ("Occupation", tk.Entry),
            ("Previous experience with the site", tk.Entry),
            ("Internet proficiency", ttk.Combobox, {"values": ["Beginner", "Intermediate", "Advanced"]}),
            ("Mobile or desktop user", ttk.Combobox, {"values": ["Mobile", "Desktop"]}),
            ("Other behavioral traits", tk.Entry)
        ]

        self.entries = {}

        for idx, (label_text, widget, *options) in enumerate(fields):
            label = ttk.Label(self.user_info_frame, text=label_text)
            label.grid(row=idx, column=0, pady=5, sticky=tk.W)
            entry = widget(self.user_info_frame, **(options[0] if options else {}))
            entry.grid(row=idx, column=1, pady=5, sticky=tk.EW)
            self.entries[label_text] = entry

        # Next button
        self.next_button = ttk.Button(self.user_info_frame, text="Next", command=self.show_login_page)
        self.next_button.grid(row=len(fields), columnspan=2, pady=10)

    def show_login_page(self):
        # Collect user info
        self.user_info = {label: entry.get() for label, entry in self.entries.items()}
        print("Collected User Info:", self.user_info)

        # Hide user info frame and show login frame
        self.user_info_frame.pack_forget()
        self.login_frame.pack(padx=10, pady=10, fill='x', expand=True)

        # Login information fields
        ttk.Label(self.login_frame, text="Website URL").grid(row=0, column=0, pady=5, sticky=tk.W)
        self.website_url = ttk.Entry(self.login_frame)
        self.website_url.grid(row=0, column=1, pady=5, sticky=tk.EW)

        ttk.Label(self.login_frame, text="Username").grid(row=1, column=0, pady=5, sticky=tk.W)
        self.username = ttk.Entry(self.login_frame)
        self.username.grid(row=1, column=1, pady=5, sticky=tk.EW)

        ttk.Label(self.login_frame, text="Password").grid(row=2, column=0, pady=5, sticky=tk.W)
        self.password = ttk.Entry(self.login_frame, show="*")
        self.password.grid(row=2, column=1, pady=5, sticky=tk.EW)

        # Submit button
        self.submit_button = ttk.Button(self.login_frame, text="Submit", command=self.submit_login_info)
        self.submit_button.grid(row=3, columnspan=2, pady=10)

    def submit_login_info(self):
        # Collect login info
        self.login_info = {
            "website_url": self.website_url.get(),
            "username": self.username.get(),
            "password": self.password.get()
        }
        print("Collected Login Info:", self.login_info)

        # Quit the application
        self.root.quit()

        # Call the callback function with collected data
        self.on_submit(self.login_info, self.user_info)

       

def runUserInfoApp(completion):
    root = tk.Tk()
    UserInfoApp(root, completion)
