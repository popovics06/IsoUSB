import os


def write(image, disk):
    os.system("sudo dd if=" + image + " of=" + disk + " status=progress")
    exit()

print("▓▓▓[ IsoUSB ]▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▒▒▒▒▒▒▒▒▒▒░░░░░\n")
print("Please enter the path to disk image file:")
print(" Example: /home/user/Downloads/test.iso\n")
image = input("Location of image file: ")
print()
print("Please enter the path to device (unmounted):")
print(" Example: /dev/sdb\n")
disk = input("Path to disk device: ")
print("\nPlease verify the entered information:")
print("\nImage file:\n " + image)
print("\nDevice:\n " + disk)
print("Enter CONFIRM here to continue:")
test = input("> ")
if test == "CONFIRM":
    write(image, disk)
else:
    print("Verification not complete!")
exit()
