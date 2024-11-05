from tkinter import *
import tkinter as tk
import pymysql
from tkinter import ttk
from PIL import Image,ImageTk
db=pymysql.connect(
    host='localhost',
    port=3306,
    user='root',
    database='mydatabse',
    password='srx19980201',
    charset='utf8'
)
class teacher:
    def __init__(self,mwindow):
        mwindow.destroy()
        self.window=tk.Tk()
        self.window.title('教师端信息管理系统')
        self.window.geometry('700x600+500+200')
        self.window.configure(bg='white')
        Label(self.window, text="教工号:", fg="#7e0c6e", bg="white",
        font=("SimSun", 12)).place(x=240,y=240)
        self.entry = tk.Entry(self.window, font=("SimSun", 14), width=20)
        self.entry.place(x=400, y=250, anchor=tk.CENTER)
        Label(self.window, text="密码：", fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=240,y=270)
        self.passentry = tk.Entry(self.window, font=("SimSun", 14), width=20)
        self.passentry.place(x=400, y=280, anchor=tk.CENTER)
        self.passentry.configure(show='*')
        Button(self.window, text="登陆", width=8, font=("SimSun", 18), command=self.login).place(x=350,y=330)
        Button(self.window, text="返回", width=8, font=("SimSun", 18), command=self.returnmain).place(x=500,y=400)
        self.window.mainloop()
    def login(self):
        id=self.entry.get()
        password=self.passentry.get()
        cursor = db.cursor()
        sql="select * from teacher where tno='%s' and tpassword='%s'"%(id,password)
        cursor.execute(sql)
        result=cursor.fetchall()
        if len(result) !=0:
            self.zhuye(result,id)
        else:
             Label(self.window, text="用户名或密码输入错误，请重新输入", fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=240,y=300)
        db.close
    def zhuye(self,message0,tno):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.title('教师端信息管理系统')
        self.window.geometry('1000x600+500+200')
        self.window.configure(bg='white')
        Label(self.window, text="欢迎"+message0[0][1], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=10,y=10)
        zhuye_button = Button(self.window, text="主页", command=lambda: self.zhuye(message0,tno))
        zhuye_button.place(x=100, y=10)
        xuanke_button = Button(self.window, text="我的课程", command=lambda: self.caozuo(message0,tno))
        xuanke_button.place(x=140, y=10)
        chengji_button = Button(self.window, text="成绩录入", command=lambda: self.chengji(message0,tno))
        chengji_button.place(x=220, y=10)
        return_button = Button(self.window, text="退出登录", command=self.return_to_login)
        return_button.place(x=300, y=10)
        Label(self.window, text="个人信息", fg="#7e0c6e", bg="white",font=("SimSun", 15)).place(x=500,y=50)
        Label(self.window, text="姓名"+message0[0][1], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=500,y=90)
        Label(self.window, text="教工号"+message0[0][0], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=500,y=130)
        Label(self.window, text="性别"+message0[0][2], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=500,y=170)
        Label(self.window, text="学院"+message0[0][4], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=500,y=210)
    def caozuo(self,message1,tno):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.title('教师端信息管理系统')
        self.window.geometry('1000x600+500+200')
        self.window.configure(bg='white')
        Label(self.window, text="欢迎"+message1[0][1], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=10,y=10)
        cursor = db.cursor()
        sql = "SELECT class.cno,class.name,class.ist from class where tno='%s'"%(tno)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        results = cursor.fetchall()
        columtext = ['cno', 'name', 'ist']
        teacher_text = ttk.Treeview(self.window, height=14, columns=columtext, show='headings')
        teacher_text.place(x=10,y=50)

        for col in columtext:
            teacher_text.heading(col, text=col)
            teacher_text.column(col, width=135, anchor=tk.CENTER)
        for row in results:
            teacher_text.insert('', 'end', values=row)
        zhuye_button = Button(self.window, text="主页", command=lambda: self.zhuye(message1,tno))
        zhuye_button.place(x=100, y=10)
        xuanke_button = Button(self.window, text="我的课程", command=lambda: self.caozuo(message1,tno))
        xuanke_button.place(x=140, y=10)
        chengji_button = Button(self.window, text="成绩录入", command=lambda: self.chengji(message1,tno))
        chengji_button.place(x=220, y=10)
        return_button = Button(self.window, text="退出登录", command=self.return_to_login)
        return_button.place(x=300, y=10)
        Label(self.window, text="是否允许退课", fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=600,y=210)
        yes_button = Button(self.window, text="是", command=lambda: self.yes(teacher_text,tno))
        yes_button.place(x=600, y=300)
        no_button = Button(self.window, text="否", command=lambda: self.no(teacher_text,tno))
        no_button.place(x=700, y=300)
    def chengji(self,message1,tno):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.title('教师端信息管理系统')
        self.window.geometry('1000x600+500+200')
        self.window.configure(bg='white')
        Label(self.window, text="欢迎"+message1[0][1], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=10,y=10)
        zhuye_button = Button(self.window, text="主页", command=lambda: self.zhuye(message1,tno))
        zhuye_button.place(x=100, y=10)
        xuanke_button = Button(self.window, text="我的课程", command=lambda: self.caozuo(message1,tno))
        xuanke_button.place(x=140, y=10)
        chengji_button = Button(self.window, text="成绩录入", command=lambda: self.chengji(message1,tno))
        chengji_button.place(x=220, y=10)
        return_button = Button(self.window, text="退出登录", command=self.return_to_login)
        return_button.place(x=300, y=10)
        Label(self.window, text="个人信息", fg="#7e0c6e", bg="white",font=("SimSun", 15)).place(x=500,y=50)
        Label(self.window, text="姓名"+message1[0][1], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=500,y=90)
        Label(self.window, text="教工号"+message1[0][0], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=500,y=130)
        Label(self.window, text="性别"+message1[0][2], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=500,y=170)
        Label(self.window, text="学院"+message1[0][4], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=500,y=210)
        cursor = db.cursor()
        sql = "SELECT class.cno,class.name,class.ist from class where tno='%s'"%(tno)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        results = cursor.fetchall()
        columtext = ['cno', 'name', 'ist']
        teacher_text = ttk.Treeview(self.window, height=14, columns=columtext, show='headings')
        teacher_text.place(x=10,y=50)

        for col in columtext:
            teacher_text.heading(col, text=col)
            teacher_text.column(col, width=135, anchor=tk.CENTER)
        for row in results:
            teacher_text.insert('', 'end', values=row)
        columtext2=['cno','sno','sname','cname','grade']







        myselect=ttk.Treeview(self.window,height=14,columns=columtext2,show='headings')
        myselect.place(x=500,y=50)
        for col in columtext2:
            myselect.heading(col, text=col)
            myselect.column(col, width=100, anchor=tk.CENTER)
        chaxun_button=Button(self.window, text="查询", command=lambda: self.chaxun(teacher_text,myselect))
        chaxun_button.place(x=250, y=400)
        wgrade=tk.Entry(self.window, font=("SimSun", 14), width=20)
        wgrade.place(x=500,y=400)
        xiugai_button = Button(self.window, text="修改", command=lambda: self.xiugai(myselect,wgrade))
        xiugai_button.place(x=800, y=400)
    def xiugai(self,treeview,wgrade):
        wwgrade=wgrade.get()
        foc = treeview.focus()
        val =treeview.set(foc)
        try:
            cursor=db.cursor()
            sql="update gradev set gradev.grade='%s' where gradev.cno='%s' and gradev.sno='%s'"%(wwgrade,val['cno'],val['sno']) 
            cursor.execute(sql)
            db.commit()
            Label(self.window, text="成绩修改成功", fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=240,y=500)
        except Exception as e:
            print("成绩范围不对")
            Label(self.window, text="成绩范围不对", fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=240,y=500)
            db.rollback()
        self.updat(treeview,val['cno'])
    def updat(self,treeview,cno):
        treeview.delete(*treeview.get_children())
        cursor=db.cursor()
        sql="select gradev.cno,student.sno,student.name,gradev.name,gradev.grade from gradev left join student on student.sno=gradev.sno where  gradev.cno='%s' "%(cno)
        cursor.execute(sql)
        db.commit()
        results = cursor.fetchall()
        for row in results:
            treeview.insert('', 'end', values=row)
    def chaxun(self,treeview,t2):
        foc = treeview.focus()
        val =treeview.set(foc)
        if val =={}:
            Label(self.window, text="没有选中课程", fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=240,y=500)
        else:
            cursor=db.cursor()
            sql="select gradev.cno,student.sno,student.name,gradev.name,gradev.grade from gradev left join student on student.sno=gradev.sno where  gradev.cno='%s' "%(val['cno'])
            cursor.execute(sql)
            db.commit()
            results = cursor.fetchall()
            for row in results:
                t2.insert('', 'end', values=row)
            self.upda2(t2,val['cno'])
    def upda2(self,treeview,cno):
        treeview.delete(*treeview.get_children())
        cursor=db.cursor()
        sql="select gradev.cno,student.sno,student.name,gradev.name,gradev.grade from gradev left join student on student.sno=gradev.sno where  gradev.cno='%s' "%(cno)
        cursor.execute(sql)
        db.commit()
        results = cursor.fetchall()
        for row in results:
            treeview.insert('', 'end', values=row)

    def yes(self,treeview,tno):
        foc = treeview.focus()
        val =treeview.set(foc)
        cursor=db.cursor()
        sql="call tuike('%s','二')"%(val['cno'])
        cursor.execute(sql)
        db.commit
        self.update(treeview,tno)
        print(val)
    def no(self,treeview,tno):
        foc = treeview.focus()
        val =treeview.set(foc)
        cursor=db.cursor()
        sql="call tuike('%s','否')"%(val['cno'])
        cursor.execute(sql)
        db.commit
        self.update(treeview,tno)
        print(val)
    def returnmain(self):
        self.window.destroy()
        self.window=None
        mainwindow()
    def return_to_login(self):
        self.__init__(self.window)
    def update(self,treeview,tno):
        treeview.delete(*treeview.get_children())
        cursor=db.cursor()
        sql = "SELECT class.cno,class.name,class.ist from class where tno='%s'"%(tno)
        cursor.execute(sql)
        db.commit()
        cursor.close()
        results = cursor.fetchall()
        for row in results:
            treeview.insert('', 'end', values=row)


class student:
    def __init__(self,mwindow):
        mwindow.destroy()
        self.window=tk.Tk()
        self.window.title('学生端信息管理系统')
        self.window.geometry('700x600+500+200')
        self.window.configure(bg='white')
        Label(self.window, text="学号号:", fg="#7e0c6e", bg="white",
        font=("SimSun", 12)).place(x=240,y=240)
        self.entry = tk.Entry(self.window, font=("SimSun", 14), width=20)
        self.entry.place(x=400, y=250, anchor=tk.CENTER)
        Label(self.window, text="密码:", fg="#7e0c6e", bg="white",
        font=("SimSun", 12)).place(x=240,y=270)
        self.passentry = tk.Entry(self.window, font=("SimSun", 14), width=20)
        self.passentry.place(x=400, y=280, anchor=tk.CENTER)
        self.passentry.configure(show='*')
        Button(self.window, text="登陆", width=8, font=("SimSun", 18), command=self.login).place(x=350,y=330)
        Button(self.window, text="返回", width=8, font=("SimSun", 18), command=self.returnmain).place(x=500,y=400)
        self.window.mainloop()
    def returnmain(self):
        self.window.destroy()
        self.window=None
        mainwindow()
    def login(self):
        id=self.entry.get()
        password=self.passentry.get()
        cursor = db.cursor()
        sql="select * from student where sno='%s' and password='%s'"%(id,password)
        cursor.execute(sql)
        result=cursor.fetchall()
        print(result)
        if len(result) !=0:
            self.zhuye(result,id)
        else:
             Label(self.window, text="用户名或密码输入错误，请重新输入", fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=240,y=300)
    def zhuye(self,message0,sno):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.title('学生端信息管理系统')
        self.window.geometry('1000x600+500+200')
        self.window.configure(bg='white')
        Label(self.window, text="欢迎"+message0[0][1], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=10,y=10)
        zhuye_button = Button(self.window, text="主页", command=lambda: self.zhuye(message0,sno))
        zhuye_button.place(x=100, y=10)
        xuanke_button = Button(self.window, text="选课", command=lambda: self.caozuo(message0,sno))
        xuanke_button.place(x=140, y=10)
        chengji_button = Button(self.window, text="成绩", command=lambda: self.chengji(message0,sno))
        chengji_button.place(x=180, y=10)
        return_button = Button(self.window, text="退出登录", command=self.return_to_login)
        return_button.place(x=220, y=10)
        Label(self.window, text="个人信息", fg="#7e0c6e", bg="white",font=("SimSun", 15)).place(x=500,y=50)
        Label(self.window, text="姓名"+message0[0][1], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=500,y=90)
        Label(self.window, text="学号"+message0[0][0], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=500,y=130)
        Label(self.window, text="性别"+message0[0][2], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=500,y=170)
        Label(self.window, text="学院"+message0[0][4], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=500,y=210)
    def caozuo(self,message1,sno):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.title('学生端信息管理系统')
        self.window.geometry('1000x600+500+200')
        self.window.configure(bg='white')
        Label(self.window, text="欢迎"+message1[0][1], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=10,y=10)
        zhuye_button = Button(self.window, text="主页", command=lambda: self.zhuye(message1,sno))
        zhuye_button.place(x=100, y=10)
        xuanke_button = Button(self.window, text="选课", command=lambda: self.caozuo(message1,sno))
        xuanke_button.place(x=140, y=10)
        chengji_button = Button(self.window, text="成绩", command=lambda: self.chengji(message1,sno))
        chengji_button.place(x=180, y=10)
        cursor = db.cursor()
        sql = "SELECT * FROM class"
        cursor.execute(sql)
        results = cursor.fetchall()
        columtext = ['cno', 'name', 'cteacher', 'tno','ist']
        mytext = ttk.Treeview(self.window, height=14, columns=columtext, show='headings')
        mytext.place(x=10,y=50)

        for col in columtext:
            mytext.heading(col, text=col)
            mytext.column(col, width=100, anchor=tk.CENTER)
        for row in results:
            mytext.insert('', 'end', values=row)
        cursor2=db.cursor()
        sql2="SELECT * From class where cno in(select cno from selclass where sno='%s')"%(sno)
        cursor2.execute(sql2)
        seldclass=cursor2.fetchall()
        myselect=ttk.Treeview(self.window,height=14,columns=columtext,show='headings')
        myselect.place(x=500,y=50)
        for col in columtext:
            myselect.heading(col, text=col)
            myselect.column(col, width=100, anchor=tk.CENTER)
        for r in seldclass:
            myselect.insert('', 'end', values=r)
        delete_button = Button(self.window, text="删除选定", command=lambda: self.delete(myselect,sno))
        delete_button.place(x=600, y=550)
        select_button=Button(self.window,text="我要选这个",command=lambda:self.selected(mytext,myselect,sno))
        select_button.place(x=500,y=550)
        return_button = Button(self.window, text="退出登录", command=self.return_to_login)
        return_button.place(x=220, y=10)
    def chengji(self,message2,sno):
        for widget in self.window.winfo_children():
            widget.destroy()
        self.window.title('学生端信息管理系统')
        self.window.geometry('1000x600+500+200')
        self.window.configure(bg='white')
        Label(self.window, text="欢迎"+message2[0][1], fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=10,y=10)
        zhuye_button = Button(self.window, text="主页", command=lambda: self.zhuye(message2,sno))
        zhuye_button.place(x=100, y=10)
        xuanke_button = Button(self.window, text="选课", command=lambda: self.caozuo(message2,sno))
        xuanke_button.place(x=140, y=10)
        chengji_button = Button(self.window, text="成绩", command=lambda: self.chengji(message2,sno))
        chengji_button.place(x=180, y=10)
        cursor = db.cursor()
        sql = "SELECT  cno,name,cteacher,grade from gradev where gradev.sno='%s'"%(sno)
        cursor.execute(sql)
        results = cursor.fetchall()
        columtext = ['cno', 'name', 'cteacher', 'grade']
        mytext = ttk.Treeview(self.window, height=14, columns=columtext, show='headings')
        mytext.place(x=10,y=50)

        for col in columtext:
            mytext.heading(col, text=col)
            mytext.column(col, width=100, anchor=tk.CENTER)
        for row in results:
            mytext.insert('', 'end', values=row)

    def return_to_login(self):
        self.__init__(self.window)
    def delete(self,treeview,sno):
        label1=None
        foc = treeview.focus()
        val =treeview.set(foc)
        print(val)
        if val =={}:
            Label(self.window, text="没有选中课程", fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=240,y=400)
        else:
            cursor=db.cursor()
            sql="delete selclass,grade from selclass left join grade on selclass.cno=grade.cno where selclass.sno='%s' and selclass.cno='%s'"%(sno,val['cno'])
            try:
                db.begin()
                cursor.execute(sql)
                db.commit()
                Label(self.window, text="您已退课成功", fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=240,y=400)
            except Exception as e:
                print("不能执行退课")
                db.rollback()
                Label(self.window, text="不能进行退课", fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=240,y=400)
        self.update(treeview,sno)
    def selected(self,treeview,t2,sno):
         foc = treeview.focus()
         val =treeview.set(foc)
         print(val)
         print(sno)
         cursor=db.cursor()
         sql="insert into selclass(sno,cno,ist) values('%s','%s','%s')"%(str(sno),str(val['cno']),str(val['ist']))
         sql2 = "insert into grade(tno,sno,cno,grade) values('%s','%s','%s',0)" % (str(val['tno']), sno, str(val['cno']))
         try:
             cursor.execute(sql)
             cursor.execute(sql2)
             db.commit()
             Label(self.window, text="您已选课成功", fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=240,y=400)
         except Exception as e:
             print("不能重复选课")
             Label(self.window, text="不能重复选课", fg="#7e0c6e", bg="white",font=("SimSun", 12)).place(x=240,y=400)
             db.rollback()
         self.update(t2,sno)
    def update(self,treeview,sno):
        treeview.delete(*treeview.get_children())
        cursor2=db.cursor()
        sql2="SELECT * From class where cno in(select cno from selclass where sno='%s')"%(sno)
        cursor2.execute(sql2)
        seldclass=cursor2.fetchall()
        for r in seldclass:
            treeview.insert('', 'end', values=r)
def mainwindow():
    root = tk.Tk()
    root.title('南开大学信息管理系统')
    root.geometry('700x600+500+200')
    root.configure(bg='white')
    
    teacher_login_button = tk.Button(root, text="教师登录", font=("SimSun", 18),command=lambda: teacher(root),bg='#7e0c6e',fg='white')
    teacher_login_button.place(relx=0.5, rely=0.8, anchor=tk.CENTER)

    
    student_login_button = tk.Button(root, text="学生登录", font=("SimSun", 18), command=lambda:student(root),bg='#7e0c6e',fg='white')
    student_login_button.place(relx=0.5, rely=0.9, anchor=tk.CENTER)
    photo = Image.open("OIP.jpg")
    photo = photo.resize((100,50 ))  # 规定图片大小
    img0 = ImageTk.PhotoImage(photo)
    tk.Label(image=img0).place(x=-2, y=0)
    photo1 = Image.open("111.jpg")
    photo1 = photo1.resize((500,400 ))  # 规定图片大小
    img3 = ImageTk.PhotoImage(photo1)
    tk.Label(image=img3).place(x=100, y=50)
    root.mainloop()

if __name__=='__main__':
    mainwindow()