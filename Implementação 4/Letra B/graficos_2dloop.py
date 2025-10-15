import cairo
import math

WIDTH, HEIGHT = 600, 600
surface = cairo.ImageSurface(cairo.FORMAT_ARGB32, WIDTH, HEIGHT)
ctx = cairo.Context(surface)

ctx.set_source_rgb(1, 1, 1) 
ctx.paint()

def desenhar_grade(ctx, x_start, y_start, square_size, rows, cols, padding):
    cores = [
        (1.0, 0.0, 0.0), (1.0, 0.5, 0.0), (1.0, 1.0, 0.0),
        (0.0, 1.0, 0.0), (0.5, 1.0, 0.0), (0.5, 1.0, 1.0), 
        (0.0, 0.0, 1.0), (0.5, 0.5, 1.0), (1.0, 0.5, 1.0)
    ]

    for i in range(rows):
        for j in range(cols):
            x = x_start + j * (square_size + padding)
            y = y_start + i * (square_size + padding)
            cor_index = i * cols + j
            r, g, b = cores[cor_index]
            ctx.set_source_rgb(r, g, b)
            ctx.rectangle(x, y, square_size, square_size)
            ctx.fill()

def desenhar_barras(ctx, x_start, y_base, bar_width, gap, heights):
    cores = [
        (0.0, 0.0, 1.0), (0.0, 0.4, 1.0), (0.0, 0.6, 1.0), (0.0, 0.9, 1.0)
    ]

    for i, height in enumerate(heights):
        x = x_start + i * (bar_width + gap)
        y = y_base - height 
        r, g, b = cores[i % len(cores)]
        ctx.set_source_rgb(r, g, b)
        ctx.rectangle(x, y, bar_width, height)
        ctx.fill()

def desenhar_concentricos(ctx, center_x, center_y, num_squares, start_size, step):
    ctx.set_line_width(2)
    cores = [
        (1.0, 0.8, 0.0), (1.0, 0.6, 0.0), (1.0, 0.4, 0.0),
        (1.0, 0.2, 0.0), (1.0, 0.0, 0.0)
    ]

    for i in range(num_squares):
        size = start_size + i * step 
        x = center_x - size / 2
        y = center_y - size / 2
        
        if i < len(cores):
            r, g, b = cores[len(cores) - 1 - i]
        else:
            r, g, b = (0, 0, 0.5)

        ctx.set_source_rgb(r, g, b)
        ctx.rectangle(x, y, size, size)
        ctx.stroke()


desenhar_grade(ctx, 50, 50, 40, 3, 3, 10)

bar_heights = [200, 150, 100, 50]
desenhar_barras(ctx, 300, 500, 30, 15, bar_heights)

desenhar_concentricos(ctx, 450, 100, 5, 40, 30)

surface.write_to_png("graficos_letra_b.png")
print("Desenho salvo em graficos_letra_b.png")