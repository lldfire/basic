import numpy as np
import pandas as pd


class Point:
    """
    经纬度类，更方便快捷的使用每个点的 lon 和 lng
    """

    def __init__(self, lng='', lat=''):
        self.lng = lng
        self.lat = lat

    def show(self):
        print([self.lng, self.lat])


class IsPointInBorders:
    """
    判断点是否在某个边界范围内
    point: [longitude, latitude]
    border_sets: [[longitude, latitude],……]
    """

    def __init__(self, lng, lat, border_sets):
        self.point = Point(lng, lat)
        self.border_sets = [Point(lng, lat) for lon, lat in border_sets]

    def getPolygonBounds(self):
        """
        闭合边界的最大外接矩形
        ： return list
        """
        top = down = left = right = self.border_sets[0]

        for item in self.border_sets[1:]:
            if item.lng > top.lng:
                top = item
            elif item.lng < down.lng:
                down = item
            else:
                pass

            if item.lat > right.lat:
                right = item
            elif item.lat < left.lat:
                left = item
            else:
                pass

        point0 = Point(top.lng, left.lat)    # 最大的经度，最小维度
        point1 = Point(top.lng, right.lat)     # 最大经度，最大维度
        point2 = Point(down.lng, right.lat)    # 最小经度，最大维度
        point3 = Point(down.lng, left.lat)    # 最小经度，最小维度
        return [point0, point1, point2, point3]

    def isPointInRect(slef, point, polygonBounds):
        """判断点是否在最大外接矩形内"""
        if point.lng >= polygonBounds[3].lng and point.lng <= polygonBounds[0].lng and point.lat >= polygonBounds[3].lat and point.lat <= polygonBounds[2].lat:
            return True
        else:
            return False

    def isPointsInPolygons(self):
        """
        判断某个点是否在闭合边界内
        """
        # 求最大外接矩形
        polygonBounds = self.getPolygonBounds()
        # 判断是否在外包矩形内，如果不在，直接返回false
        if not self.isPointInRect(self.point, polygonBounds):
            return 0

        length = len(self.border_sets)
        p = self.point
        p1 = self.border_sets[0]
        flag = False
        for i in range(1, length):
            p2 = self.border_sets[i]
            # 点与多边形顶点重合，则表示点在边界内
            if (p.lng == p1.lng and p.lat == p1.lat) or (p.lng == p2.lng and p.lat == p2.lat):
                return 1
            # 判断线段两端点是否在射线两侧
            if (p2.lat < p.lat and p1.lat >= p.lat) or (p2.lat >= p.lat and p1.lat < p.lat):
                # 线段上与射线 Y 坐标相同的点的 X 坐标
                if (p2.lat == p1.lat):
                    x = (p1.lng + p2.lng)/2
                else:
                    x = p2.lng - (p2.lat - p.lat) * \
                        (p2.lng - p1.lng)/(p2.lat - p1.lat)
                # 点在多边形的边上
                if (x == p.lng):
                    return 1
                # 射线穿过多边形的边界
                if (x > p.lng):
                    flag = not flag
                else:
                    pass
            else:
                pass
            p1 = p2

        if flag:
            return 1


def one_point(lng, lat, border_sets):
    """对某一个点进行判断"""
    size = len(np.array(border_sets).shape)
    if size == 2:
        ipib = IsPointInBorders(lng, lat, border_sets)
        return ipib.isPointsInPolygons()

    elif size == 3:
        for border_set in border_sets:
            ipib = IsPointInBorders(lng, lat, border_sets)
            if ipib.isPointsInPolygons() == 1:
                return 1
        else:
            return 0

    else:
        raise TypeError('border_sets 类型格式不符合要求！')


def many_point(data, border_sets, path='./result.csv'):
    """
    多个点，批量判断
    data: pandas.DataFrame, 经纬度的列名需设置为：lng, lat
    """
    data['isinborder'] = data.apply(
        lambda x: one_point(x.lng, x.lat, border_sets), axis=1
    )

    # 保存结果
    data[data['isinborder'] == 1].to_csv(path, index=False)


if __name__ == '__main__':
    """
    使用说明：
    需要：1.待测点（可以是单个点，也可以是多个点）；2.多边形边界顶点集，形状如下：
    [[lng, lat], [lng, lat],……]
    """
    # 使用样例一：批量处理
    # 读取边界经纬度信息，将经纬度转化为列表
    borders = pd.read_csv(r'temp\corde.txt', header=None, names=['lng', 'lat'])
    border_sets = np.array([borders.lng.tolist(), borders.lat.tolist()]).T

    # 待处理的文件目录
    # data_path = r'C:\Users\86132\Desktop\jupyter\temp\城西科创大走廊矢量文件-shp\old.csv'

    # data = pd.read_csv(data_path, usecols=[1, 2], nrows=10000)
    # 替换经纬度列名，如下
    # data.columns = ['lat', 'lng']
    # 调用函数批量处理文件，并指定保存的文件夹
    # many_point(data, border_sets, save_path='./result.csv')

    # 使用样例二：处理单个点
    # point = [119.716833, 30.258643]
    # print(one_point(point[0], point[1], border_sets))
    print(border_sets[:5])
    