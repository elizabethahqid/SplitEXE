# SplitEXE - EXE File Splitter

**SplitEXE** is a user-friendly tool designed to split large executable files (`.exe`) into smaller chunks. It allows you to specify the chunk size, making it easy to manage large EXE files for distribution or storage.

---

## Features
- **Intuitive GUI**: Built with a simple, clean interface for easy use.
- **Customizable Chunk Size**: Specify chunk size in MB according to your needs.
- **Automatic Output Organization**: Splits files into a designated folder (`SplitChunks`).

---

## How to Use
1. Run the `splitexe.py` script.
2. Use the "Browse" button to select the `.exe` file you want to split.
3. Enter the chunk size (in MB) in the provided input box.
4. Click "Split File" to start splitting the executable.
5. The split files will be saved in a new folder named `SplitChunks` located in the same directory as the original file.

---

## Requirements
- Python 3.7 or later
- Required Python packages:
  - `tkinter` (usually included in Python by default)

---

## License
This project is open-source and available under the MIT License.

---

## Troubleshooting
- **Invalid File Path**: Ensure the selected file exists and is an `.exe`.
- **Invalid Chunk Size**: Make sure the chunk size is a positive number in MB.

For any issues or questions, feel free to reach out!
