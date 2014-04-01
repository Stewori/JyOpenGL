'''OpenGL extension OES.fixed_point

This module customises the behaviour of the 
OpenGL.raw.GL.OES.fixed_point to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/OES/fixed_point.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
from OpenGL.GL import glget
import ctypes
from OpenGL.raw.GL import _types
from OpenGL.raw.GL.OES.fixed_point import *
from OpenGL.raw.GL.OES.fixed_point import _EXTENSION_NAME

def glInitFixedPointOES():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )

### END AUTOGENERATED SECTION