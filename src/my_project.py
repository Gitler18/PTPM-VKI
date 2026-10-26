import logging
import math

EPS = 1e-9

logging.basicConfig(
    filename="log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    encoding="utf-8"
)

logger = logging.getLogger(__name__)


def calculate_triangle(side_a: str, side_b: str, side_c: str):
    try:
        a = float(side_a)
        b = float(side_b)
        c = float(side_c)
    except ValueError:
        logger.error("Стороны должны быть числами")
        return "не треугольник", [(-1, -1), (-1, -1), (-1, -1)]

    if a <= EPS or b <= EPS or c <= EPS:
        logger.error("Стороны должны быть положительными числами")
        return "не треугольник", [(-1, -1), (-1, -1), (-1, -1)]

    if a + b - c <= EPS or a + c - b <= EPS or b + c - a <= EPS:
        logger.warning("Треугольник с такими сторонами не существует")
        return "не треугольник", [(-1, -1), (-1, -1), (-1, -1)]

    x1, y1 = 0.0, 0.0
    x2, y2 = a, 0.0
    x3 = (b ** 2 + a ** 2 - c ** 2) / (2 * a)
    y_squared = b ** 2 - x3 ** 2

    if y_squared < 0:
        y_squared = 0
    y3 = math.sqrt(y_squared)

    coordinates = [(round(x1, 4), round(y1, 4)),
                   (round(x2, 4), round(y2, 4)),
                   (round(x3, 4), round(y3, 4))]

    sides = sorted([a, b, c])
    is_right = abs(sides[0] ** 2 + sides[1] ** 2 - sides[2] ** 2) <= EPS
    is_equilateral = (abs(a - b) <= EPS) and (abs(b - c) <= EPS)
    is_isosceles = (abs(a - b) <= EPS) or (abs(b - c) <= EPS) or (abs(a - c) <= EPS)

    if is_equilateral:
        triangle_type = "равносторонний"
    elif is_right and is_isosceles:
        triangle_type = "равнобедренный прямоугольный"
    elif is_right:
        triangle_type = "прямоугольный"
    elif is_isosceles:
        triangle_type = "равнобедренный"
    else:
        triangle_type = "разносторонний"

    return triangle_type, coordinates