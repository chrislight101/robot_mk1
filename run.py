import sys
from Core.System import System


def main():
    try:
        system = System()
        system.run()

    except:
        ex_type, ex_value, traceback = sys.exc_info()
        print("Exception in main: %s %s" % (ex_type, ex_value))

    finally:
        pass


if __name__ == '__main__':
    main()
