import os

put = r"C:\Users\Dimash\Documents\pp1"
"""r деген табуляцияны алып тастайды"""
isExist=os.path.exists(put)
print(f"Path {put} is {isExist}")
if isExist:
    print(f"PathName:{os.path.dirname(put)}")
    """os.path.dirname ге дейинги путты шыгарып береди"""
    print(f"Dirname:{os.path.basename(put)}")
    """Dirname нын атынын озин шыгарады"""