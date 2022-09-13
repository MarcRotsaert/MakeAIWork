#!/usr/bin/env bash

export LIBGL_ALLOW_SOFTWARE=1
python -m simpylc -s
python simulations/car/world.py