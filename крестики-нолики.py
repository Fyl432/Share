def checkwin(pole):
    if pole[0][0]==pole[0][1]==pole[0][2]: return pole[0][0]
    if pole[1][0]==pole[1][1]==pole[1][2]: return pole[1][0]
    if pole[2][0]==pole[2][1]==pole[2][2]: return pole[2][0]
    if pole[0][0]==pole[1][0]==pole[2][0]: return pole[0][0]
    if pole[0][1]==pole[1][1]==pole[2][1]: return pole[0][1]
    if pole[0][2]==pole[1][2]==pole[2][2]: return pole[0][2]
    if pole[0][0]==pole[1][1]==pole[2][2]: return pole[0][0]
    if pole[0][2]==pole[1][1]==pole[2][0]: return pole[0][2]
    return False

def draw(pole):
    print ("-------------")
    for i in range(3):
        print ("|", pole[i][0], "|", pole[i][1], "|", pole[i][2], "|")
        print ("-------------")

def human_turn(token):
    empty= False
    while not empty:
        num = int (input('Введите номер поля для ' + token ))
        if 0<= num <=8:
            if  str(pole[num//3][num%3]) not in "XO":
                pole[num//3][num%3] = token
                empty = True
            else: print('Это поле занято, выберите другое')
        else: print('Введите существующий номер поля')

def main():
    q = input('Хотите сыграть в крестики-нолики? (Y/Any) ')
    if q == 'Y' or q == 'y':
        global pole
        pole = [['0','1','2'],['3','4','5'],['6','7','8']]
        counter = 0
        win=False
        while not win:
            draw(pole)
            if counter % 2 == 0:
                human_turn('X')
            else:
                human_turn('O')
            winner = checkwin(pole)
            if winner:
                print('Победил "', winner,'"')
                win = True
            counter += 1
            if counter == 9:
                print('Ничья!')
                break

main()








