import os

import pykx as kx

print(os.environ.get("QLIC"))
print(kx.q.til(10))
# In case of using .pykx-config file
print(kx.config.pykx_config_locs)
