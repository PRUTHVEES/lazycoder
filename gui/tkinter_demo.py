import tkinter as tk
from tkinter import ttk


class ZenmapApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Lazy Coder")
        self.root.geometry("800x700")

        self.icons = {}
        self.create_widgets()

    def create_widgets(self):
        title_bar = tk.Frame(self.root, bg="#d4d0c8", relief="raised", bd=2)
        title_bar.pack(fill="x")

        title_label = tk.Label(title_bar, text="Lazy Coder", bg="#d4d0c8", font=("Arial", 10, "bold"))
        title_label.pack(expand=True, anchor="center")

        menu_bar = tk.Frame(self.root, bg="#d4d0c8", relief="raised", bd=2)
        menu_bar.pack(fill="x")
        for menu in ["Commands", "Tools", "Profile", "Help"]:
            menu_label = tk.Label(menu_bar, text=menu, bg="#d4d0c8", font=("Arial", 10))
            menu_label.pack(side="left", padx=10)
            self.add_hover_effect(menu_label)

        toolbar = tk.Frame(self.root, bg="#e5e5e5", relief="raised", bd=2)
        toolbar.pack(fill="x")
        for icon in ["New Command", "Command Wizard", "Save Command", "Open Command", "Report Bug", "Help"]:

            try:
                image = tk.PhotoImage(file=f"icons/{icon}.png")
            except Exception as e:
                image = None
            self.icons[icon] = image

            icon_label = tk.Label(toolbar, text=icon, image=image, compound="left",
                                  bg="#e5e5e5", font=("Arial", 10))
            icon_label.pack(side="left", padx=5)
            self.add_hover_effect(icon_label)

        content_frame = tk.Frame(self.root)
        content_frame.pack(fill="both", expand=True)

        sidebar = tk.Frame(content_frame, width=200, bg="#e5e5e5", relief="sunken", bd=2)
        sidebar.pack(side="left", fill="y")
        self.create_sidebar(sidebar)

        main_content = tk.Frame(content_frame, bg="#ffffff", relief="sunken", bd=2)
        main_content.pack(side="left", fill="both", expand=True)
        self.create_main_content(main_content)

    def add_hover_effect(self, widget):

        widget.bind("<Enter>", lambda e: widget.config(bg="#4169e1"))

        widget.bind("<Leave>", lambda e: widget.config(bg="#d4d0c8"
        if widget.cget("text") in ["Lazy Coder", "Command", "Tools", "Profile", "Help"]
        else "#e5e5e5"))

    def create_sidebar(self, sidebar):
        target_label = tk.Label(sidebar, text="Target:", bg="#e5e5e5", font=("Arial", 10))
        target_label.pack(anchor="w", padx=5, pady=2)
        target_entry = tk.Entry(sidebar, width=30)
        target_entry.pack(anchor="w", padx=5, pady=2)
        target_entry.insert(0, "www.sanchi.com")

        profile_label = tk.Label(sidebar, text="Profile:", bg="#e5e5e5", font=("Arial", 10))
        profile_label.pack(anchor="w", padx=5, pady=2)
        profile_entry = tk.Entry(sidebar, width=30)
        profile_entry.pack(anchor="w", padx=5, pady=2)
        profile_entry.insert(0, "Pruthveesh Gharal")

        command_label = tk.Label(sidebar, text="Command:", bg="#e5e5e5", font=("Arial", 10))
        command_label.pack(anchor="w", padx=5, pady=2)
        command_entry = tk.Entry(sidebar, width=30)
        command_entry.pack(anchor="w", padx=5, pady=2)
        command_entry.insert(0, "vinaymore69")

        scan_button = tk.Button(sidebar, text="Scan", bg="#d4d0c8", font=("Arial", 10))
        scan_button.pack(anchor="w", padx=5, pady=5, fill="x")
        self.add_hover_effect(scan_button)

        hosts_label = tk.Label(sidebar, text="Hosts", bg="#e5e5e5", font=("Arial", 10, "bold"))
        hosts_label.pack(anchor="w", padx=5, pady=5)
        hosts_list = tk.Listbox(sidebar, height=22)
        hosts_list.pack(anchor="w", padx=5, pady=2, fill="x")
        for host in ["sanchi.com", "172.12.0.1", ":8090", "vinaymore.in", "vpt.edu.in"]:
            hosts_list.insert(tk.END, host)

    def create_main_content(self, main_content):
        notebook = ttk.Notebook(main_content)
        notebook.pack(fill="both", expand=True)

        tab_ports = ttk.Frame(notebook)
        notebook.add(tab_ports, text="Ports / Hosts")
        text_ports = tk.Text(tab_ports, wrap="word", bg="#ffffff", font=("Arial", 10))
        text_ports.pack(fill="both", expand=True)
        text_ports.insert(tk.END, "Ports / Hosts Content...")

        tab_nmap = ttk.Frame(notebook)
        notebook.add(tab_nmap, text="Nmap Output")
        text_nmap = tk.Text(tab_nmap, wrap="word", bg="#ffffff", font=("Arial", 10))
        text_nmap.pack(fill="both", expand=True)
        text_nmap.insert(tk.END, "Nmap Output Content...")

        tab_host_details = ttk.Frame(notebook)
        notebook.add(tab_host_details, text="Host Details")
        text_host = tk.Text(tab_host_details, wrap="word", bg="#ffffff", font=("Arial", 10))
        text_host.pack(fill="both", expand=True)
        text_host.insert(tk.END, "Host Details Content...")

        tab_scan = ttk.Frame(notebook)
        notebook.add(tab_scan, text="Scan Details")
        text_scan = tk.Text(tab_scan, wrap="word", bg="#ffffff", font=("Arial", 10))
        text_scan.pack(fill="both", expand=True)
        text_scan.insert(tk.END, "Scan Details Content...")


if __name__ == "__main__":
    root = tk.Tk()
    app = ZenmapApp(root)
    root.mainloop()