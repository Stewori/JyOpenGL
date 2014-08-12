'''OpenGL extension NV.shader_atomic_int64

This module customises the behaviour of the 
OpenGL.raw.GL.NV.shader_atomic_int64 to provide a more 
Python-friendly API

The official definition of this extension is available here:
http://www.opengl.org/registry/specs/NV/shader_atomic_int64.txt
'''
from OpenGL import platform, constant, arrays
from OpenGL import extensions, wrapper
import ctypes
from OpenGL.raw.GL import _types, _glgets
from OpenGL.raw.GL.NV.shader_atomic_int64 import *
from OpenGL.raw.GL.NV.shader_atomic_int64 import _EXTENSION_NAME

def glInitShaderAtomicInt64NV():
    '''Return boolean indicating whether this extension is available'''
    from OpenGL import extensions
    return extensions.hasGLExtension( _EXTENSION_NAME )


### END AUTOGENERATED SECTION