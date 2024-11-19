import itertools
from tkinter import *
import tkinter.filedialog as fd
import os

BASES = ['A', 'C', 'G', 'U']
CODONS = [''.join(p) for p in itertools.product(BASES, repeat=4)]
BYTE_TO_CODON = {i: CODONS[i] for i in range(256)}
CODON_TO_BYTE = {v: k for k, v in BYTE_TO_CODON.items()}

def msg(msg : str) -> None:
    msg_lbl.configure(text=msg)
  
def file_to_rna(filepath):
    file_extension = os.path.splitext(filepath)[1]
    with open(filepath, 'rb') as f:
        data = f.read()
    rna_sequence = ''.join(BYTE_TO_CODON[b] for b in data)
    return f"{file_extension}|{rna_sequence}"

def rna_to_file(rna_sequence, output_path):
    file_extension, rna_sequence = rna_sequence.split('|', 1)
    byte_chunks = [rna_sequence[i:i+4] for i in range(0, len(rna_sequence), 4)]
    data = bytes(CODON_TO_BYTE[codon] for codon in byte_chunks)
    output_file = os.path.join(output_path, f"decoded_file{file_extension}")
    with open(output_file, 'wb') as f:
        f.write(data)

def decode_handler() -> None:
    try:
        archive = fd.askopenfilename(title="Select file to decode", filetypes=[("RNArchives", ".rna")])
        dest_dir = fd.askdirectory(parent=root, title="Choose destination directory")

        with open(archive, 'r') as f:
            rna_seq = f.read()
        
        rna_to_file(rna_seq, dest_dir)
    except:
        msg("decoding error")

def encode_handler() -> None:
    try:
        encode_file = fd.askopenfilename(title="Select file to convert")
        dest_dir = fd.askdirectory(parent=root, title="Choose destination directory")

        rna_seq = file_to_rna(encode_file)
        with open(f'{dest_dir}/{archive_name.get()}.rna', 'w') as f:
            f.write(rna_seq)
    except:
        msg("encoding error")

root = Tk()
root.title("RNArchive")
root.geometry("500x400")

title = Label(text="RNArchive")
title.pack(pady=20)
title["font"] = "Arial 20 bold"

msg_lbl = Label(text="", fg="#f00")
msg_lbl["font"] = "Segoe-UI 20 bold"
msg_lbl.pack(pady=0)

encode_label = Label(text="Upload to encode")
encode_label.pack(pady=10)
encode_label["font"] = "Arial 12 bold"

archive_name = Entry()
archive_name.insert(0, "Enter archive name")
archive_name["font"] = "Arial 14"
archive_name.pack(pady=10)

btn_encode = Button(text="Upload file", command=encode_handler)
btn_encode["font"] = "Arial 16"
btn_encode.pack(pady=0)

decode_label = Label(text="Upload .rna to decode")
decode_label.pack(pady=20)
decode_label["font"] = "Arial 12 bold"

btn_decode = Button(text="Upload .rna file", command=decode_handler)
btn_decode["font"] = "Arial 16"
btn_decode.pack(pady=0)

root.mainloop()