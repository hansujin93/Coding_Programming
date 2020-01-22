from math import sqrt

class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect_x(self):
        return (self.x, -1 * self.y)

    def slope_from_origin(self):
        if self.x == 0:
            return 0
        return self.y / self.x

    def get_line_to(self, target):
        if self.x == target.x:
            return (0, 0)
        else:
            self.a = (target.y - self.y) / (target.x - self.x)
            self.b = self.y - self.a * self.x
            return (self.a, self.b)

    def get_length(self, target):
        self.leng_x = sqrt((target.x - self.x) ** 2)
        self.leng_y = sqrt((target.y - self.y) ** 2)
        return (self.leng_x, self.leng_y)

    def get_line_through_mid(self, target):
        self.mid_x = (target.x + self.x) / 2
        self.mid_y = (target.y + self.y) / 2
        if self.x == target.x:
            self.inverse_slope = 0
        else:
            self.inverse_slope = (target.y - self.y) / (target.x - self.x)
        self.inverse_slope = -1 / self.inverse_slope
        self.bias = self.mid_y - self.inverse_slope * self.mid_x
        return (self.inverse_slope, self.bias)

    @staticmethod  #simulate function based on different parameter system from __init__
    def midpoint(p1, p2, p3, p4):
        P1, P2, P3, P4 = Point(p1[0], p1[1]), Point(p2[0], p2[1]), Point(p3[0], p3[1]), Point(p4[0], p4[1])
        L1_slope = P1.get_line_to(P2)[0]
        L2_slope = P3.get_line_to(P4)[0]
        L1_length = P1.get_length(P2)
        L2_length = P3.get_length(P4)

        if L1_slope == L2_slope:
            if L1_length == L2_length:  # rectangle
                center_x = (p1[0] + p2[0] + p3[0] + p4[0]) / 4
                center_y = (p1[1] + p2[1] + p3[1] + p4[1]) / 4
                return (center_x, center_y)
            else:
                center_x = round((P2.get_line_through_mid(P4)[1] - P1.get_line_through_mid(P3)[1]) / (P1.get_line_through_mid(P3)[0] - P2.get_line_through_mid(P4)[0]),2)
                center_y = round(P1.get_line_through_mid(P3)[0] * center_x + P1.get_line_through_mid(P3)[0],2)
                return (center_x, center_y)
        center_x = round((P3.get_line_through_mid(P4)[1] - P1.get_line_through_mid(P2)[1]) / (P1.get_line_through_mid(P2)[0] - P3.get_line_through_mid(P4)[0]), 2)
        center_y = round(P1.get_line_through_mid(P2)[0] * center_x + P1.get_line_through_mid(P2)[1], 2)
        if center_x == -0.00:
            center_x = 0.00
        else:
            pass
        return (center_x, center_y)
