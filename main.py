import tkinter as tk
import os
import subprocess


# Window setup
root = tk.Tk()
root.title("Color Previewer")
root.geometry("500x500")
root.resizable(False, False)
root.iconbitmap('./assets/icon.ico')


# Functions
def rgb_to_hex() -> str:
    return '#%02x%02x%02x'.upper() % (red_slider.get(), green_slider.get(), blue_sider.get())


def display(_) -> None:
    new_color = rgb_to_hex()
    root.configure(bg=new_color)
    hex_label.configure(text=new_color)
    title.    configure(bg=new_color)
    hex_label.configure(bg=new_color)


def save_to_file() -> bool:
    current_color = rgb_to_hex()
    try:
        with open("saved_colors.txt", 'a') as f:
            f.write(current_color + "\n")
            return True
    except Exception:   # noqa
        return False


def copy_to_clipboard():
    current_color = rgb_to_hex()
    if os.name == 'nt':
        command = f'echo {current_color}|clip'
    else:
        command = f'echo {current_color}|pbcopy'
    subprocess.check_call(command, shell=True)


# GUI #
title = tk.Label(root, text="Color Previewer", font=("Helvetica", 16))
title.pack(side="top", fill="x", expand=False, padx=10, pady=10)


# RGB Sliders
red_slider = tk.Scale(root, from_=0, to=255, tickinterval=255, orient=tk.HORIZONTAL, bg="RED", length=200,
                      command=display)
red_slider.pack(side="top", fill='y', expand=False, padx=10, pady=10)
red_slider.set(255)

green_slider = tk.Scale(root, from_=0, to=255, tickinterval=255, orient=tk.HORIZONTAL, bg="GREEN", length=200,
                        command=display)
green_slider.pack(side="top", fill='y', expand=False, padx=10, pady=10)
green_slider.set(255)

blue_sider = tk.Scale(root, from_=0, to=255, tickinterval=255, orient=tk.HORIZONTAL, bg="BLUE", length=200,
                      command=display)
blue_sider.pack(side="top", fill='y', expand=False, padx=10, pady=10)
blue_sider.set(255)


# Hex
hex_label = tk.Label(root, text="#ffffff", font=("Helvetica", 20))
hex_label.pack(side="top", fill='y', expand=True, padx=10, pady=10)


# Buttons
copy_to_clipboard_button = tk.Button(root, text="Copy to Clipboard", font=("Helvetica", 16), command=copy_to_clipboard)
copy_to_clipboard_button.pack(side="top", fill='y', expand=True, padx=10, pady=10)

save_to_file_button = tk.Button(root, text="Save to File", font=("Helvetica", 16), command=save_to_file)
save_to_file_button.pack(side="top", fill='y', expand=True, padx=10, pady=10)


if __name__ == '__main__':
    root.mainloop()
