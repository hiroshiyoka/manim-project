from manim import *

class Geometry(Scene):
    def construct(self):
        # Animasi Opening
        opening = Tex("HELLO WORLD!", color=YELLOW).scale(1)
        text1 = MarkupText(f'My name is <span fgcolor="{RED}">Raka Fadilah</span>', color=WHITE, font_size=38)
        text2 = MarkupText(f'I am gonna talk about <span fgcolor="{TEAL_C}">Geometry</span>.', color=WHITE, font_size=38)
        check_it = Tex("Let's check it out!", color=BLUE_D).scale(1)
        mob = Circle(radius=4, color=TEAL_A)
        self.wait(1)
        self.play(Write(opening))
        self.wait(2)
        self.play(Unwrite(opening, reverse=False))
        self.wait(0.5)
        self.play(Write(text1))
        self.wait(3)
        self.play(ReplacementTransform(text1, text2))
        self.wait(3)
        self.play(Unwrite(text2, reverse=False))
        self.wait(1)
        self.play(Write(check_it))
        self.wait(1)
        self.play(Broadcast(mob))
        self.wait(1)
        self.play(FadeOut(check_it, shift=DOWN, scale=1.0))
        self.wait(0.5)
        
        # Animasi Bentuk Geometri
        line = Line(start=[-3, 0, 0], end=[3, 0, 0], color=BLUE)
        circle = Circle(radius=1, color=RED)
        triangle = Polygon([-2, -1, 0], [0, 1, 0], [2, -1, 0], color=GREEN)
        rectangle = Rectangle(height=2, width=4, color=YELLOW)
        self.play(Create(line), run_time=2)
        self.wait(0.5)
        self.play(Create(circle), run_time=2)
        self.wait(0.5)
        self.play(Create(triangle), run_time=2)
        self.wait(0.5)
        self.play(Create(rectangle), run_time=2)
        self.wait(0.5)
        
        # Teks Penjelasan
        penjelasan_geometri = Tex("Geometry is a branch of mathematics that studies the shapes, sizes, and properties of figures and spaces.", color=WHITE).scale(0.75)
        penjelasan_geometri1 = Tex("It involves understanding the relationships between points, lines, angles, and geometric shapes such as triangles, squares, and circles.", color=WHITE).scale(0.75)
        penjelasan_geometri2 = Tex("Geometry is used to measure, compare, and model real-world objects.", color=WHITE).scale(0.75)
        penjelasan_garis = Tex("A line is a geometric object that consists of infinitely many points extending in a particular direction.", color=WHITE).scale(0.75)
        penjelasan_lingkaran = Tex("A circle is a set of all points on a plane that are equidistant from a fixed point called the center.", color=YELLOW).scale(0.75)
        penjelasan_segitiga = Tex("A triangle is a polygon with three sides and three angles.", color=BLUE).scale(0.75)
        penjelasan_persegi = Tex("A rectangle is a polygon with four angles that form right angles and has both length and width.", color=RED).scale(0.75)
        # Teks next to
        penjelasan_geometri1.next_to(penjelasan_geometri, DOWN)
        penjelasan_geometri2.next_to(penjelasan_geometri1, DOWN)
        
        # Animasi Penjelasan Geometri
        objects = VGroup(line, circle, triangle, rectangle)
        self.wait(0.5)
        objects.generate_target()
        objects.target.shift(UP * 2)
        self.add(objects)
        self.play(MoveToTarget(objects))
        self.play(Write(penjelasan_geometri), Write(penjelasan_geometri1), Write(penjelasan_geometri2))
        self.wait(10)
        self.play(FadeOut(objects, shift=UP), FadeOut(penjelasan_geometri, shift=DOWN), FadeOut(penjelasan_geometri1, shift=DOWN), FadeOut(penjelasan_geometri2, shift=DOWN))
        self.wait(0.5)
        
        # Animasi Penjelasan Garis
        line = Line(start=[-3, 0, 0], end=[3, 0, 0], color=BLUE)
        self.play(Create(line), run_time=2)
        line.generate_target()
        line.target.set_fill(color=BLUE, opacity=0.5)
        line.target.shift(UP * 2)
        self.add(line)
        self.play(MoveToTarget(line))
        self.play(Write(penjelasan_garis))
        self.wait(5)
        self.play(FadeOut(line, shift=UP), FadeOut(penjelasan_garis, shift=DOWN))
        self.wait(0.5)
        
        # Animasi Penjelasan Lingkaran
        circle = Circle(radius=1, color=RED)
        self.play(Create(circle), run_time=2)
        circle.generate_target()
        circle.target.set_fill(color=RED, opacity=0.5)
        circle.target.shift(UP * 2)
        self.add(circle)
        self.play(MoveToTarget(circle))
        self.play(Write(penjelasan_lingkaran))
        self.wait(5)
        self.play(FadeOut(circle, shift=UP), FadeOut(penjelasan_lingkaran, shift=DOWN))
        self.wait(0.5)
        
        # Animasi Penjelasan Segitiga
        triangle = Polygon([-2, -1, 0], [0, 1, 0], [2, -1, 0], color=GREEN)
        self.play(Create(triangle), run_time=2)
        triangle.generate_target()
        triangle.target.set_fill(color=GREEN, opacity=0.5)
        triangle.target.shift(UP * 2)
        self.add(triangle)
        self.play(MoveToTarget(triangle))
        self.play(Write(penjelasan_segitiga))
        self.wait(5)
        self.play(FadeOut(triangle, shift=UP), FadeOut(penjelasan_segitiga, shift=DOWN))
        self.wait(0.5)
        
        # Animasi Penjelasan Persegi
        rectangle = Rectangle(height=2, width=4, color=YELLOW)
        self.play(Create(rectangle), run_time=2)
        rectangle.generate_target()
        rectangle.target.set_fill(color=YELLOW, opacity=0.5)
        rectangle.target.shift(UP * 2)
        self.add(rectangle)
        self.play(MoveToTarget(rectangle))
        self.play(Write(penjelasan_persegi))
        self.wait(5)
        self.play(FadeOut(rectangle, shift=UP), FadeOut(penjelasan_persegi, shift=DOWN))
        self.wait(0.5)
        
        # Animasi Geometri Terakhir
        last_text = Tex("And this is a Geometry.", color=WHITE).scale(1)
        self.play(Write(last_text))
        last_text.generate_target()
        last_text.target.shift(UP * 2)
        self.play(MoveToTarget(last_text))
        self.wait()
        dot = Dot(3 * UR, color=BLACK)
        line = Line(color=BLUE)
        circle = Circle(color=RED)
        triangle = Triangle(color=GREEN)
        rectangle = Rectangle(color=YELLOW)
        VGroup(line, circle, triangle, rectangle).set_x(0).arrange(buff=1)
        self.add(dot)
        self.play(GrowFromPoint(line, ORIGIN), run_time=2)
        self.play(GrowFromPoint(circle, [-2, 2, 0]), run_time=2)
        self.play(GrowFromPoint(triangle, [3, -2, 0]), run_time=2)
        self.play(GrowFromPoint(rectangle, dot), run_time=2)
        self.wait(0.5)
        objects = VGroup(line, circle, triangle, rectangle)
        self.play(FadeOut(objects, shift=DOWN), FadeOut(last_text, shift=UP))
        self.wait(0.5)
        
        # Transisi Terakhir
        text_closing = Tex("That's all about Geometry.", color=WHITE).scale(0.75)
        text_closing1 = Tex("Hopefully, this explanation about geometry can be useful.", color=ORANGE).scale(0.75)
        text_closing1.next_to(text_closing, DOWN)
        self.play(Write(text_closing))
        self.wait()
        self.play(Write(text_closing1))
        self.wait(4)
        self.play(FadeOut(text_closing, shift=UP), FadeOut(text_closing1, shift=DOWN))
        self.wait()
        
        # Closing
        closing = Tex("Thanks for watching.", color=BLUE_D).scale(1)
        self.play(Write(closing))
        self.wait(1)
        self.play(Broadcast(mob))
        self.play(FadeOut(closing, shift=DOWN, scale=1.0))
        self.wait(0.5)