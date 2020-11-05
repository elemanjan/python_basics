criminalsQuantity = int(input())

if criminalsQuantity < 5:
    print("Я смогу сам")
elif (criminalsQuantity >= 5) & (criminalsQuantity <= 10):
    print("Помоги мне, Бэтмен")
elif criminalsQuantity > 10:
    print("Удачи тебе!")
