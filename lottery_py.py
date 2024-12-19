# Comprehensive Lottery Selection App
import tkinter as tk
from tkinter import messagebox, simpledialog, scrolledtext
import random
import os
from datetime import datetime

class LotteryApp:
    def __init__(self):
        # Modern UI Configuration
        self.root = tk.Tk()
        self.root.title("🎲 Dynamic Lottery Selector")
        self.root.geometry("650x650")  # Increased height
        self.root.configure(bg='#3D3D3D')

        # Participants and Winners Management
        self.participants = []
        self.winners_history = []
        self.create_ui()

    def create_ui(self):
        # Responsive UI Components
        tk.Label(
            self.root, 
            text="Lottery Participant Selector", 
            font=("Arial", 18, "bold"),
            bg='#f0f0f0'
        ).pack(pady=20)

        # Button Styling
        button_style = {
            'font': ('Arial', 12),
            'width': 25,
            'pady': 10
        }

        # Dynamic Buttons
        buttons = [
            ("Add Participant", self.add_participant, 'lightblue'),
            ("View Participants", self.view_participants, 'lightgreen'),
            ("Select Random Winner", self.select_winner, 'lightyellow'),
            ("Remove Participant", self.remove_participant, 'lightcoral'),
            ("Clear All Participants", self.clear_participants, 'lightsalmon'),
            ("View Winners History", self.view_winners_history, 'lightpink')
        ]

        for text, command, color in buttons:
            tk.Button(
                self.root, 
                text=text, 
                command=command,
                bg=color,
                **button_style
            ).pack(pady=10)

    def add_participant(self):
        name = simpledialog.askstring("Input", "Enter Participant Name:")
        if name and name.strip():
            if name not in self.participants:
                self.participants.append(name.strip())
                messagebox.showinfo("Success", f"{name} added successfully!")
            else:
                messagebox.showwarning("Duplicate", "Participant already exists!")

    def view_participants(self):
        if self.participants:
            participants_list = "\n".join(self.participants)
            messagebox.showinfo("Current Participants", participants_list)
        else:
            messagebox.showinfo("Participants", "No participants added yet!")

    def select_winner(self):
        if len(self.participants) > 0:
            winner = random.choice(self.participants)
            # Record winner with timestamp
            winner_entry = {
                'name': winner, 
                'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            self.winners_history.append(winner_entry)
            messagebox.showinfo("🏆 Winner Selected", f"Congratulations!\n{winner} is the winner!")
        else:
            messagebox.showerror("Error", "Add participants first!")

    def remove_participant(self):
        if self.participants:
            name = simpledialog.askstring("Remove", "Enter participant name to remove:")
            if name in self.participants:
                self.participants.remove(name)
                messagebox.showinfo("Removed", f"{name} removed successfully!")
            else:
                messagebox.showerror("Error", "Participant not found!")
        else:
            messagebox.showinfo("Empty List", "No participants to remove!")

    def clear_participants(self):
        if self.participants:
            confirm = messagebox.askyesno("Confirm", "Are you sure to clear all participants?")
            if confirm:
                self.participants.clear()
                messagebox.showinfo("Cleared", "All participants removed!")
        else:
            messagebox.showinfo("Empty", "No participants to clear!")

    def view_winners_history(self):
        # Create a new window for winners history
        history_window = tk.Toplevel(self.root)
        history_window.title("🏆 Winners History")
        history_window.geometry("400x400")

        # Create a scrolled text widget
        history_text = scrolledtext.ScrolledText(
            history_window, 
            wrap=tk.WORD, 
            width=50, 
            height=20
        )
        history_text.pack(padx=10, pady=10)

        # Populate winners history
        if self.winners_history:
            history_text.insert(tk.END, "🏆 Winners History:\n\n")
            for index, winner in enumerate(self.winners_history, 1):
                history_text.insert(
                    tk.END, 
                    f"{index}. {winner['name']} (on {winner['timestamp']})\n"
                )
        else:
            history_text.insert(tk.END, "No winners yet!")

        # Make text read-only
        history_text.config(state=tk.DISABLED)

    def run(self):
        self.root.mainloop()

# Application Execution
if __name__ == "__main__":
    app = LotteryApp()
    app.run()
