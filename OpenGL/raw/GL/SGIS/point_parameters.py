'''OpenGL extension SGIS.point_parameters

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/SGIS/point_parameters.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIS_point_parameters'
_DEPRECATED = False
GL_POINT_SIZE_MIN_SGIS = constant.Constant( 'GL_POINT_SIZE_MIN_SGIS', 0x8126 )
GL_POINT_SIZE_MAX_SGIS = constant.Constant( 'GL_POINT_SIZE_MAX_SGIS', 0x8127 )
GL_POINT_FADE_THRESHOLD_SIZE_SGIS = constant.Constant( 'GL_POINT_FADE_THRESHOLD_SIZE_SGIS', 0x8128 )
GL_DISTANCE_ATTENUATION_SGIS = constant.Constant( 'GL_DISTANCE_ATTENUATION_SGIS', 0x8129 )
glPointParameterfSGIS = platform.createExtensionFunction( 
	'glPointParameterfSGIS', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLfloat,),
	doc = 'glPointParameterfSGIS( GLenum(pname), GLfloat(param) ) -> None',
	argNames = ('pname', 'param',),
	deprecated = _DEPRECATED,
)

glPointParameterfvSGIS = platform.createExtensionFunction( 
	'glPointParameterfvSGIS', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, arrays.GLfloatArray,),
	doc = 'glPointParameterfvSGIS( GLenum(pname), GLfloatArray(params) ) -> None',
	argNames = ('pname', 'params',),
	deprecated = _DEPRECATED,
)


def glInitPointParametersSGIS():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
