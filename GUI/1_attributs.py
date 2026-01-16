from tkinter import *

root = Tk()
root.geometry("500x500")
root.minsize(200,200)
# root.maxsize(1000,1000)

text = '''Baahubali (styled in official material as bāhubali;[a] transl. 'The One\n with Strong Arms') is an Indian Telugu-language \nmedia franchise created by S. S. Rajamouli and owned by Arka Media Works.\n The Telugu language franchise started off with a \ntwo-part film series directed by Rajamouli.[b] The franchise is widely\n regarded as one of the most important and influential \nfilms in the history of Indian cinema.[8][9]'''

'''
Label properties :-
1. text - add text
2. bd , bg - background
3. fg - foreground
4. font - set font
5. padx , pady - padding
6. relief - border styling -sunken ,relief , groove
'''
a=Label(text=text , bg='blue' , padx=4, fg="white" , pady=100 , font=('conicsans' , 19 , 'bold') , borderwidth=3 , relief='solid' )

'''
pack options -
1. anchor = direction - ne , nw
2. side = direction of flow - top , bottom , right , left
3. padx , pady
4. fill = x , fill = y -- similar as vh , vw
'''
a.pack(side='bottom',anchor='se',fill=Y)


root.mainloop()
