import sys
import coinchanger.changer as changer


def main():
    if len(sys.argv) < 2:
        print("Please pass an argument")
    else:
        coin_changer = changer.CoinChanger()
        print(coin_changer.calculate(int(sys.argv[1])))


if __name__ == '__main__': main()
