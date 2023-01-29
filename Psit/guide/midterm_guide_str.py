"""test"""
def main():
    """test"""
    txt = 'Hello World'
        #  0123456789...
    print(txt.center(30, ' '))   #(จองพื้นที่, แสดงที่เหลือ)
    print(txt.ljust(30, '-'))
    print(txt.rjust(30, '*'))
    print()

    print(txt.endswith('d'))    #(จบด้วยอะไร)
    print(txt.endswith('D'))
    print(txt.startswith('H'))  #(เริ่มด้วยอะไร)
    print()

    print(txt.find('l'))        #บอกตำแหน่งตัวที่หา ตัวแรกทางซ้าย
    print(txt.rfind('l'))       #บอกตำแหน่งตัวที่หา ตัวแรกทางขวา
    print(txt.find('l', 5, 10)) #หาจากตำแหน่งที่ 5 ถึง 10 (หา, เริ่ม, จบ)
    print(txt.index('l', 2))    #หาจากตำแหน่งที่ 7 จนจบ เหมือน find แต่ถ้าไม่เจอจะ error
    print()

    txt1 = 'Hello123'
    txt2 = '1234'
    txt3 = ' '
    print(txt1.isalnum())       #เป็น [ตัวเลขกับตัวอักษร] ทั้งหมดไหม True/False
    print(txt1.isalpha())       #เป็น [ตัวอักษร] ทั้งหมดไหม True/False
    print(txt2.isdigit())       #เป็น [ตัวเลข] ทั้งหมดไหม
    print(txt2.isdecimal())
    print(txt2.isnumeric())
    print(txt.islower())        #เป็น [อักษรพิมพ์เล็ก] ทั้งหมดไหม
    print(txt.isupper())        #เป็น [อักษรพิมพ์ใหญ่] ทั้งหมดไหม
    print(txt3.isspace())       #เป็น [ช่องว่าง] ทั้งหมดไหม
    print(txt.istitle())        #คำในแต่ละช่วงขึ้นต้นด้วยพิมพ์ใหญ่ >> This Is Test Title
    print()

    txt1 = 'Helloooo'
    txt2 = '    Hello     '
    print(txt.lower())          #แปลงเป็นพิมพ์เล็ก
    print(txt.upper())          #แปลงเป็นพิมพ์ใหญ่
    print(txt1.strip('o'))      #ดึงตัวซ้ายสุด/ขวาสุดออก
    print(txt2.strip(' '))      #ห้ามใช้ในการสอบ ;-;
    print()

    print(txt.replace('l', '1', 2)) #(ค่าเก่า, ค่าใหม่, จำนวนที่จะเปลี่ยน)
    print(txt.swapcase())           #สลับพิมพ์เล็กพิมพ์ใหญ่
    print(txt.title())              #แปลงเป็นรูปแบบ title ขึ้นต้นพิมพ์ใหญ่ในแต่ละช่วง
    print()
main()
