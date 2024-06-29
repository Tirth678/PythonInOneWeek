# Write a program which finds out whether a given name is present in a list or not.
def check_name_in_list(name, name_list):
    if name in name_list:
        print(f"{name} exists in the list.")
    else:
        print(f"{name} does not exist in the list.")


my_list = ["Alice", "Bob", "Charlie", "David"]
given_name = "Charlie"
check_name_in_list(given_name, my_list)
