import sys
from itertools import accumulate
import bisect
sys.stdin = open('./day9/input.txt', 'r')
sys.stdout = open('./day9/output.txt', 'a')
def aoc_1():
    g = []
    try:
        while True:
            s = input().split(',')
            g.append(list(map(int, s)))
    except EOFError:
        pass
    res = 0
    for i in range(len(g)):
        for j in range(i +  1, len(g)):
            res = max(res, abs((g[i][0]  -  g[j][0] + 1) * (g[i][1]  -  g[j][1] + 1)) )
    print(res)

from functools import lru_cache
from itertools import combinations

def point_on_segment(px, py, x1, y1, x2, y2, eps=1e-12):
    # 判断点(px,py)是否在线段(x1,y1)-(x2,y2)上（包含端点）
    dx1 = x2 - x1
    dy1 = y2 - y1
    dx2 = px - x1
    dy2 = py - y1
    cross = dx1 * dy2 - dy1 * dx2
    if abs(cross) > eps:
        return False
    dot = dx1 * dx2 + dy1 * dy2
    if dot < -eps:
        return False
    len2 = dx1 * dx1 + dy1 * dy1
    if dot > len2 + eps:
        return False
    return True


def point_in_polygon(point, polygon, include_boundary=True):
    """
    判定点是否在简单多边形内。
    Args:
        point: (x, y)
        polygon: [(x0,y0), (x1,y1), ..., (xn-1,yn-1)]，首尾不必重复
        include_boundary: True -> 边界视为 "inside"
    Returns:
        True if inside (or on boundary when include_boundary True), else False
    """
    x, y = point
    n = len(polygon)
    if n < 3:
        return False

    # 边界检测
    for i in range(n):
        x1, y1 = polygon[i]
        x2, y2 = polygon[(i + 1) % n]
        if point_on_segment(x, y, x1, y1, x2, y2):
            return include_boundary

    # 射线法（水平向右）
    inside = False
    for i in range(n):
        xi, yi = polygon[i]
        xj, yj = polygon[(i + 1) % n]
        # 检查边与水平线 y 是否有交叉，使用半开半闭规则避免顶点重算
        intersect = ((yi > y) != (yj > y))
        if intersect:
            # 计算交点 x 坐标： x_inter = xi + (y - yi) * (xj - xi) / (yj - yi)
            if (yj - yi) == 0:
                continue  # horizontal, skip
            x_inter = xi + (y - yi) * (xj - xi) / (yj - yi)
            if x_inter > x:
                inside = not inside
    return inside

def segment_intersect(seg1_x1, seg1_y1, seg1_x2, seg1_y2, seg2_x1, seg2_y1, seg2_x2, seg2_y2):
    # 假设一个水平一个垂直
    # 确定哪个是垂直，哪个是水平
    if seg1_x1 == seg1_x2:
        if seg2_x1 == seg2_x2:
            return False  # both vertical
        v_x1, v_y1, v_x2, v_y2 = seg1_x1, seg1_y1, seg1_x2, seg1_y2
        h_x1, h_y1, h_x2, h_y2 = seg2_x1, seg2_y1, seg2_x2, seg2_y2
    else:
        if seg2_y1 == seg2_y2:
            return False  # both horizontal
        v_x1, v_y1, v_x2, v_y2 = seg2_x1, seg2_y1, seg2_x2, seg2_y2
        h_x1, h_y1, h_x2, h_y2 = seg1_x1, seg1_y1, seg1_x2, seg1_y2
    # 检查严格相交
    return (min(v_y1, v_y2) < h_y1 < max(v_y1, v_y2) and
            min(h_x1, h_x2) < v_x1 < max(h_x1, h_x2))


def seg_intersect_sides(x1, y1, x2, y2, points):
    n = len(points)
    for i in range(n):
        x3, y3 = points[i]
        x4, y4 = points[(i + 1) % n]
        if segment_intersect(x1, y1, x2, y2, x3, y3, x4, y4):
            return True
    return False

def aoc_2():
    g = []
    try:
        while True:
            s = input().strip().split(',')
            g.append((int(s[0]), int(s[1])))
    except EOFError:
        pass
    res = 0
    for p1, p2 in combinations(g, 2):
        xi, yi = p1
        xj, yj = p2
        min_x, max_x = min(xi, xj), max(xi, xj)
        min_y, max_y = min(yi, yj), max(yi, yj)
        area = (max_x - min_x + 1) * (max_y - min_y + 1)
        if area <= res:
            continue
        corners = [(min_x, min_y), (max_x, min_y), (max_x, max_y), (min_x, max_y)]
        if all(point_in_polygon(c, g) for c in corners):
            rect_sides = [
                (corners[0], corners[1]),
                (corners[1], corners[2]),
                (corners[2], corners[3]),
                (corners[3], corners[0])
            ]
            intersects = any(
                seg_intersect_sides(s[0][0], s[0][1], s[1][0], s[1][1], g)
                for s in rect_sides
            )
            if not intersects:
                res = area
    print(res)

aoc_2()