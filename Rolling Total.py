import tkinter as tk
import pandas as pd
from pandastable import Table

# Sample DataFrame
df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "Los Angeles", "Chicago"]
})

# Create the main window
root = tk.Tk()
root.title("Pandas DataFrame in Tkinter")

# Create a frame for the table
frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True)

# Create the table
table = Table(frame, dataframe=df, showtoolbar=True, showstatusbar=True)
table.show()

# Run the application
root.mainloop()