import argparse

from utils import config
from utils import booker
from utils import chromedriver


def reservation(input_args):
  reservationConfig = input_args.config
  configs = config.read_config(reservationConfig)

  driver = chromedriver.createChormeDriver()
  booker.reservataion(driver, configs)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '--config',
        required=True,
        help='configs 폴더 확인.',
    )

    # parser.add_argument(
    #     '--reservationTime',
    #     required=True,
    #     help='The GAN type',
    # )
    args = parser.parse_args()

    reservation(args)
      


if __name__ == '__main__':
    main()