import argparse
import corpus


def convert_io2bio(labels):
    new_labels = []
    last_label = "O"
    for label in labels:
        label = label[2:] if label[:2] == "I-" else label
        if label == "O":
            new_labels.append("O")
        else:
            new_labels.append(("B-" if label != last_label else "I-") + label)
        last_label = label
    assert len(labels) == len(new_labels)
    return new_labels


def main(args):
    sentences = corpus.read_dataset(args.input)
    sentences = [(tokens, convert_io2bio(labels)) for tokens, labels in sentences]
    corpus.write_dataset(args.output, sentences)


def parse_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--input", required=True, help="path to input file in Stanford format")
    ap.add_argument("--output", required=True, help="path to output file in IOB format")
    return ap.parse_args()


if __name__ == "__main__":
    cli_args = parse_args()
    print("Command Line Args:", cli_args)
    main(cli_args)
