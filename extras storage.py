label = tk.Label(root, text="Choose Account")
label.place(x=90, y=200)
option =["Domestic > Savings", "Domestic > Current", "International > Savings", "International > Current"]
ops = ttk.Combobox(root, values=option)
ops.place(x=70, y=220)
ops.set(" ")