'''OpenGL extension ARB.fragment_shader

Overview (from the spec)
	
	This extension adds functionality to define fragment shader objects. A
	fragment shader object is a shader object (see the ARB_shader_objects
	extension) that, when attached to a program object, can be compiled and
	linked to produce an executable that runs on the fragment processor in
	OpenGL. The fragment processor is a programmable unit that replaces the
	OpenGL 1.4 fixed-function texturing, color sum and fog stages. This
	extension also defines how such an executable interacts with the fixed
	functionality fragment processing of OpenGL 1.4. The language used to
	write fragment shaders is not discussed here. That language is defined
	in the OpenGL Shading Language specification as the Fragment Shading
	Language.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/ARB/fragment_shader.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_ARB_fragment_shader'
_DEPRECATED = False
GL_FRAGMENT_SHADER_ARB = constant.Constant( 'GL_FRAGMENT_SHADER_ARB', 0x8B30 )
GL_MAX_FRAGMENT_UNIFORM_COMPONENTS_ARB = constant.Constant( 'GL_MAX_FRAGMENT_UNIFORM_COMPONENTS_ARB', 0x8B49 )
glget.addGLGetConstant( GL_MAX_FRAGMENT_UNIFORM_COMPONENTS_ARB, (1,) )
GL_FRAGMENT_SHADER_DERIVATIVE_HINT_ARB = constant.Constant( 'GL_FRAGMENT_SHADER_DERIVATIVE_HINT_ARB', 0x8B8B )
glget.addGLGetConstant( GL_FRAGMENT_SHADER_DERIVATIVE_HINT_ARB, (1,) )


def glInitFragmentShaderARB():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
