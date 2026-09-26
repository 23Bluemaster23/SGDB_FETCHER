import requests
from PIL import Image

from configuration.constants import IMAGE_TYPE


def download_image(url:str,type:int):
    size = [100,100]
    file_name:str = 'image.jpg'
    if type == IMAGE_TYPE.COVERTART:
        size = [264,352]
        file_name = 'super' + '.jpg'
    elif type == IMAGE_TYPE.BANNER:
        size = [184,69]
        file_name = 'duper' + '.jpg'
    elif type == IMAGE_TYPE.ICON:
        size = [128,128]
        file_name = 'ultra' + '.png'
    data = requests.get(url,stream=True).raw
    image = Image.open(fp =data)
    image = image.resize(size)
    image.save(file_name)

# if __name__ == '__main__':
#     download_image("https://media.geeksforgeeks.org/wp-content/uploads/20221014220743/karma.png",IMAGE_TYPE.ICON)
