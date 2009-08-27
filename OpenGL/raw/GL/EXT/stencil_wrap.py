'''OpenGL extension EXT.stencil_wrap

Overview (from the spec)
	
	Various algorithms use the stencil buffer to "count" the number of
	surfaces that a ray passes through.  As the ray passes into an object,
	the stencil buffer is incremented.  As the ray passes out of an object,
	the stencil buffer is decremented.
	
	GL requires that the stencil increment operation clamps to its maximum
	value.  For algorithms that depend on the difference between the sum
	of the increments and the sum of the decrements, clamping causes an
	erroneous result.
	
	This extension provides an enable for both maximum and minimum wrapping
	of stencil values.  Instead, the stencil value wraps in both directions.
	
	Two additional stencil operations are specified.  These new operations
	are similiar to the existing INCR and DECR operations, but they wrap
	their result instead of saturating it.  This functionality matches
	the new stencil operations introduced by DirectX 6.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/stencil_wrap.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_stencil_wrap'
_DEPRECATED = False
GL_INCR_WRAP_EXT = constant.Constant( 'GL_INCR_WRAP_EXT', 0x8507 )
GL_DECR_WRAP_EXT = constant.Constant( 'GL_DECR_WRAP_EXT', 0x8508 )


def glInitStencilWrapEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
