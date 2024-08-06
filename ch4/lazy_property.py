import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

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

def main():
    pygame.init()
    display = (800, 600)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)
    glTranslatef(0.0, 0.0, -5)

    obj = ObjectUsingShaderProgram()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

        glUseProgram(obj.shader_program)

        glBegin(GL_TRIANGLES)
        glVertex3f(-1, -1, 0)
        glVertex3f(1, -1, 0)
        glVertex3f(0, 1, 0)
        glEnd()

        glUseProgram(0)

        pygame.display.flip()
        pygame.time.wait(10)

if __name__ == "__main__":
    main()