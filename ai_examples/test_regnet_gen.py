from cyclegan import ResNetGenerator
from PIL import Image

from torchvision import transforms
import torch

netG = ResNetGenerator()

model_path = 'data/pich2/horse2zebra_0.4.0.pth'
model_data = torch.load(model_path)
netG.load_state_dict(model_data)
netG.eval()

preprocess = transforms.Compose([transforms.Resize(256),
                                 transforms.ToTensor()])

img = Image.open("data/pich2/horse3.jpg")
img_t = preprocess(img)

batch_t = torch.unsqueeze(img_t, 0)
batch_out = netG(batch_t)

out_t = (batch_out.data.squeeze() + 1.0) / 2.0

out_img = transforms.ToPILImage()(out_t)

# out_img.save('data/p1ch2/zebra.jpg')

out_img.show()
