import torch
import numpy as np

values = np.random.rand(1, 1, 161, 980)
tensor = torch.Tensor(values)
tensor.requires_grad=True
print(tensor)
