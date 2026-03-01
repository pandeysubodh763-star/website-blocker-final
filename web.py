import tkinter as tk
from tkinter import messagebox
import platform
import platform

# Determine hosts file path based on OS
if platform.system() == "Windows":
    hosts_path = r"C:\Windows\System32\drivers\etc\hosts"
elif platform.system() == "Darwin":  # macOS
    hosts_path = "/etc/hosts"
else:  # Linux/Unix
    hosts_path = "/etc/hosts"

redirect_ip = "127.0.0.1"  # Localhost IP to redirect blocked sites to

def block_website():#to block
    website = entry.get().strip()
    if not website:
        messagebox.showwarning("Warning", "Please enter a website")
        return
    
    websites_to_block = [website] #pATh
    if not website.startswith("www."):
        websites_to_block.append(f"www.{website}")
    elif website.startswith("www."):
        websites_to_block.append(website[4:])  # this program - 
    
    try:#try
        with open(hosts_path, "r+") as file:
            content = file.read()
            added = False
            for site in websites_to_block:
                if site not in content:
                    file.write(f"\n{redirect_ip} {site}")
                    added = True
            if added:
                messagebox.showinfo("Success", f"{website} (and variants) blocked")
            else:
                messagebox.showinfo("Info", f"{website} is already blocked")
    except PermissionError:
        messagebox.showerror("Error", "Run the program as Administrator (or with sudo on macOS/Linux)!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def unblock_website():#to unblock
    website = entry.get().strip()
    if not website:
        messagebox.showwarning("Warning", "Please enter a website")
        return
    
    websites_to_unblock = [website]
    if not website.startswith("www."):
        websites_to_unblock.append(f"www.{website}")# append
    elif website.startswith("www."):
        websites_to_unblock.append(website[4:])  # Add version without www.
    
    try:
        with open(hosts_path, "r+") as file:#try
            lines = file.readlines()
            file.seek(0)
            removed = False
            for line in lines:
                if not any(site in line.split() for site in websites_to_unblock):
                    file.write(line)
                else:
                    removed = True
            file.truncate()
            if removed:
                messagebox.showinfo("Success", f"{website} (and variants) unblocked")
            else:
                messagebox.showinfo("Info", f"{website} was not blocked")
    except PermissionError:
        messagebox.showerror("Error", "Run the program as Administrator (or with sudo on macOS/Linux)!")
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")# info

# GUI Window
root = tk.Tk()
root.title("Website Blocker")
root.geometry("350x200")
root.resizable(False, False)

tk.Label(root, text="Website Blocker", font=("Arial", 14, "bold")).pack(pady=10)
tk.Label(root, text="Enter website (example: facebook.com)").pack()

entry = tk.Entry(root, width=30)#entry
entry.pack(pady=5)

tk.Button(root, text="Block Website", width=20, command=block_website).pack(pady=5)
tk.Button(root, text="Unblock Website", width=20, command=unblock_website).pack(pady=5)

tk.Label(root, text="Run as Administrator (or sudo)", fg="red").pack(pady=5)

root.mainloop()
# features -blocks any website