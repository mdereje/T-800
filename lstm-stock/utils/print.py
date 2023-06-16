def printAsBanner(str: str):
    length = len(str)
    boarder = '=' * (length + 2)
    spaces = ' ' * length
    print(
        f'''
        {boarder}
        |{spaces}|
        |{str}|
        |{spaces}|
        {boarder}
    '''
    )
