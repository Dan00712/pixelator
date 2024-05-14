import argparse
import pixelator.util as putil
import sys
from PIL import Image


def main():
    parser = argparse.ArgumentParser(
        prog="pixelator",
        description="a utility to pixelate an image",
    )
    parser.add_argument('input_file', type=argparse.FileType('rb'), default='-')
    parser.add_argument('-o', '--output_file', type=argparse.FileType("wb"), default='-')
    parser.add_argument('-r', '--rows', type=int, default=20)
    parser.add_argument('-c', '--column', type=int, default=20)
    
    args = parser.parse_args()
    
    inp = Image.open(args.input_file)
    outp = putil.pixelate_image(inp,
                            row_pixels=args.rows,
                            col_pixels=args.column
                        )
    outp.save(args.output_file)
    


if __name__ == "__main__":
    main()

