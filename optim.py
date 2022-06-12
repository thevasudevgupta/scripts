import deepspeed
from tqdm.auto import tqdm
import sys

command = sys.argv[1]

x = torch.ones(2, 10000)
model = nn.Linear(10000, 30000).to("cuda")

if command == "fused":
  print("using fused")
  optim = deepspeed.ops.adam.FusedAdam(model.parameters())
else:
  print("using torch")
  optim = torch.optim.Adam(model.parameters())

for _ in tqdm(range(10000)):
    loss = model(x.to("cuda")).mean()
    loss.backward()
    optim.step()
