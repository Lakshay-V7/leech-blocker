import customtkinter as ct
from tkinter import messagebox
import os

def change_appearance_mode(app):
    ct.set_appearance_mode(optionmenu_1.get())

def blockingProcess(siteUrl):
    website_lists = customUrl.get()
    Website = list(website_lists.split(","))
    
    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for website in Website:
            if website in file_content:
                messagebox.showerror("Already Blocked", "The site " + siteUrl + " is already blocked")
                pass
            else:
                host_file.write('\n' + ip_address + " " + website + '\n')
                messagebox.showinfo("Blocking Action", "Blocking Action completed\n" + siteUrl + " is now blocked.\nFor this to take effect, restart your browser once.")

def blockingProcess2(siteUrl):
    Website_list = []
    Website_list.append(siteUrl)
    
    with open(host_path, 'r+') as host_file:
        file_content = host_file.read()
        for website in Website_list:
            if website in file_content:
                messagebox.showerror("Already Blocked", "The site " + siteUrl + " is already blocked")
                pass
            else:
                host_file.write('\n' + ip_address + " " + website + '\n')
                messagebox.showinfo("Blocking Action", "Blocking Action completed\n" + siteUrl + " is now blocked.\nFor this to take effect, restart your browser once.")

def unblocker():
    with open(host_path, 'w') as host_file:
        host_file.write('''# Copyright (c) 1993-2009 Microsoft Corp.
#
# This is a sample HOSTS file used by Microsoft TCP/IP for Windows.
#
# This file contains the mappings of IP addresses to host names. Each
# entry should be kept on an individual line. The IP address should
# be placed in the first column followed by the corresponding host name.
# The IP address and the host name should be separated by at least one
# space.
#
# Additionally, comments (such as these) may be inserted on individual
# lines or following the machine name denoted by a '#' symbol.
#
# For example:
#
#      102.54.94.97     rhino.acme.com          # source server
#       38.25.63.10     x.acme.com              # x client host

# localhost name resolution is handled within DNS itself.
#	127.0.0.1       localhost
#	::1             localhost
''')

def popup():
    response = messagebox.askyesno("Confirmation", "Are you sure about unblocking all the time sucking websites?")
    if response:
        popup2()
    else:
        pass

def popup2():
    response = messagebox.askyesno("Confirmation", "Do you really want to unblock them?")
    if response:
        popup3()
    else:
        pass

def popup3():
    response = messagebox.askyesno("Confirmation", "Don't you value your time even for bit. Still want to unblock?")
    if response:
        unblocker()
        messagebox.showinfo("Unblocked", "Ok you go waste your time and don't be productive. All sites are now unblocked")
    else:
        pass

host_path = r'C:\Windows\System32\drivers\etc\hosts'
ip_address = '127.0.0.1'

ct.set_appearance_mode("light")
ct.set_default_color_theme("blue")

app = ct.CTk()
app.title("LeechBlocker")
app.geometry("1020x500")
app.resizable(0,0)

# Config of main grid
app.grid_columnconfigure(1, weight=1)
app.grid_rowconfigure(0, weight=1)

# Frames define and place
# Left frame
frame_left = ct.CTkFrame(master=app, width=100, corner_radius=0)
frame_left.grid(row=0, column=0, sticky="ns")

# Right frame
frame_right = ct.CTkFrame(master=app, corner_radius=20, width=1000)
frame_right.grid(row=0, column=1, columnspan=3, rowspan=3, pady=10, padx=20, sticky="nswe")

# Dashboard frame
frame_dashboard = ct.CTkFrame(master=frame_right, corner_radius=30)
frame_dashboard.grid(row=0, column=0, rowspan=1, pady=10, padx=20, sticky="nw")

# Site frame
frame_sites = ct.CTkFrame(master=frame_right, corner_radius=10)
frame_sites.grid(row=1, column=0, columnspan=2, rowspan=8, pady=10, padx=20, sticky="nw")

# Creators frame
frame_credits = ct.CTkFrame(master=frame_right, corner_radius=10)
frame_credits.grid(row=1, column=2, pady=10, padx=10)

# Frame config
frame_left.grid_rowconfigure(0, minsize=10)   # Empty row with minsize as spacing
frame_left.grid_rowconfigure(5, weight=1)     # Empty row as spacing
frame_left.grid_rowconfigure(8, minsize=20)   # Empty row with minsize as spacing
frame_left.grid_rowconfigure(11, minsize=10)  # Empty row with minsize as spacing

frame_right.rowconfigure((0, 1, 2, 3), weight=1)
frame_right.rowconfigure(7, weight=10)
frame_right.columnconfigure((0, 1), weight=1)
frame_right.columnconfigure(2, weight=0)

frame_dashboard.rowconfigure(1, weight=1)
frame_dashboard.columnconfigure(0, weight=1)

# Left frame content
greeting = ct.CTkLabel(master=frame_left, text="Welcome to", font=("Roboto Medium", -12), anchor="w")
title = ct.CTkLabel(master=frame_left, text="LeechBlocker", font=("Roboto Medium", -20), anchor="w")
greeting.grid(row=0, column=0)
title.grid(row=1, column=0)

# Right frame content

# Dashboard frame content
dashboard = ct.CTkLabel(master=frame_dashboard,
                        text="DashBoard",
                        corner_radius=45,
                        fg_color=("white", "gray38"),
                        font=("Roboto Medium", -16),
                        anchor="w")
dashboard.grid(row=0, column=0, pady=10, padx=10, sticky="nw")

# Sites content

# Available sites
sitesAvailable = ct.CTkLabel(master=frame_sites,
                            text="Available sites to block:\n================",
                            font=("Roboto Medium", -16),
                            anchor="w")
sitesAvailable.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

# Button for Facebook
button_facebook = ct.CTkButton(master=frame_sites,
                                text="1. Facebook",
                                command=lambda: blockingProcess2("www.facebook.com"),
                                corner_radius=15)
button_facebook.grid(row=1, column=0, padx=10, pady=5, sticky="nw")

# Button for Instagram
button_instagram = ct.CTkButton(master=frame_sites,
                                text="2. Instagram",
                                command=lambda: blockingProcess2("www.instagram.com"),
                                corner_radius=15)
button_instagram.grid(row=2, column=0, padx=10, pady=5, sticky="nw")

# Button for YouTube
button_youtube = ct.CTkButton(master=frame_sites,
                                text="3. YouTube",
                                command=lambda: blockingProcess2("www.youtube.com"),
                                corner_radius=15)
button_youtube.grid(row=3, column=0, padx=10, pady=5, sticky="nw")

# Button for Twitter
button_twitter = ct.CTkButton(master=frame_sites,
                                text="4. Twitter",
                                command=lambda: blockingProcess2("www.twitter.com"),
                                corner_radius=15)
button_twitter.grid(row=4, column=0, padx=10, pady=5, sticky="nw")

# Button for Snapchat
button_snapchat = ct.CTkButton(master=frame_sites,
                                text="5. Snapchat",
                                command=lambda: blockingProcess2("www.snapchat.com"),
                                corner_radius=15)
button_snapchat.grid(row=5, column=0, padx=10, pady=5, sticky="nw")

# For custom URL
siteNotAvailable = ct.CTkLabel(master=frame_sites, text='''Can't find site you want to block? 
Don't worry just copy it in the input box given below.''',
                            font=("Roboto Medium", -14),
                            anchor="w")
siteNotAvailable.grid(row=6, column=0, padx=15, pady=20, sticky="nw")

# Input bar
customUrl = ct.CTkEntry(master=frame_sites,
                    width=120,
                    placeholder_text="eg. xyz.com")
customUrl.grid(row=7, column=0, columnspan=1, pady=20, padx=20, sticky="we")

# Enter button
enterButton = ct.CTkButton(master=frame_sites, text="Enter", command=lambda: blockingProcess(customUrl.get()))
enterButton.grid(row=7, column=1, pady=10, padx=10)

# Credits
credits = ct.CTkLabel(master=frame_credits,
                    text="This software is made by:",
                    font=("Roboto Medium", -17),
                    anchor="w")
credits.grid(row=0, column=0, padx=10, pady=10)

names = ct.CTkLabel(master=frame_credits,
                    text="1.Om Satapathy\n" + "2.Lakshay Verma\n" + "3.Bimal Tyagi\n" + "4.Rakshit Uniyal",
                    font=("Roboto Medium", -14))
names.grid(row=1, column=0, pady=10, sticky="w")

# Button unblock
unblock_button = ct.CTkButton(master=frame_right, text="Unblock", command=popup)
unblock_button.grid(row=2, column=2, sticky="s")

# Color theme change drop-down menu
optionmenu_1 = ct.CTkOptionMenu(master=frame_left,
                                values=["Light", "Dark", "System"],
                                command=change_appearance_mode)
optionmenu_1.grid(row=3, column=0, pady=10, padx=20, sticky="sw")

app.mainloop()
