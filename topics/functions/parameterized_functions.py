def my_name(fname):
    print(f"{fname}")


my_name("Ensar")


def full_name(firstname, lastname):
    print(firstname,lastname)

full_name("Ensar","Yildirim")


def my_name2(**kwargs):
    print("My real name is " + kwargs["name1"])

my_name2(name1="Murat",name2="Ensar",name3="Busra")