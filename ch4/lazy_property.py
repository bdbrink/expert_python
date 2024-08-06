import OpenGL.GL as gl
from OpenGL.GL import shaders
from functools import wraps

def lazy_property(func):
    attr_name = '_lazy_' + func.__name__

    @wraps(func)
    def wrapper(self):
        if not hasattr(self, attr_name):
            setattr(self, attr_name, func(self))
        return getattr(self, attr_name)

    return property(wrapper)

class ObjectUsingShaderProgram(object):
    vertex = """
    layout(location = 0) in vec4 vertexPosition;
    void main(){
        gl_Position = vertexPosition;
    }
    """
    
    fragment = """
        out lowp vec4 out_color;
        void main(){
            out_color = vec4(1,1,1,1);
        }
    """

    @lazy_property
    def shader_program(self):
        vertex_shader = shaders.compileShader(self.vertex, gl.GL_VERTEX_SHADER)
        fragment_shader = shaders.compileShader(self.fragment, gl.GL_FRAGMENT_SHADER)
        return shaders.compileProgram(vertex_shader, fragment_shader)
