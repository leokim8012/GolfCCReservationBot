import argparse

from utils import config


def reservataion(input_args):

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--id',
        required=True,
        help='PRETRAINED or TRAIN',
    )

    parser.add_argument(
        '--reservationDate',
        required=True,
        help='The GAN type',
    )
    parser.add_argument(
        '--reservationTime',
        required=True,
        help='The GAN type',
    )
    args = parser.parse_args()

    if(args.exp == 'TRAIN'):
      run_training(args)
    elif(args.exp == 'PRETRAINED'):
      run_pretrained(args)
    elif(args.exp == 'GIF'):
      makeGIF(args)
      


if __name__ == '__main__':
    main()