import sys
import logging


def main():
    logging.debug('test')
    logging.info('we are here now')
    logging.warning('is when this event was logged.')


if __name__ == "__main__":
    print('You are running {script}'.format(script=sys.argv[0]))
    loglevel = str(sys.argv[1]).upper()
    logging.basicConfig(format='%(asctime)s %(levelname)s:\t%(message)s',
                        datefmt='%m/%d/%Y %I:%M:%S %p',
                        level=loglevel)
    main()
