from tkinter import *

def add_Ask():
    new_ask = '{ask}'\
                .format(ask=entryAsk.get())
    allQuest.insert(END, new_ask)
    write_questions()

def delete_questions():
    select = allQuest.curselection()
    allQuest.delete(select[0])
    
    write_questions()

def write_questions():
    data = open('users_questions.txt', 'w', encoding='utf-8')
    for row in allQuest.get(0, END):
        data.writelines(row + '\n')
    data.close()

def print_data():
    try:
        data = open('users_questions.txt', 'r', encoding='utf-8')
        for contact in data.readlines():
            allQuest.insert(END, contact)
        data.close()
    except FileNotFoundError:
        print('файл не найден')
root = Tk()

root.geometry('700x500')

buttonAddAsk = Button(root, text='Добавить ответ', command=add_Ask)
buttonAddAsk.grid(row=1, column=1, columnspan=2)
buttonDeleteQuestions = Button(root, text='Удалить вопрос', command=delete_questions)
buttonDeleteQuestions.grid(row=2, column=1)

labelAsk = Label(root, text='Введите ответ')
labelAsk.grid(row=0, column=0)


entryAsk = Entry(root,  width=100)
entryAsk.grid(row=1, column=0)


allQuest = Listbox(root, height=30, width=100, selectmode=EXTENDED)
allQuest.grid(row=2, column=0)
print_data()

root.mainloop()
