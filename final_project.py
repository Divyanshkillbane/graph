import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import *
from PIL import ImageTk, Image
from tkinter import Label,filedialog


# window
root  = Tk()
root.geometry('1200x900')
root.title("graph analysis")
# photo = ImageTk.PhotoImage(file ='python_practice/GUI_icon.ico')
# root.iconphoto(False,photo)
root.configure(background="#88cffa")

'''open function'''
def open():
    global data 
    root.filename = filedialog.askopenfilename(initialdir=r"D:/ml vs/python_practice",title ='selct a file',filetypes=(('all files','*.*'),('png','*.png')))
    data = pd.read_csv(root.filename)
    fun()



'''open button'''
bt1 = Button(root,text='Open File',command = open)
bt1.place(x =5, y =5)


def fun():
    global Canvas



    '''value dictionary'''
    values = {
        'Pair Plot': 'sns.pairplot(data)',
        'Joint Plot': "sns.jointplot(data= data,x='{c1}' , y ='{c2}')",
        'Bar Plot': "sns.barplot(data= data,x='{c1}' , y ='{c2}',hue ='{c3}')",
        'Box Plot': "sns.boxplot(data= data,x='{c1}' , y ='{c2}',hue ='{c3}')",
        'Line Plot': "sns.lineplot(data= data,x='{c1}' , y ='{c2}',hue ='{c3}')",
        'Scatter Plot':"sns.scatterplot(data= data,x='{c1}' , y ='{c2}',hue ='{c3}')",
        'Histogram' : "sns.distplot(data['{c1}'])",
        'violin plot':"sns.violinplot(data= data,x='{c1}' , y ='{c2}')",
        'Heatmap':"sns.heatmap(data)"
    }

    '''graph varible (string var)'''
    graph = StringVar()
    graph.set(values['Pair Plot'])

    '''Radio Buttons''' 
    y =100 
    for key, value in values.items():
        Radiobutton(root, text = key, variable = graph, value = value , bg ='LightPink1',font =20).place(x =10, y=y)
        y +=40
    
    '''drop down values'''
    dd_values = ['Select'] + list(data.columns)
    
    col1 = StringVar()
    col2 = StringVar()
    col3 = StringVar()
    
    #select 
    col1.set(dd_values[0])
    col2.set(dd_values[0])
    col3.set(dd_values[0])

    '''3 dropdowns and labels'''
    Label(root,text='X label',bg = 'navajo white',font =20).place(x=150, y =100)
    opt_1 = OptionMenu(root,col1 ,*dd_values)
    opt_1.place(x=150,y=130)
    opt_1.config(font =20 , bg = 'LightPink2')
    
    Label(root,text='Y label',bg = 'navajo white',font =20).place(x=150, y =170)
    opt_1 = OptionMenu(root,col2 ,*dd_values)
    opt_1.place(x=150,y=200)
    opt_1.config(font =20 , bg = 'LightPink2')

    Label(root,text='Hue',bg = 'navajo white',font =20).place(x=150, y =240)
    opt_1 = OptionMenu(root,col3 ,*dd_values)
    opt_1.place(x=150,y=270)
    opt_1.config(font =20 , bg = 'LightPink2')

    cnv = Canvas(root, width = 800,height=600)
    cnv.place(x=300,y=60)
   
    result = StringVar()
    Label(root, textvariable=result).place(x=680,y=650)

    def show():
        global data
        column1= col1.get()
        column2=col2.get()
        column3 = col3.get()
        print("hello1")
        g= graph.get()
        if 'c1' in g:
           if column1 == 'Select':
              result.set('Column 1 must be selected')
              return
        if 'c2' in g:
           if column2 == 'Select':
              result.set('Column 2 must be selected')
              return
        if 'c3' in g:
            if column3 == 'Select':
               result.set('Column 3 must be selected')
               return

        fig = plt.figure(figsize=(16,9))
        print(g.format( c1 = column1 , c2 = column2 , c3 = column3))
        eval(g.format( c1 = column1 , c2 = column2 , c3 = column3))
        fig.savefig('GGGGG.png')
        print("hello")
        img = ImageTk.PhotoImage(Image.open('GGGGG.png').resize((800,600)))
        cnv.create_image(0,0,anchor =NW,image = img)
        print("hello2")
        result.set('success')

    Button(root, text ='show',command =show).place(x=400,y=10)

root.mainloop()