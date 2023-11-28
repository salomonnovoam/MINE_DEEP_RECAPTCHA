#%%

# model.save('yolo_model')
from ultralytics import YOLO
import os
curr_path = os.getcwd()
import matplotlib.pyplot as plt
#%matplotlib inline
#%%


# %%



# %%
#test_image=os.path.join("juan-pablo-garcia-marruecosjpg.jpeg")
#test_image=os.path.join("descarga_3.webp")
#test_image=os.path.join("WhatsApp Image 2023-11-27 at 19.01.11.jpeg")
#test_image=os.path.join("download.jpeg")

#test_image


# %%

def get_prediction(image_path):
    model2 = YOLO('train47/weights/best.pt')  # load a custom model
    img = plt.imread(image_path)
    imgplot = plt.imshow(img)
    plt.show()
    res = model2(image_path)
    res_plotted = res[0].plot()
    plt.imshow(res_plotted)
    plt.title("Image with predictions", fontsize = 40)
    plt.xticks([])
    plt.yticks([])
    plt.show()
    return res_plotted

#%%
# test_image=os.path.join("download.jpeg")
# get_prediction(test_image)
#
##%%
#
## Predict
#res = model2(test_image)
#res_plotted = res[0].plot()
#
## Display image with predictions
#plt.imshow(res_plotted)
#plt.title("Image with predictions", fontsize = 40)
#plt.xticks([])
#plt.yticks([])

# %%
