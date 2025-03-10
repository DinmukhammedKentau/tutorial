booleans=[True,True , True]
print(all(booleans))
print("hello")
"""All деген егер бари True True кайтарады"""
print(all([1, 0, 3]))      # False (өйткені ішінде 0 бар)
print(all([True, False]))  # False (өйткені ішінде False бар)
print(all(['', 'Hello']))  # False (өйткені '' бос жол)
print(all([[], 1]))        # False (өйткені [] бос тізім)
print(all([]))             # True (бос итерируемді объект ерекше жағдай)
