def main():
    name = get_name()
    house = get_house()
    print(f"{name} from {house}")

def get_name():#abstraction
    name = input("Name: ")
    return name

def get_house():
    house = input("House: ")
    return house

if __name__ == "__main__":
    main()