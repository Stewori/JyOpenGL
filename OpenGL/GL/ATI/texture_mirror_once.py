'''OpenGL extension ATI.texture_mirror_once

This module customises the behaviour of the 
OpenGL.raw.GL.ATI.texture_mirror_once to provide a more 
Python-friendly API
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL.ATI.texture_mirror_once import *
### END AUTOGENERATED SECTION