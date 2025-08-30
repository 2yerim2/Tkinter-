from tkinter import*
from tkinter import filedialog, messagebox


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

current_file = None

menu = Menu(root)

#파일 열기
def open_file():
    global current_file
    file_path = filedialog.askopenfilename(
        defaultextension=".txt"
    )
    if file_path: 
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text.delete(1.0, END)  # 기존 내용 지우기
                text.insert(END, f.read())
            current_file = file_path
        except Exception as e:
            messagebox.showerror("에러", f"파일을 열 수 없습니다.\n{e}")
            
#파일 저장
def save_file():
    global current_file
    if current_file:
        try:
            with open(current_file , "w",encoding = "utf-8") as f:
                f.write(text.get(1.0 ,END))
            messagebox.showinfo("저장 완료","파일이 저장되었습니다.")
        except Exception as e:
            messagebox.showinfo("에러",f"파일을 저장할 수 없습니다.\n{e}")
    else:
        save_as_file()
        
# 다른 이름으로 저장
def save_as_file():
    global current_file
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("mynote.txt", "*.txt"), ("모든 파일", "*.*")]
    )
    if file_path:
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(text.get(1.0, END))
            current_file = file_path
            root.title(f"{file_path} - Windows 메모장")
            messagebox.showinfo("저장 완료", "파일이 저장되었습니다.")
        except Exception as e:
            messagebox.showerror("에러", f"파일을 저장할 수 없습니다.\n{e}")


    
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