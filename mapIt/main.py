import webbrowser, sys, pyperclip
# программа открывает карту в браузере, используя почтовый адрес из командной строки
# или буфера обмена

if len(sys.argv) > 1:
    # получение адреса из командной строки
    address = ''.join(sys.argv[1:])
else:
    # получение адреса из буфура
    address = pyperclip
