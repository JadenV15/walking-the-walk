class Rasteriser:
    @staticmethod
    def edge(ax, ay, bx, by, px, py):
        return (
            (px - ax) * (by - ay)
            -
            (py - ay) * (bx - ax)
        )

    @staticmethod
    def draw_triangle(
        framebuffer,
        p0,
        p1,
        p2,
        colour
    ):
        min_x = max(
            0,
            int(min(
                p0[0],
                p1[0],
                p2[0]
            ))
        )

        max_x = min(
            framebuffer.width - 1,
            int(max(
                p0[0],
                p1[0],
                p2[0]
            ))
        )

        min_y = max(
            0,
            int(min(
                p0[1],
                p1[1],
                p2[1]
            ))
        )

        max_y = min(
            framebuffer.height - 1,
            int(max(
                p0[1],
                p1[1],
                p2[1]
            ))
        )

        area = Rasteriser.edge(
            p0[0], p0[1],
            p1[0], p1[1],
            p2[0], p2[1]
        )

        if area == 0:
            return

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                w0 = Rasteriser.edge(
                    p1[0], p1[1],
                    p2[0], p2[1],
                    x, y
                )

                w1 = Rasteriser.edge(
                    p2[0], p2[1],
                    p0[0], p0[1],
                    x, y
                )

                w2 = Rasteriser.edge(
                    p0[0], p0[1],
                    p1[0], p1[1],
                    x, y
                )

                if (
                    (w0 >= 0 and w1 >= 0 and w2 >= 0)
                    or
                    (w0 <= 0 and w1 <= 0 and w2 <= 0)
                ):
                    framebuffer.set_pixel(x, y, colour)

