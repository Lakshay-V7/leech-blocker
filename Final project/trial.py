import os


current_directory = os.path.dirname(__file__)
relative_path_to_image = "leechblocker-logo-transparent-backgroung.ico"
image_path = os.path.join(current_directory, relative_path_to_image)
print(image_path)