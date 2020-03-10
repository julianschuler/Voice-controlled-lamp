#!/bin/bash

julius/julius/julius -C settings.jconf -dnnconf dnn.jconf > /dev/null 2>&1 &
./voice-control.py
pkill julius
