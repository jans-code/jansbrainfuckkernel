#!/usr/bin/env python
from ipykernel.kernelapp import IPKernelApp
from .kernel import jansbrainfuckkernel
IPKernelApp.launch_instance(kernel_class=jansbrainfuckkernel)
