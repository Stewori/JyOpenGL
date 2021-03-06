'''OpenGL extension NV.viewport_array2

This module customises the behaviour of the 
OpenGL.raw.GLES2.NV.viewport_array2 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/viewport_array2.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GLES2 import _types, _glgets
from OpenGL.raw.GLES2.NV.viewport_array2 import *
from OpenGL.raw.GLES2.NV.viewport_array2 import _EXTENSION_NAME

def glInitViewportArray2NV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION