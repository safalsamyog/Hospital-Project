from PIL import Image
#resizing the image
xx=input('enter name: ')
image=Image.open("hospital/{}.png".format(xx))

print("The current size of image",image.size)

height=int(input("enter height: "))#input of height and width
width=int(input("enter width: "))
image.thumbnail((height,width))#thubnail function takes tuples
name=input("enter file name to save: ")
image.save("hospital/{}.png".format(name))
print("sucessfully created file name ",name)


