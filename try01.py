from tkinter import *
import tkinter as tk
import tkinter.messagebox

#หน้าจอแรก
window = tk.Tk()
window.geometry("400x400+0+50")
window.title('TeleOB&GYN')
name_entry = StringVar()
id_entry = StringVar()
gender_entry = StringVar()
age_entry = StringVar()
birth_entry = StringVar()
number_entry = StringVar()


def pt_database():
    print('Accepted!')
    name = name_entry.get()
    thai_id = id_entry.get()
    gender = gender_entry.get()
    age = age_entry.get()
    birth = birth_entry.get()
    number = number_entry.get()
    print(name, thai_id, gender, age, birth, number)


def sign_in():
    #หน้าจอที่สอง
    window2 = tk.Tk()
    window2.geometry('600x500+30+100')
    window2.title('ลงทะเบียน')
    window2.option_add('*Font', 'Consolas 14')
    window_label = tk.Label(master=window2, text='กรุณากรอกข้อมูลต่อไปนี้ ตามความจริง').grid(row=0, column=3)

    #labelและช่องกรอกข้อมูล
    name_label = tk.Label(master=window2, text='ชื่อ-นามสกุล')
    name_entry = tk.Entry(master=window2)  # .pack()
    id_label = tk.Label(master=window2, text='เลขประจำตัวประชาชน')  # .pack()
    id_entry = tk.Entry(master=window2)  # .pack()
    gender_label = tk.Label(master=window2, text='เพศ')  # .pack()
    gender_entry = tk.Entry(master=window2)  # .pack()
    age_label = tk.Label(master=window2, text='อายุ')  # .pack()
    age_entry = tk.Entry(master=window2)  # .pack()
    birth_label = tk.Label(master=window2, text='วัน/เดือน/ปีเกิด')  # .pack()
    birth_entry = tk.Entry(master=window2)  # .pack()
    number_label = tk.Label(master=window2, text='เบอร์โทรศัพท์')  # .pack()
    number_entry = tk.Entry(master=window2)  # .pack()
    #จัดหน้าจอ
    name_label.grid(row=1, column=2)
    name_entry.grid(row=1, column=3)
    id_label.grid(row=2, column=2)
    id_entry.grid(row=2, column=3)
    gender_label.grid(row=3, column=2)
    gender_entry.grid(row=3, column=3)
    age_label.grid(row=4, column=2)
    age_entry.grid(row=4, column=3)
    birth_label.grid(row=5, column=2)
    birth_entry.grid(row=5, column=3)
    number_label.grid(row=6, column=2)
    number_entry.grid(row=6, column=3)
    #ปุ่มต่างๆ
    data_btn = tk.Button(master=window2, text='ตกลง', command=pt_database, width=5, height=1, bg='pink').grid(row=7, column=3)
    previous_btn = tk.Button(master=window2, text='ย้อนกลับ', width=5, height=1, fg='white', bg='red').grid(row=8,
                                                                                                            column=3)
    examine_btn = tk.Button(master=window2, text='ตรวจสอบ', width=5, height=1, fg='white', bg='blue').grid(row=9,
                                                                                                           column=3)
    # tk.Button(master=window2, text='แก้ไข', width=5, height=1, fg='white', bg='orange').pack()

    window2.mainloop()

mymenu = Menu()
window.config(menu=mymenu)
#เมนูย่อย
menuitem1 = Menu()
menuitem1.add_command(label='วัตถุประสงค์')
menuitem1.add_command(label='ข้อมูลโรงพยาบาล')

#เมนูหลัก
mymenu.add_cascade(label='เกี่ยวกับ',menu=menuitem1)
mymenu.add_cascade(label='ติดต่อเรา')
mymenu.add_cascade(label='ข้อมูลแพทย์')
mymenu.add_cascade(label='เข้าสู่ระบบ')
mymenu.add_cascade(label='ลงทะเบียน', command=sign_in)
#labelหน้าจอแรก
window.option_add("*Font",'Consolas 14')
text1 = tk.Label(master=window, text='ยินดีต้อนรับเข้าสู่', bg='pink').pack()
text2 = tk.Label(master=window, text='คลินิกออนไลน์สำหรับให้คำปรึกษาปัญหาสุขภาพผู้หญิง', bg='pink').pack()

window.mainloop()