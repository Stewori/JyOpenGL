'''OpenGL extension EXT.index_material

Overview (from the spec)
	
	This extends color index lighting to include a way for the current
	index to contribute to the color index produced by lighting.  This
	works much like ColorMaterial does for RGBA lighting by allowing
	one or more color index material properties to be attached to the
	current index.
	
	The color index lighting formula is also modified so that the lit
	color index may be bitwise shifted in order to allow greater control
	when using lighting and fog together in color index mode.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/index_material.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_index_material'
_DEPRECATED = False
GL_INDEX_MATERIAL_EXT = constant.Constant( 'GL_INDEX_MATERIAL_EXT', 0x81B8 )
GL_INDEX_MATERIAL_PARAMETER_EXT = constant.Constant( 'GL_INDEX_MATERIAL_PARAMETER_EXT', 0x81B9 )
GL_INDEX_MATERIAL_FACE_EXT = constant.Constant( 'GL_INDEX_MATERIAL_FACE_EXT', 0x81BA )
glIndexMaterialEXT = platform.createExtensionFunction( 
	'glIndexMaterialEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLenum,),
	doc = 'glIndexMaterialEXT( GLenum(face), GLenum(mode) ) -> None',
	argNames = ('face', 'mode',),
	deprecated = _DEPRECATED,
)


def glInitIndexMaterialEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
