def name_inventory(firstname, lastname, **kwargs):
    age_collection(**kwargs)
    print(firstname, lastname)

def age_collection(age):
    print("your age ", age)

def main():
    name_inventory(
        firstname = "John",
        lastname = "Brown",
        age = 32
    )

if __name__ == "__main__":
    main()