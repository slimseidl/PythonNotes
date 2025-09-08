try:
    user_num = int(input())
    div_num = int(input())
    quot = user_num // div_num
    print(quot)
except ZeroDivisionError:
    print(f'Zero Division Exception: integer division or modulo by zero')
except ValueError as e:
    print('Input Exception:',e)