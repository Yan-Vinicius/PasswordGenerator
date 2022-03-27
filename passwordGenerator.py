import random
import string

def main():

    chars = string.ascii_letters + string.digits + 'ç!@#$%&*()-+='

    rnd = random.SystemRandom()
    size = input("Digite o tamanho da senha que deseja: ")
    print("A senha gerada foi:")
    print("".join(rnd.choice(chars) for i in range(int(size))))

if __name__ == "__main__":
    main()