import argparse
import codecs

ap = argparse.ArgumentParser()
ap.add_argument("-i", "--input", required=True, help="path to input file in Stanford format")
ap.add_argument("-o", "--output", required=True, help="path to output file in IOB format")
args = ap.parse_args()

fin = codecs.open(args.input, "r", "utf8")
fout = codecs.open(args.output, "w", "utf8")

last = "O"
for line in fin.readlines():
    line = line.strip()
    cols = line.split("\t")
    if len(cols) > 0:
        label = cols[-1]
        if label != "O":
            cols[-1] = ("I-" if label == last else "B-") + cols[-1]
        last = label
        line = "\t".join(cols)
    else:
        last = "O"
    fout.write(line + "\n")

fin.close()
fout.close()
