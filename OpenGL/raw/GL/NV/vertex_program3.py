'''OpenGL extension NV.vertex_program3

Overview (from the spec)
	
	This extension, like the NV_vertex_program2_option extension,
	provides additional vertex program functionality to extend the
	standard ARB_vertex_program language and execution environment.
	ARB programs wishing to use this added functionality need only add:
	
	    OPTION NV_vertex_program3;
	
	to the beginning of their vertex programs.
	
	New functionality provided by this extension, above and beyond that
	already provided by NV_vertex_program2_option extension, includes: 
	
	    * texture lookups in vertex programs,
	
	    * ability to push and pop address registers on the stack,
	
	    * address register-relative addressing for vertex attribute and
	      result arrays, and
	
	    * a second four-component condition code.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/NV/vertex_program3.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_vertex_program3'
_DEPRECATED = False



def glInitVertexProgram3NV():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
