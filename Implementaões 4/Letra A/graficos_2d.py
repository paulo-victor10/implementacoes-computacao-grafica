import cairo
import math

WIDTH, HEIGHT = 400, 350
OUTPUT_FILE = "carranca_geometrica.png"

surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
cr = cairo.Context(surface)

def draw_arrow(cr, x, y, length, width, r, g, b, rotation=0.0):
    
    cr.save() 
    cr.translate(x, y) 
    cr.rotate(rotation)  
    cr.set_source_rgb(r, g, b)
    
    rect_width = length * 0.7
    rect_height = width * 0.4 
    
    rect_x_start = -length / 2.0
    
    cr.rectangle(rect_x_start, -rect_height / 2.0, rect_width, rect_height)
    
    tri_x_base = rect_x_start + rect_width 
    tri_x_tip = -rect_x_start 
    
    cr.move_to(tri_x_base, -width / 2.0)    
    cr.line_to(tri_x_tip, 0.0)             
    cr.line_to(tri_x_base, width / 2.0)    
    cr.close_path()
    
    cr.fill()

    cr.restore()

cr.set_source_rgb(1.0, 1.0, 0.9)
cr.paint()

cr.set_source_rgb(0.5, 0.3, 0.5)
cr.rectangle(130, 75, 140, 180) 
cr.fill() 

cr.set_source_rgb(1.0, 1.0, 1.0) 
cr.arc(160, 120, 25, 0, 2 * math.pi) 
cr.fill() 

cr.set_source_rgb(0.0, 0.0, 0.0) 
cr.arc(160, 120, 15, 0, 2 * math.pi)
cr.fill()

cr.set_source_rgb(1.0, 1.0, 1.0) 
cr.arc(240, 120, 25, 0, 2 * math.pi)
cr.fill() 

cr.set_source_rgb(0.0, 0.0, 0.0) 
cr.arc(240, 120, 15, 0, 2 * math.pi)
cr.fill()

cr.set_source_rgb(1.0, 0.7, 0.8) 
cr.move_to(130, 140)    
cr.line_to(130, 200)    
cr.line_to(185, 150)    
cr.close_path()
cr.fill()

cr.set_source_rgb(1.0, 0.7, 0.8) 
cr.move_to(270, 140)    
cr.line_to(270, 200)    
cr.line_to(215, 150)    
cr.close_path()
cr.fill()

RAIO_SEMICIRCULO = 35
CENTRO_X = 200
CENTRO_SEMI_Y = 215 

cr.set_source_rgb(0.9, 0.4, 0.4) 

cr.arc(
    CENTRO_X, 
    CENTRO_SEMI_Y, 
    RAIO_SEMICIRCULO, 
    0,            
    math.pi       
)

cr.close_path()
cr.fill()

draw_arrow(cr, 200, 160, 100, 40, 1.0, 0.6, 0.5, rotation = math.pi / 2) 

surface.write_to_png(OUTPUT_FILE)

print(f"Imagem '{OUTPUT_FILE}' gerada com sucesso! \n =p Merecemos +1 ponto pela criatividade ;) ")