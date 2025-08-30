# Notepad program
Tkinter로 구현한 windows의 메모장 프로그램

# 프로그램 설명

## 1. 상단 메뉴
파일(F)  편집(E)  서식(C)  보기(V)  도움말
<img width="640" height="550" alt="image" src="https://github.com/user-attachments/assets/88ca3d82-d40e-49b6-af94-c3e2aecd9931" />

이 중에서 파일(F) 기능만 구현됨.
파일(F) 메뉴 아래 열기 ,저장 , 끝내기 기능이 있음.
```Python
# 파일 메뉴

file_menu = Menu( menu , tearoff = 0)
file_menu.add_command(label = "열기" , command = open_file )
file_menu.add_command(label = "저장" , command = save_file )
file_menu.add_separator()
file_menu.add_command(label = "끝내기" , command = root.quit)
menu.add_cascade(label = "파일(F)" , menu = file_menu)
```
### 1) 열기
새 파일을 여는 기능. 
이 버튼을 선택하면 파일 탐색기가 실행되고 원하는 텍스트 파일을 열 수 있음.
<img width="640" height="550" alt="image" src="https://github.com/user-attachments/assets/4f9e5314-cf46-4595-982b-c49b89d87468" />

<img width="640" height="550" alt="image" src="https://github.com/user-attachments/assets/94edf971-62bd-4003-9f2d-354ae107bef0" />

<img width="640" height="550" alt="image" src="https://github.com/user-attachments/assets/24ea8907-1587-48d7-a3a4-1b19021043e0" />



```Python
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
```

### 2) 저장
텍스트 입력 창에 입력된 내용을 파일로 저장할 수 있는 기능.
메모장에 원하는 내용을 입력하고 이 버튼을 누르면 파일 탐색기가 실행되고 'gui_basic' 파일 아래에 원하는 파일 이름을 작성하여 저장 가능.
저장과 동시에 VScode gui_basic 폴더 아래 텍스트 파일(.txt) 형식으로 저장되고 VScode에서 바로 확인 가능함.

<img width="640" height="550" alt="image" src="https://github.com/user-attachments/assets/f7d70e8a-64f1-4f0c-b2ce-75a527848ba2" />

<img width="640" height="550" alt="image" src="https://github.com/user-attachments/assets/0c26b216-1bf3-4c6e-a9a0-cece15af5420" />

<img width="640" height="550" alt="image" src="https://github.com/user-attachments/assets/f96f401a-56d7-4780-8111-402b999d8d17" />

```Python
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
```


### 3) 끝내기
이 버튼을 누르면 자동으로 메모장 프로그램이 종료됨.

<img width="640" height="550" alt="image" src="https://github.com/user-attachments/assets/3f9d4637-93c3-4a52-b533-0ce12f02634b" />

```Python
file_menu.add_command(label = "끝내기" , command = root.quit)
```
## 2. 그 밖의 기능들
1) 스크롤 바 기능
   창 오른쪽에 스크롤 바 존재. 만약 정해진 geometry 이상으로 내용을 작성하게 되면 스크롤 바 생성되며 실제로 창을 위아래로 움직일 수 있음.

2) 프로그램 크기 , 위치 조절 가능
   사용자가 원하는대로 자유롭게 조절 가능

3) 예외처리
   파일 저장 시 open() 이나 f.write() 가 실패하는 모든 상황에서 예외처리가 실행됨.




