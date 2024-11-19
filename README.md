![banner where?](https://github.com/czett/rnarchive/blob/main/assets/banner.png)

# RNArchive

**RNArchive** is a Python application that encodes files into RNA-like sequences and decodes them back to their original form. The program uses a simple mapping of bytes to RNA codons (A, C, G, U) and provides a graphical user interface for ease of use.

---

## Features

- **Encode Files**: Converts any file into an RNA-like sequence stored in `.rna` format.
- **Decode Files**: Restores the original file from an `.rna` archive.
- **GUI Interface**: Simple and intuitive interface using `tkinter`.
- **File Extension Preservation**: Automatically stores and restores the correct file extension.

---

## How It Works

1. **Encoding**: 
   - Each byte of the input file is converted into a unique 4-base RNA codon.
   - The file extension is preserved in the `.rna` archive for proper restoration.

2. **Decoding**: 
   - The `.rna` file is decoded back into its original binary data.
   - The preserved file extension ensures the file is saved with the correct type.

---

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/czett/RNArchive.git
   cd RNArchive
   ```

2. Install Python dependencies (if not already installed):
   - `tkinter` (included with most Python distributions)
   - Standard Python libraries: `os`, `itertools`

---

## Usage

1. Run the application:
   ```bash
   python app.py
   ```

2. Use the graphical interface:
   - **Encoding**:
     1. Click **Upload File** in the "Upload to encode" section.
     2. Enter a name for the `.rna` archive.
     3. Select the destination folder.
   - **Decoding**:
     1. Click **Upload .rna File** in the "Upload .rna to decode" section.
     2. Choose the `.rna` file to decode.
     3. Select the destination folder to save the restored file.

---

## Example

### Encoding
1. Select a file (e.g., `example.txt`).
2. Enter a name (e.g., `example_archive`).
3. Save as `example_archive.rna`.

### Decoding
1. Select `example_archive.rna`.
2. Save the restored file as `decoded_file.txt` (or its original extension).

---

## Error Handling

- If an error occurs during encoding or decoding, an error message will be displayed at the top of the application.
- Ensure the input files are valid and `.rna` files were generated using RNArchive.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details. 
