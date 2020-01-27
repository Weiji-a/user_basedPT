# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import user_based__PT

# <codecell>

example=user_based__PT.dataset('../data/Nantes/')
example.select_days()
example.parent_stations()
example.routes()
example.shortest_paths()
example.heatmap()

# <codecell>


