'''OpenGL extension NV.vertex_program2_option

Overview (from the spec)
	
	This extension provides additional vertex program functionality
	to extend the standard ARB_vertex_program language and execution
	environment.  ARB programs wishing to use this added functionality
	need only add:
	
	    OPTION NV_vertex_program2;
	
	to the beginning of their vertex programs.
	
	The functionality provided by this extension, which is roughly
	equivalent to that provided by the NV_vertex_program2 extension,
	includes:
	
	  * general purpose dynamic branching,
	
	  * subroutine calls,
	
	  * data-dependent conditional write masks,
	
	  * programmable user clip distances,
	
	  * address registers with four components (instead of just one),
	
	  * absolute value operator on scalar and swizzled operand loads,
	
	  * rudimentary address register math,
	
	  * SIN and COS trigonometry instructions, and
	
	  * fully orthogonal "set on" instructions, including a "set sign"
	    instruction.

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/NV/vertex_program2_option.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_NV_vertex_program2_option'
_DEPRECATED = False



def glInitVertexProgram2OptionNV():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
