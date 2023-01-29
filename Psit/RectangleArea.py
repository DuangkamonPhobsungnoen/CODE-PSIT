""" RectangleArea """
def main(area_x, area_y):
    """ ฟังก์ชั่น RectangleArea """
    l1_x, l2_x = int(area_x[0]), int(area_y[0]) #จุดตามแกนx (10, 40)
    l1_y, l2_y = int(area_x[1]), int(area_y[1]) #จุดตามแกนy (10, 10)
    r1_x, r2_x = (int(area_x[0])+int(area_x[2])), (int(area_y[0])+int(area_y[2])) #แกน X (90, 120)
    r1_y, r2_y = (int(area_x[1])+int(area_x[3])), (int(area_y[1])+int(area_y[3])) #แกน y (110, 110)
    code_x = (min(r1_x, r2_x)-max(l1_x, l2_x))
    code_y = (min(r1_y, r2_y)-max(l1_y, l2_y))
    if code_x > 0 and code_y > 0:
        area_overlapping = code_x * code_y
        print(area_overlapping)
    else:
        print('no overlapping')
main(input().split(), input().split())
