#include <GL/glut.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    // ---------------------------
    // Fundo em gradiente
    // ---------------------------
    glBegin(GL_QUADS);
        glColor3f(0.85f, 0.88f, 0.85f); 
        glVertex2f(-1.0f, 1.0f);
        glVertex2f( 1.0f, 1.0f);

        glColor3f(0.70f, 0.75f, 0.72f); 
        glVertex2f( 1.0f,-1.0f);
        glVertex2f(-1.0f,-1.0f);
    glEnd();

    // ---------------------------
    // Conjunto Esquerdo
    // Triângulo superior (invertido)
    // ---------------------------
    glBegin(GL_TRIANGLES);
        glColor3f(0.4f, 0.1f, 0.1f);
        glVertex2f(-0.8f, 0.6f);

        glColor3f(0.3f, 0.0f, 0.0f); 
        glVertex2f(-0.2f, 0.6f);

        glColor3f(0.25f, 0.1f, 0.2f); 
        glVertex2f(-0.5f, 0.1f);
    glEnd();

    // Triângulo inferior (em pé)
    glBegin(GL_TRIANGLES);
        glColor3f(0.25f, 0.1f, 0.2f);
        glVertex2f(-0.5f, 0.1f);

        glColor3f(0.2f, 0.0f, 0.2f);
        glVertex2f(-0.7f,-0.6f);

        glColor3f(0.3f, 0.0f, 0.2f);
        glVertex2f(-0.3f,-0.6f);
    glEnd();

    // ---------------------------
    // Conjunto Direito
    // Triângulo em pé (vermelho)
    // ---------------------------
    glBegin(GL_TRIANGLES);
        glColor3f(0.9f, 0.1f, 0.1f); 
        glVertex2f(0.0f,-0.2f);

        glColor3f(0.8f, 0.0f, 0.0f); 
        glVertex2f(0.3f,-0.2f);

        glColor3f(0.95f,0.3f, 0.3f); 
        glVertex2f(0.3f, 0.9f);
    glEnd();

    // Triângulo invertido (laranja)
    glBegin(GL_TRIANGLES);
        glColor3f(0.95f, 0.5f, 0.1f); 
        glVertex2f(0.2f,-0.3f);

        glColor3f(0.95f, 0.4f, 0.0f);
        glVertex2f(0.8f,-0.3f);

        glColor3f(0.9f,  0.3f, 0.0f); 
        glVertex2f(0.5f,-0.7f);
    glEnd();

    glFlush();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitWindowSize(500, 500);
    glutCreateWindow("Triângulos com Gradiente");
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
