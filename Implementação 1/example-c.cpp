#include <GL/glut.h>

void display() {
    glClear(GL_COLOR_BUFFER_BIT);

    glBegin(GL_QUADS);

    // -----------------------------
    // Quadrado Superior Esquerdo
    // -----------------------------
    glColor3f(0.95f, 0.87f, 0.76f); 
    glVertex2f(-1.0f, 1.0f);

    glColor3f(0.85f, 0.85f, 0.85f);
    glVertex2f(0.0f, 1.0f);

    glColor3f(0.2f, 0.4f, 0.8f);    
    glVertex2f(0.0f, 0.0f);

    glColor3f(0.9f, 0.8f, 0.8f);    
    glVertex2f(-1.0f, 0.0f);

    // -----------------------------
    // Quadrado Superior Direito
    // -----------------------------
    glColor3f(0.85f, 0.85f, 0.85f);
    glVertex2f(0.0f, 1.0f);

    glColor3f(0.9f, 0.8f, 0.7f);
    glVertex2f(1.0f, 1.0f);

    glColor3f(0.9f, 0.5f, 0.0f);
    glVertex2f(1.0f, 0.0f);

    glColor3f(0.2f, 0.4f, 0.8f);
    glVertex2f(0.0f, 0.0f);

    // -----------------------------
    // Quadrado Inferior Esquerdo
    // -----------------------------
    glColor3f(0.9f, 0.8f, 0.8f);    
    glVertex2f(-1.0f, 0.0f);

    glColor3f(0.7f, 0.2f, 0.4f);    
    glVertex2f(0.0f, 0.0f);

    glColor3f(0.5f, 0.1f, 0.2f);   
    glVertex2f(0.0f, -1.0f);

    glColor3f(0.95f, 0.92f, 0.9f); 
    glVertex2f(-1.0f, -1.0f);

    // -----------------------------
    // Quadrado Inferior Direito
    // -----------------------------
    glColor3f(0.7f, 0.2f, 0.4f);   
    glVertex2f(0.0f, 0.0f);

    glColor3f(0.9f, 0.5f, 0.0f);   
    glVertex2f(1.0f, 0.0f);

    glColor3f(1.0f, 1.0f, 1.0f);   
    glVertex2f(1.0f, -1.0f);

    glColor3f(0.7f, 0.7f, 0.9f);    
    glVertex2f(0.0f, -1.0f);

    glEnd();

    glFlush();
}

int main(int argc, char** argv) {
    glutInit(&argc, argv);
    glutInitWindowSize(500, 500);
    glutCreateWindow("Quatro Gradientes");
    glutDisplayFunc(display);
    glutMainLoop();
    return 0;
}
