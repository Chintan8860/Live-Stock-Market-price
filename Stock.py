from urllib.request import urlopen
from tkinter import *
from tkinter import messagebox
from urllib.request import urlopen
from zipfile import ZipFile


def serch():
    if display.get() == "":
        messagebox.showinfo("Warnning", "enter a keyword for serch")

    else:
        print_text.set("Fetching data .... ")

        scrap()


def screen():
    global start
    start = Tk()
    global mainframe
    mainframe = Frame(start, bg="red")
    mainframe.pack()
    start.geometry('1100x600')
    start.configure(bg="#E29484")
    start.title("Show Stock Market View")
    label = Label(mainframe, text="Live Stock Market Price", bg="black", fg="white", width="700", height="2",
                  font=("Calibri", 18), padx=5, pady=5)
    label.pack(fill="x")
    global display
    display = StringVar()
    Label(start, text="Search Share :-", bg="#E29484", width="12", fg="black", height="2", font=("Calibri", 20)).place(
        x=50, y=100)
    Entry(start, relief=RIDGE, bd=6, bg="powder blue", textvar=display, width="30", font=("Calibri", 18)).place(x=230,
                                                                                                                y=115)
    Button(start, text="Search", width="18", height="2", command=serch).place(x=620, y=115)
    global print_text
    print_text = StringVar()
    Label(start, textvariable=print_text, bg="#E29484", fg="black", height="2", font=("Calibri", 13)).place(x=350,
                                                                                                            y=160)
    horizontal_frame = Frame(mainframe, bg="#E29484")

    label1 = Label(horizontal_frame, text="CODE", bg="white", fg="black", padx=10, pady=10)
    label1.grid(row=0, column=0, padx=10, pady=150, sticky="nsew")
    label1 = Label(horizontal_frame, text="NAME", bg="white", fg="black", padx=10, pady=10)
    label1.grid(row=0, column=1, padx=10, pady=150, sticky="nsew")
    label1 = Label(horizontal_frame, text="OPEN", bg="white", fg="black", padx=10, pady=10)
    label1.grid(row=0, column=2, padx=10, pady=150, sticky="nsew")
    label1 = Label(horizontal_frame, text="CLOSE", bg="white", fg="black", padx=10, pady=10)
    label1.grid(row=0, column=3, padx=10, pady=150, sticky="nsew")
    label1 = Label(horizontal_frame, text="HIGH", bg="white", fg="black", padx=10, pady=10)
    label1.grid(row=0, column=4, padx=10, pady=150, sticky="nsew")
    label1 = Label(horizontal_frame, text="LOW", bg="white", fg="black", padx=10, pady=10)
    label1.grid(row=0, column=5, padx=10, pady=150, sticky="nsew")
    horizontal_frame.grid_columnconfigure(0, weight=1)
    horizontal_frame.grid_columnconfigure(1, weight=1)
    horizontal_frame.grid_columnconfigure(2, weight=1)
    horizontal_frame.grid_columnconfigure(3, weight=1)
    horizontal_frame.grid_columnconfigure(4, weight=1)
    horizontal_frame.grid_columnconfigure(5, weight=1)
    horizontal_frame.pack(fill="x")

    start.mainloop()


def chnge_occur():
    # print comanny code

    label1 = Label(start, textvariable=dis_no, bg="#E29484", fg="black", padx=20, pady=10, font=("Calibri", 15))
    label1.place(x=45, y=310)
    # print name

    label1 = Label(start, textvariable=dis_name, bg="#E29484", fg="black", padx=20, pady=10, font=("Calibri", 15))
    label1.place(x=225, y=310)
    # print open
    label1 = Label(start, textvariable=dis_open, bg="#E29484", fg="black", padx=20, pady=10, font=("Calibri", 15))
    label1.place(x=412, y=310)
    # print close
    label1 = Label(start, textvariable=dis_close, bg="#E29484", fg="black", padx=20, pady=10, font=("Calibri", 15))
    label1.place(x=600, y=310)
    # print high
    label1 = Label(start, textvariable=dis_high, bg="#E29484", fg="black", padx=20, pady=10, font=("Calibri", 15))
    label1.place(x=790, y=310)
    # print low
    label1 = Label(start, textvariable=dis_low, bg="#E29484", fg="black", padx=20, pady=10, font=("Calibri", 15))
    label1.place(x=970, y=310)


def scrap():
    print_text.set("wait")

    URL = "https://www.bseindia.com/markets/MarketInfo/BhavCopy.aspx"
    text_from_entry = display.get()
    with_sp = text_from_entry.replace(" ", "")
    without_sp = with_sp.upper()
    stock_count = 0
    website = urlopen(URL)

    if website.status == 200:
        html = website.read().decode('utf-8')
        pattern = '"(http://www.bseindia.com/download/BhavCopy/Equity/.*?)"'
        links = re.findall(pattern, html)
        response = urlopen(links[0])
        zipfile = ZipFile(BytesIO(response.read()))
        for csvfilename in zipfile.namelist():
            for line in zipfile.open(csvfilename).readlines()[1:]:
                arr = line.decode('utf-8').split(",")
                dic = {
                    "CODE": arr[0],
                    "NAME": arr[1],
                    "OPEN": arr[4],
                    "HIGH": arr[5],
                    "LOW": arr[6],
                    "CLOSE": arr[7],
                }
                stock_count += 1
                nn = dic.copy()
                global p

                p = nn.get('NAME')
                p_c = nn.get('CODE')

                f = p.replace(" ", "")
                global c
                global o
                global h
                global l
                global cl
                global dis_name
                global dis_open
                global dis_no
                global dis_high
                global dis_close
                global dis_low
                dis_no = StringVar()
                dis_name = StringVar()
                dis_high = StringVar()
                dis_low = StringVar()
                dis_open = StringVar()
                dis_close = StringVar()

                if f == without_sp or p_c == without_sp:
                    c = nn.get('CODE')
                    o = nn.get('OPEN')
                    h = nn.get('HIGH')
                    l = nn.get('LOW')
                    cl = nn.get('CLOSE')
                    print_text.set("Live value From BSE Website... ")

                    # print _
                    print_line = StringVar()
                    st = "_"
                    for i in range(0, 1000):
                        st = st + '_'
                    print_line.set(st)
                    label1 = Label(start, textvariable=print_line, bg="#E29484", fg="black", padx=0, pady=10,
                                   font=("Calibri", 10))
                    label1.place(x=1, y=260)
                    dis_no.set(c)
                    dis_name.set(p)
                    dis_open.set(o)
                    dis_close.set(h)
                    dis_low.set(l)
                    dis_high.set(cl)

                    chnge_occur()
                    display.set("")
                    break
                else:
                    if stock_count < 2880:
                        pass
                    else:
                        print_text.set("Opps..Data Not Found!!!")
                        st = " "
                        for i in range(0, 100):
                            st = st + ' '
                        dis_no.set(st)
                        dis_name.set(st)
                        dis_open.set(st)
                        dis_close.set(st)
                        dis_low.set(st)
                        dis_high.set(st)
                        display.set(st)
                        chnge_occur()
                        break

        return stock_count
    else:
        print_text.set("Website server Down !!! try after some time..")
        return stock_count


screen()
