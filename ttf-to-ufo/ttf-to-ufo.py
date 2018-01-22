#! /usr/bin/env python
import argparse
import defcon
import extractor

def create_arg_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", help = "input filename")
    parser.add_argument("--output", help = "output filename")
    args = parser.parse_args()
    print('inputfile: ', args.input)
    print('outputfile: ', args.output)
    return args

if __name__ == "__main__":
    args = create_arg_parser()
    ttf_path = args.input
    ufo_path = args.output
    print('ttf_path: ', ttf_path)
    print('ufo_path', ufo_path)
    # Make UFO
    ufo = defcon.Font()
    extractor.extractUFO(ttf_path, ufo)
    ufo.save(ufo_path)
