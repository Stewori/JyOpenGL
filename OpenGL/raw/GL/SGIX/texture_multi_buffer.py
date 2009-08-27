'''OpenGL extension SGIX.texture_multi_buffer

Overview (from the spec)
	
	This extension provides an API for the application to specify that
	the OpenGL should handle multiple textures in such a way that,
	wherever possible, a texture definition or redefinition can occur
	in parallel with rendering that uses a different texture.
	
	The texture_object extension allows the simultaneous definition
	of multiple textures; any texture that is not being used for 
	rendering can, in principle, have its definition or operations
	in its definition (e.g. downloading to hardware) occur in parallel
	with the use of another texture. This is true as long as all
	redefinitions strictly follow any use of the previous definition.
	
	Conceptually this is similar to frame buffer double-buffering,
	except that the intent here is to simply provide a hint to the
	OpenGL to promote such double-buffering if and wherever possible.
	The effect of such a hint is to speed up operations without
	affecting the result. The user on any particular system must be
	knowledgable and prepared to accept any trade-offs which follow
	from such a hint.
	
	GL_FASTEST in this context means that texture multi-buffering
	is being used whenever possible to improve performance. 
	Generally, textures that are adjacent in a sequence of multiple
	texture definitions have the greatest chance of being in 
	different buffers. The number of buffers available at any time
	depends on various factors, such as the machine being used and
	the textures' internal formats.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/SGIX/texture_multi_buffer.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_SGIX_texture_multi_buffer'
_DEPRECATED = False
GL_TEXTURE_MULTI_BUFFER_HINT_SGIX = constant.Constant( 'GL_TEXTURE_MULTI_BUFFER_HINT_SGIX', 0x812E )


def glInitTextureMultiBufferSGIX():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
