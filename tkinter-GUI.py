import genesis as gs
import tkinter as tk
from tkinter import scrolledtext

# Initialize Genesis with GPU backend
gs.init(backend=gs.gpu)

# Create the main window
root = tk.Tk()
root.title("Genesis GUI")

# Create a frame for the code editor and buttons
left_frame = tk.Frame(root)
left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a scrolled text widget for the code editor
code_editor = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD)
code_editor.pack(fill=tk.BOTH, expand=True)

# Insert the initial code into the code editor
part1 = """
import genesis as gs
gs.init(backend=gs.gpu)

scene = gs.Scene(show_viewer=True)
"""
part2 = """
plane = scene.add_entity(gs.morphs.Plane())
franka = scene.add_entity(
    gs.morphs.MJCF(file='xml/franka_emika_panda/panda.xml'),
)
"""
part3 = """
scene.build()

for i in range(1000):
    scene.step()
"""
initial_code = part1 + part2 + part3
code_editor.insert(tk.INSERT, initial_code)

# Create a frame for the buttons
button_frame = tk.Frame(left_frame)
button_frame.pack(fill=tk.X)

# Define the run and pause functions
def run_code():
    code = code_editor.get("1.0", tk.END)
    if "gs.init(" in code:
        code = code.replace("gs.init(backend=gs.gpu)\n", "")
    exec(code)

def pause_code():
    # Implement pause functionality if needed
    pass

# Function to add a robotic arm
def add_robotic_arm():
    current_code = code_editor.get("1.0", tk.END)
    part1_end = current_code.find(part2)
    part2_end = current_code.find(part3)
    part2_code = current_code[part1_end:part2_end]
    new_arm_code = """
scene.add_entity(
    gs.morphs.MJCF(file="xml/franka_emika_panda/panda.xml", pos=(0.0, {y_pos}, 0.0)),
    material=gs.materials.Rigid(gravity_compensation={gravity}),
)
"""
    y_pos = part2_code.count("scene.add_entity(") * 1.0
    gravity = y_pos * 0.5
    new_arm_code = new_arm_code.format(y_pos=y_pos, gravity=gravity)
    updated_code = current_code[:part1_end] + part2_code + new_arm_code + current_code[part2_end:]
    code_editor.delete("1.0", tk.END)
    code_editor.insert(tk.INSERT, updated_code)

# Function to remove the last robotic arm
def remove_robotic_arm():
    current_code = code_editor.get("1.0", tk.END)
    part1_end = current_code.find(part2)
    part2_end = current_code.find(part3)
    part2_code = current_code[part1_end:part2_end]
    if "scene.add_entity(" in part2_code:
        last_arm_index = part2_code.rfind("scene.add_entity(")
        end_index = part2_code.find("\n", last_arm_index) + 1
        part2_code = part2_code[:last_arm_index] + part2_code[end_index:]
        updated_code = current_code[:part1_end] + part2_code + current_code[part2_end:]
        code_editor.delete("1.0", tk.END)
        code_editor.insert(tk.INSERT, updated_code)

# Create the run and pause buttons
run_button = tk.Button(button_frame, text="Run", command=run_code)
run_button.pack(side=tk.LEFT)

pause_button = tk.Button(button_frame, text="Pause", command=pause_code)
pause_button.pack(side=tk.LEFT)

# Create the add and remove buttons
add_button = tk.Button(button_frame, text="Add Arm", command=add_robotic_arm)
add_button.pack(side=tk.LEFT)

remove_button = tk.Button(button_frame, text="Remove Arm", command=remove_robotic_arm)
remove_button.pack(side=tk.LEFT)

# Create a frame for the rendering window
right_frame = tk.Frame(root)
right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

# Add the rendering window to the right frame
# Note: This is a placeholder. Replace with actual rendering window code.
render_label = tk.Label(right_frame, text="Rendering Window")
render_label.pack(fill=tk.BOTH, expand=True)

# Start the Tkinter main loop
root.mainloop()


