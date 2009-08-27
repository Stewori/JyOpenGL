'''OpenGL extension GREMEDY.string_marker

Overview (from the spec)
	
	This extension defines a mechanism to insert textual markers into
	the OpenGL stream. 
	
	When debugging or profiling an OpenGL application some of the most
	important tools are stream loggers, which just output a list of the
	called OpenGL commands, and profilers, which show at which points
	the pipeline is bottlenecked for a given part of the frame. The
	problem in using these is that there is a definite loss of
	information between the application and the used debugger/profiler.
	The application generally has a pretty good idea what is rendered
	when (e.g. rendering background, landscape, building, players,
	particle effects, bullets etc.), but the debugger/profiler only
	sees the OpenGL stream. To analyze the stream developers have to
	guess what is done when by following the program code and the log
	output in parallel, which can get difficult for systems that
	restructure their internal pipeline or do lazy changes.
	
	This extension is really only useful for these debuggers and
	profilers, and not for actual drivers. In fact, it is not expected
	that any standard driver would ever implement this extension. The
	main point of having this extension is to allow applications to have a
	clean way of accessing this functionality only when they are run
	under the control of a debugger/profiler, without having to
	recompile or change the application.
	

The official definition of this extension is available here:
	http://oss.sgi.com/projects/ogl-sample/registry/GREMEDY/string_marker.txt

Automatically generated by the get_gl_extensions script, do not edit!
'''
from OpenGL import platform, constants, constant, arrays
from OpenGL import extensions
from OpenGL.GL import glget
import ctypes
EXTENSION_NAME = 'GL_GREMEDY_string_marker'
_DEPRECATED = False

glStringMarkerGREMEDY = platform.createExtensionFunction( 
	'glStringMarkerGREMEDY', dll=platform.GL,
	extension=EXTENSION_NAME,
	resultType=None, 
	argTypes=(constants.GLsizei, ctypes.c_void_p,),
	doc = 'glStringMarkerGREMEDY( GLsizei(len), c_void_p(string) ) -> None',
	argNames = ('len', 'string',),
	deprecated = _DEPRECATED,
)


def glInitStringMarkerGREMEDY():
	'''Return boolean indicating whether this extension is available'''
	return extensions.hasGLExtension( EXTENSION_NAME )
