'''OpenGL extension NV.blend_square

Overview (from the spec)
	
	It is useful to be able to multiply a number by itself in the blending
	stages -- for example, in certain types of specular lighting effects
	where a result from a dot product needs to be taken to a high power.
	
	This extension provides four additional blending factors to permit
	this and other effects: SRC_COLOR and ONE_MINUS_SRC_COLOR for source
	blending factors, and DST_COLOR and ONE_MINUS_DST_COLOR for destination
	blending factors.
	
	Direct3D provides capability bits for advertising these additional
	blend modes.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/NV/blend_square.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_blend_square'
_DEPRECATED = False



def glInitBlendSquareNV():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
