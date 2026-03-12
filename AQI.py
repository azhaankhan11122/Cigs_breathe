import math
import tkinter as tk
from tkinter import simpledialog, messagebox

def calculate_cigs(concentration):
    pm25_conversion = 22.0  # 22 ug/m^3 = 1 cig/day
    
    if concentration <= 0:
        return "No it's not lmao."
    
    if concentration > 10000:
        return "RIP you"

    cigs_per_day = concentration / pm25_conversion
    cigs_per_hour = round(cigs_per_day / 24.0, 2)
    
    # Calculate time breakdown
    hours_per_cig = 1.0 / cigs_per_hour
    hours = int(hours_per_cig)
    minutes_float = (hours_per_cig - hours) * 60
    minutes = int(minutes_float)
    seconds = int(round((minutes_float - minutes) * 60))

    time_str = f"{hours}h {minutes}m {seconds}s"
    
    return (f"At {concentration} µg/m³:\n\n"
            f"🚬 {cigs_per_hour} cigs per hour\n"
            f"⏱️ 1 cig every {time_str}")

def main():
    # Setup a hidden root window so the dialogs look clean
    root = tk.Tk()
    root.withdraw()

    # Pop up the input window
    user_input = simpledialog.askstring("Air Quality Calculator", "Enter the PM2.5 concentration (µg/m³):")

    if user_input is not None:
        try:
            concentration = float(user_input)
            result = calculate_cigs(concentration)
            messagebox.showinfo("Your Results", result)
        except ValueError:
            messagebox.showerror("Error", "Wtf man, give me a real number for your AQI.")
    
    root.destroy()

if __name__ == "__main__":
    main()