import itertools
from tkinter import *
import tkinter.filedialog as fd

BASES = ['A', 'C', 'G', 'U']
CODONS = [''.join(p) for p in itertools.product(BASES, repeat=4)]  # 4 bases, not three to cover more options
BYTE_TO_CODON = {i: CODONS[i] for i in range(256)}
CODON_TO_BYTE = {v: k for k, v in BYTE_TO_CODON.items()}

def file_to_rna(filepath):
    with open(filepath, 'rb') as f:
        data = f.read()  # read the file in bytes
    rna_sequence = ''.join(BYTE_TO_CODON[b] for b in data)
    return rna_sequence

def rna_to_file(rna_sequence, output_path):
    byte_chunks = [rna_sequence[i:i+4] for i in range(0, len(rna_sequence), 4)]
    data = bytes(CODON_TO_BYTE[codon] for codon in byte_chunks)
    with open(output_path, 'wb') as f:
        f.write(data)

# # encode


# # decode


def decode_handler() -> None:
    archive = fd.askopenfilename(title="Select file to decode", filetypes=[("RNArchives", ".rna")])
    dest_dir = fd.askdirectory(parent=root, title="Choose destination directory")

    with open(archive, 'r') as f:
        rna_seq = f.read()
    
    rna_to_file(rna_seq, f'{dest_dir}/new_beamng.???')

def encode_handler() -> None:
    encode_file = fd.askopenfilename(title="Select file to convert")
    dest_dir = fd.askdirectory(parent=root, title="Choose destination directory")

    rna_seq = file_to_rna(encode_file)
    with open(f'{dest_dir}/output.rna', 'w') as f:
        f.write(rna_seq)

root = Tk()
root.title("RNArchive")
root.geometry("500x300")

title = Label(text="RNArchive")
title.pack(pady=20)
title["font"] = "Arial 20 bold"

msg_lbl = Label(text="вефивухфеоивуе", fg="#f00")
msg_lbl["font"] = "Segoe-UI 20 bold"
msg_lbl.pack(pady=0)

encode_label = Label(text="upload to encode")
encode_label.pack(pady=10)
encode_label["font"] = "Arial 12 bold"

btn_encode = Button(text="upload file", command=encode_handler)
btn_encode["font"] = "Arial 16"
btn_encode.pack(pady=0)

decode_label = Label(text="upload .rna to decode")
decode_label.pack(pady=20)
decode_label["font"] = "Arial 12 bold"

btn_decode = Button(text="upload .rna file", command=decode_handler)
btn_decode["font"] = "Arial 16"
btn_decode.pack(pady=0)

root.mainloop()