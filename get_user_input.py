


def show(alist):
    for i , p in enumerate(alist):
        print(i+1 ,')' , p)


def get_brand():
    print("please enter the brand of your laptop : ")
    brands = ['asus' , 'hp' , 'lenovo' , 'porsche' , 'microsoft' , 'acer' , 'apple' , 'dell' , 'gigabyte' ]
    show(brands)
    return brands[int(input()) - 1]

def get_cache():
    print("please enter the cache memory : 2 - 16 ")
    return int(input())

def get_GraphicM():
    print("please enter the graphic memory : " )
    return int(input())

def get_processor():
    print("Please enter your processor : " )
    processors = ['AMD '  , 'Intel']
    show(processors)
    return processors[int(input()) - 1]

def get_Graphic():
    print("please enter your grahpic card model ")
    graphics = [' Intel '  , ' NVIDIA ' , 'AMD ']
    show(graphics)
    return graphics[int(input()) - 1]

def get_sprocessor():
    print("please enter your seri procesoor : ")
    sprocessors = [' Celeron ' , ' Pentium ' , ' Ryzen 3 '  , ' Core i3 ' ,
     ' Core i7 ' ,' Ryzen 5 ' ,' Core i5 ' ,' Bristol Ridge ' ,' Ryzen 7 ' , ' Xeon ' ,' Carrizo ' ]
    show(sprocessors)
    return sprocessors[int(input()) - 1]

def get_ram():
    print("please enter ram memory : ")
    return int(input())
