try:
 with open("file.txt", "r") as file:
    lines = file.readlines()
    print(len(lines))
except FileNotFoundError:
    print("File not found")
    """file.readlines() – файлдағы барлық жолдарды 
    тізім ретінде қайтаратын әдіс."""
