import logging
import math

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def calculate_triangle(side_a: str, side_b: str, side_c: str):

    try:
        a = float(side_a)
        b = float(side_b)
        c = float(side_c)
    except (ValueError, TypeError):
        logger.error("Получены нечисловые данные")
        return "", [(-2, -2), (-2, -2), (-2, -2)]

    if (
        not math.isfinite(a)
        or not math.isfinite(b)
        or not math.isfinite(c)
        or a <= 0
        or b <= 0
        or c <= 0
    ):
        logger.error("Стороны должны быть положительными числами")
        return "не треугольник", [(-1, -1), (-1, -1), (-1, -1)]

    if a + b <= c or a + c <= b or b + c <= a:
        logger.warning("Треугольник с такими сторонами не существует")
        return "не треугольник", [(-1, -1), (-1, -1), (-1, -1)]

    if a == b and b == c:
        triangle_type = "равносторонний"
    elif a == b or a == c or b == c:
        triangle_type = "равнобедренный"
    else:
        triangle_type = "разносторонний"

    x1 = 0.0
    y1 = 0.0

    x2 = a
    y2 = 0.0

    x3 = (a * a + b * b - c * c) / (2 * a)

    y3_squared = b * b - x3 * x3

    if y3_squared < 0:
        y3_squared = 0

    y3 = math.sqrt(y3_squared)

    points = [
        (x1, y1),
        (x2, y2),
        (x3, y3)
    ]
    max_x = max(x for x, y in points)
    max_y = max(y for x, y in points)

    scale_x = 99 / max_x if max_x > 0 else 1
    scale_y = 99 / max_y if max_y > 0 else 1

    scale = min(scale_x, scale_y, 1.0)

    points = [
        (x * scale, y * scale)
        for x, y in points
    ]

    min_x = min(x for x, y in points)
    max_x = max(x for x, y in points)

    min_y = min(y for x, y in points)
    max_y = max(y for x, y in points)

    offset_x = (99 - (max_x - min_x)) / 2 - min_x
    offset_y = (99 - (max_y - min_y)) / 2 - min_y

    coordinates = [
        (
            int(round(x + offset_x)),
            int(round(y + offset_y))
        )
        for x, y in points
    ]

    logger.info("Тип треугольника: %s", triangle_type)
    logger.info("Координаты вершин: %s", coordinates)

    return triangle_type, coordinates


# Запуск программы
if __name__ == "__main__":
    side_a = input("Введите сторону A: ")
    side_b = input("Введите сторону B: ")
    side_c = input("Введите сторону C: ")

    triangle_type, coordinates = calculate_triangle(
        side_a,
        side_b,
        side_c
    )

    print("Тип треугольника:", triangle_type)
    print("Координаты вершин:", coordinates)