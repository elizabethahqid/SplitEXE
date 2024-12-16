import os
from tkinter import Tk, filedialog, messagebox, Label, Button, Entry


class SplitEXE:
    def __init__(self, master):
        self.master = master
        self.master.title("SplitEXE - EXE File Splitter")
        self.master.geometry("400x200")

        self.file_label = Label(master, text="Select EXE File:")
        self.file_label.pack(pady=5)

        self.file_entry = Entry(master, width=40)
        self.file_entry.pack(pady=5)

        self.browse_button = Button(master, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=5)

        self.size_label = Label(master, text="Enter Chunk Size (in MB):")
        self.size_label.pack(pady=5)

        self.size_entry = Entry(master, width=10)
        self.size_entry.pack(pady=5)

        self.split_button = Button(master, text="Split File", command=self.split_file)
        self.split_button.pack(pady=10)

        self.status_label = Label(master, text="", fg="green")
        self.status_label.pack(pady=5)

    def browse_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Executable Files", "*.exe")])
        if file_path:
            self.file_entry.delete(0, "end")
            self.file_entry.insert(0, file_path)

    def split_file(self):
        file_path = self.file_entry.get()
        chunk_size_mb = self.size_entry.get()

        if not os.path.isfile(file_path):
            messagebox.showerror("Error", "Invalid file path.")
            return

        if not chunk_size_mb.isdigit():
            messagebox.showerror("Error", "Chunk size must be a valid number.")
            return

        chunk_size = int(chunk_size_mb) * 1024 * 1024
        output_dir = os.path.join(os.path.dirname(file_path), "SplitChunks")
        os.makedirs(output_dir, exist_ok=True)

        try:
            with open(file_path, "rb") as f:
                index = 1
                while chunk := f.read(chunk_size):
                    chunk_file = os.path.join(output_dir, f"part{index:03}.exe")
                    with open(chunk_file, "wb") as chunk_f:
                        chunk_f.write(chunk)
                    index += 1

            self.status_label.config(text="File split successfully!", fg="green")
            messagebox.showinfo("Success", f"File split into {index - 1} parts.\nSaved in: {output_dir}")

        except Exception as e:
            self.status_label.config(text="Failed to split file.", fg="red")
            messagebox.showerror("Error", f"An error occurred: {e}")


if __name__ == "__main__":
    root = Tk()
    app = SplitEXE(root)
    root.mainloop()
