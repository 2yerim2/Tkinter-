from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("제목 없음 - Windows 메모장")
root.geometry("640x480")  # 가로 * 세로

# 텍스트 입력 창
text_area = Text(root, wrap="word", font=("맑은 고딕", 12))
text_area.pack(expand=True, fill="both")

# 파일 열기
def open_file():
    file_path = filedialog.askopenfilename(
        filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
    )
    if file_path:
        with open(file_path, "r", encoding="utf-8") as file:
            text_area.delete("1.0", END)
            # 텍스트 가져와 저장
        root.title(f"{file_path} - Windows 메모장")

# 메뉴
menu = Menu(root)

# 파일 메뉴 만들기
file_menu = Menu(menu, tearoff=0)
file_menu.add_command(label="열기", command=open_file)
file_menu.add_command(label="저장", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="끝내기", command=root.quit)
menu.add_cascade(label="파일(F)", menu=file_menu)

# 편집 메뉴 만들기 (아직 기능 없음)
edit_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="편집(E)", menu=edit_menu)

# 서식 메뉴 만들기 (아직 기능 없음)
form_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="서식(C)", menu=form_menu)

# 보기 메뉴 만들기 (아직 기능 없음)
show_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="보기(V)", menu=show_menu)

# 도움말 메뉴 만들기 (아직 기능 없음)
help_menu = Menu(menu, tearoff=0)
menu.add_cascade(label="도움말", menu=help_menu)

root.config(menu=menu)

root.config(menu=menu)
root.mainloop()