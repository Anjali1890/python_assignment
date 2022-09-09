# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# created by anjali dabholkar on 08/09/2022
# function to compare two version
def version_comp(ver1, ver2):
    vers_1 = ver1.split(".") # split by '.'
    vers_2 = ver2.split(".")
    vers_1 = [int(i) for i in vers_1] # convert into integer
    vers_2 = [int(i) for i in vers_2]

    for i in range(len(vers_1)):
        if vers_1[i] > vers_2[i]:
            return 1
        elif vers_2[i] > vers_1[i]:
            return -1
    return 0

    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    version1 = "1.2.9.9.9.9"
    version2 = "1.3"
    ans = version_comp(version1, version2)
    if ans < 0:
        print(version1 + " is smaller")
    elif ans > 0:
        print(version2 + " is smaller")
    else:
        print("Both versions are equal")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
