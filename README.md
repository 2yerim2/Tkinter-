# Notepad program
Tkinter로 구현한 windows의 메모장 프로그램

# 프로그램 설명

## 1. 상단 메뉴
파일(F)  편집(E)  서식(C)  보기(V)  도움말

이 중에서 파일(F) 기능만 구현됨.
파일(F) 메뉴 아래 열기 ,저장 , 끝내기 기능이 있음.
### 1) 열기
새 파일을 여는 기능. 
이 버튼을 선택하면 파일 탐색기가 실행되고 원하는 텍스트 파일을 열 수 있음.
<img width="500" height="550" alt="image" src="https://github.com/user-attachments/assets/c07c7475-d420-48cb-929a-2c3cbb5db190" />

<img width="500" height="550" alt="image" src="https://github.com/user-attachments/assets/f136617e-2a42-4ffd-9e29-66173fb29ce7" />

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

### 3) 끝내기
이 버튼을 누르면 자동으로 메모장 프로그램이 종료됨.

## 2. 그 밖의 기능들
1) 스크롤 바 기능
   창 오른쪽에 스크롤 바 존재. 만약 정해진 geometry 이상으로 내용을 작성하게 되면 스크롤 바 생성되며 실제로 창을 위아래로 움직일 수 있음.

2) 프로그램 크기 , 위치 조절 가능
   사용자가 원하는대로 자유롭게 조절 가능

3) 예외처리
   파일 저장 시 open() 이나 f.write() 가 실패하는 모든 상황에서 예외처리가 실행됨.




