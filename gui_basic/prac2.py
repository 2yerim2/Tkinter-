import os
from tkinter import*

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480") #가로 * 세로

# 스크롤 바
scrollbar = Scrollbar(root)
scrollbar.pack(side = "right" , fill = "y")

#텍스트 입력창
text= Text(root, yscrollcommand = scrollbar.set)
text.pack(expand=True, fill="both" , side = "left")
scrollbar.config(command = text.yview)

# current_file = None

#파일 열기
filename = "mynote.txt"

def open_file():
    if os.path.isfile(filename): #파일 있으면 열기
        with open(filename , "r" , encoding = "utf-8") as file:
            text.delete("1.0" , END) #본문 삭제
            text.insert(END , file.read()) #삭제 후 본문 입력

# 파일 저장            
def save_file():
    with open(filename , "w" , encoding ="utf-8") as file:
        file.write(text.get("1.0" , END)) #모든 내용 저장
        
menu = Menu(root)

    
# 파일 메뉴

file_menu = Menu( menu , tearoff = 0)
file_menu.add_command(label = "열기" , command = open_file )
file_menu.add_command(label = "저장" , command = save_file )
file_menu.add_separator()
file_menu.add_command(label = "끝내기" , command = root.quit)
menu.add_cascade(label = "파일(F)" , menu = file_menu)


# 편집 메뉴
edit_menu = Menu( menu , tearoff =0 )
menu.add_cascade(label = "편집(E)" , menu = edit_menu)

# 서식 메뉴
form_menu = Menu( menu , tearoff = 0 )
menu.add_cascade(label = "서식(C)" , menu = form_menu)

# 보기 메뉴
show_menu = Menu( menu , tearoff = 0 )
menu.add_cascade(label = "보기(V)" , menu = show_menu)

# 도움말 메뉴
help_menu = Menu( menu , tearoff = 0 )
menu.add_cascade(label = "도움말" , menu = help_menu)



root.config(menu = menu)

root.mainloop()