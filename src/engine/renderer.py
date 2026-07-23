import math

from engine.vector import Vec3
from engine.mesh import Mesh
from engine.rasteriser import Rasteriser

class Renderer:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.focal_length = 400

    def project(self, vertex):
        z = vertex.z + 5

        if z <= 0.1:
            return None

        x = (
            vertex.x *
            self.focal_length /
            z
        )

        y = (
            vertex.y *
            self.focal_length /
            z
        )

        screen_x = int(self.width / 2 + x)
        screen_y = int(self.height / 2 - y)

        return (screen_x, screen_y)

    def render_mesh(
        self,
        framebuffer,
        mesh,
        angle
    ):
        transformed_vertices = []

        cos_a = math.cos(angle)
        sin_a = math.sin(angle)

        for vx, vy, vz in mesh.vertices:
            x = (
                vx * cos_a
                - vz * sin_a
            )

            z = (
                vx * sin_a
                + vz * cos_a
            )

            transformed_vertices.append(
                Vec3(
                    x,
                    vy,
                    z
                )
            )

        projected = [
            self.project(v)
            for v in transformed_vertices
        ]
    
        triangles = []

        for face in mesh.faces:
            i0, i1, i2 = face

            p0 = projected[i0]
            p1 = projected[i1]
            p2 = projected[i2]

            if (p0 is None or p1 is None or p2 is None):
                continue

            cross = (
                (p1[0] - p0[0])
                *
                (p2[1] - p0[1])
                -
                (p1[1] - p0[1])
                *
                (p2[0] - p0[0])
            )

            if cross >= 0:
                continue

            depth = (
                transformed_vertices[i0].z
                +
                transformed_vertices[i1].z
                +
                transformed_vertices[i2].z
            ) / 3

            triangles.append((depth, p0, p1, p2))

        triangles.sort(key=lambda t: t[0], reverse=True)

        for _, p0, p1, p2 in triangles:
            Rasteriser.draw_triangle(
                framebuffer,
                p0,
                p1,
                p2,
                (180, 180, 220)
            )

