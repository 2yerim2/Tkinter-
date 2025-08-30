from tkinter import *

root = Tk()
root.title("Nado GUI")
root.geometry("640x480")

Label(root , text = "메뉴를 선택하세요").pack()

# radiobutton : 여러 버튼이 동시에 다중 선택이 안되고 단일 선택만 가능한 버튼

burger_var = IntVar() #여기에 int값으로 저장한다
btn_burger1 = Radiobutton(root , text = "햄버거", value =1 , variable = burger_var)
btn_burger1.select() #1번이 기본값으로 설정됨
btn_burger2 = Radiobutton(root , text = "치즈버거", value =2 , variable = burger_var)
btn_burger3 = Radiobutton(root , text = "불고기버거", value =3 , variable = burger_var)

btn_burger1.pack()
btn_burger2.pack()
btn_burger3.pack()

Label(root , text ="음료를 선택히세요").pack()

drink_var = StringVar()
btn_drink1 = Radiobutton(root , text = "콜라" , value ="콜라" , variable = drink_var)
btn_drink1.select() #1번이 기본값으로 설정됨
btn_drink2 = Radiobutton(root , text = "사이다" , value ="사이다" , variable = drink_var)
btn_drink3 = Radiobutton(root , text = "환타" , value ="환타", variable = drink_var)

btn_drink1.pack()
btn_drink2.pack()
btn_drink3.pack()



def btncmd():
    print(burger_var.get())
    print(drink_var.get())#햄버거 중 선택된 라디오 항목의 값(value)을 출력
    

btn =  Button(root , text ="주문", command = btncmd)
btn.pack()

root.mainloop()