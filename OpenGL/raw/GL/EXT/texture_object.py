'''OpenGL extension EXT.texture_object

Overview (from the spec)
	
	This extension introduces named texture objects.  The only way to name
	a texture in GL 1.0 is by defining it as a single display list.  Because
	display lists cannot be edited, these objects are static.  Yet it is
	important to be able to change the images and parameters of a texture.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/EXT/texture_object.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_EXT_texture_object'
_DEPRECATED = False
GL_TEXTURE_PRIORITY_EXT = constant.Constant( 'GL_TEXTURE_PRIORITY_EXT', 0x8066 )
GL_TEXTURE_RESIDENT_EXT = constant.Constant( 'GL_TEXTURE_RESIDENT_EXT', 0x8067 )
GL_TEXTURE_1D_BINDING_EXT = constant.Constant( 'GL_TEXTURE_1D_BINDING_EXT', 0x8068 )
glget.addGLGetConstant( GL_TEXTURE_1D_BINDING_EXT, (1,) )
GL_TEXTURE_2D_BINDING_EXT = constant.Constant( 'GL_TEXTURE_2D_BINDING_EXT', 0x8069 )
glget.addGLGetConstant( GL_TEXTURE_2D_BINDING_EXT, (1,) )
GL_TEXTURE_3D_BINDING_EXT = constant.Constant( 'GL_TEXTURE_3D_BINDING_EXT', 0x806A )
glget.addGLGetConstant( GL_TEXTURE_3D_BINDING_EXT, (1,) )
glAreTexturesResidentEXT = platform.createExtensionFunction( 
	'glAreTexturesResidentEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=constants.GLboolean, 
	argTypes=(constants.GLsizei, arrays.GLuintArray, ctypes.POINTER(constants.GLboolean),),
	doc = 'glAreTexturesResidentEXT( GLsizei(n), GLuintArray(textures), POINTER(constants.GLboolean)(residences) ) -> constants.GLboolean',
	argNames = ('n', 'textures', 'residences',),
	deprecated = _DEPRECATED,
)

glBindTextureEXT = platform.createExtensionFunction( 
	'glBindTextureEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLenum, constants.GLuint,),
	doc = 'glBindTextureEXT( GLenum(target), GLuint(texture) ) -> None',
	argNames = ('target', 'texture',),
	deprecated = _DEPRECATED,
)

glDeleteTexturesEXT = platform.createExtensionFunction( 
	'glDeleteTexturesEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLsizei, arrays.GLuintArray,),
	doc = 'glDeleteTexturesEXT( GLsizei(n), GLuintArray(textures) ) -> None',
	argNames = ('n', 'textures',),
	deprecated = _DEPRECATED,
)

glGenTexturesEXT = platform.createExtensionFunction( 
	'glGenTexturesEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLsizei, arrays.GLuintArray,),
	doc = 'glGenTexturesEXT( GLsizei(n), GLuintArray(textures) ) -> None',
	argNames = ('n', 'textures',),
	deprecated = _DEPRECATED,
)

glIsTextureEXT = platform.createExtensionFunction( 
	'glIsTextureEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=constants.GLboolean, 
	argTypes=(constants.GLuint,),
	doc = 'glIsTextureEXT( GLuint(texture) ) -> constants.GLboolean',
	argNames = ('texture',),
	deprecated = _DEPRECATED,
)

glPrioritizeTexturesEXT = platform.createExtensionFunction( 
	'glPrioritizeTexturesEXT', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLsizei, arrays.GLuintArray, arrays.GLclampfArray,),
	doc = 'glPrioritizeTexturesEXT( GLsizei(n), GLuintArray(textures), GLclampfArray(priorities) ) -> None',
	argNames = ('n', 'textures', 'priorities',),
	deprecated = _DEPRECATED,
)


def glInitTextureObjectEXT():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
