from tkinter import *
from tkinter import Tk, ttk, filedialog
import os
from tqdm import tqdm
import shutil
from qr_reader import QR
from oeq_data_write import DataWrite
from oeq_validation import Validate
from tkinter import messagebox
from PIL import ImageTk, Image
from oeq_prepare_data import PredictData

qr = QR()
prepare_data = PredictData()
data_oeq = DataWrite()
validate_oeq = Validate()
# background_image = ImageTk.PhotoImage(bg)
FILENAME = 'bg.jpg'
root = Tk()
root.title("OMR SCAN")
canvas = Canvas(root, width=800, height=500)
canvas.pack(fill=BOTH)
tk_img = ImageTk.PhotoImage(file=FILENAME)
canvas.create_image(0, 0, anchor='nw', image=tk_img)

first_label = Label(root, text="Input Image Path", bg="#f7f9f9", width=25)
first_label_window = canvas.create_window(10, 10, anchor='nw', window=first_label)

second_label = Label(root, text="Output Image Path", bg="#f7f9f9", width=25)
second_label_window = canvas.create_window(10, 50, anchor='nw', window=second_label)

result_label = Label(root, text="Result", bg="#42bff4", width=25)
result_label_windows = canvas.create_window(10, 125, anchor='nw', window=result_label)

var1 = StringVar()
var1.set("")

var2 = StringVar()
var2.set("")

first_text = Entry(root, width=70, textvariable=var1)
first_text_windows = canvas.create_window(200, 10, anchor='nw', window=first_text)

second_text = Entry(root, width=70, textvariable=var2)
second_text_windows = canvas.create_window(200, 50, anchor='nw', window=second_text)

filename1 = ""
filename2 = ""


def browse_func1():
    filename = filedialog.askdirectory()
    var1.set(filename)


def browse_func2():
    filename = filedialog.askdirectory()
    filename2 = str(filename)
    var2.set(filename)


brows_button1 = Button(root, text="Browse", width=10, command=browse_func1, bg="#9d41f4")
brows_button1_window = canvas.create_window(650, 10, anchor='nw', window=brows_button1)

brows_button2 = Button(root, text="Browse", width=10, command=browse_func2, bg="#9d41f4")
brows_button2_window = canvas.create_window(650, 50, anchor='nw', window=brows_button2)

close_button = Button(root, text="Close", width=10, command=root.quit, bg="#9d41f4")
close_button_window = canvas.create_window(650, 100, anchor='nw', window=close_button)

tree = ttk.Treeview(root, height=15, columns=('New File Path', 'Is Success', 'Paper Id', 'Student Id'),
                                 show="headings", selectmode="browse")
tree.heading("0", text="Paper ID")
tree.heading("1", text="IsSuccess")
tree.heading("2", text="Student ID")
tree.heading("3", text="The Output Images Path")
tree.column('#0', width=80)
tree.column('#1', width=100)
tree.column('#2', width=100)
tree.column('#3', width=200)
vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
hsb = ttk.Scrollbar(root, orient="horizontal", command=tree.xview)
tree.configure(yscrollcommand=vsb.set)
tree.configure(xscrollcommand=hsb.set)
tree.tag_configure("success", background="green")
tree.tag_configure("fail", background="red")
tree_window = canvas.create_window(10, 150, anchor='nw', window=tree)
vsb_window = canvas.create_window(605, 150, anchor='nw', window=vsb, height=327)
style = ttk.Style()
style.configure("Treeview", background="#383838", foreground="white", fieldbackground="white")
style.configure("Treeview.Heading", foreground='red')


def process():
    tree.delete(*tree.get_children())
    itr = 1001
    df = []
    input_path = str(var1.get())
    out_path = str(var2.get())
    try:
        for img in tqdm(os.listdir(input_path)):
            image_path = os.path.join(input_path, img)
            if image_path.endswith(tuple([".jpg", ".png"])):
                if qr.qr(image_path):
                    if qr.type(image_path) == 'm':
                        continue
                        # if qr.mark_or_answer(image_path) == '2':
                        #     length = validate_mark.array_length(image_path)
                        #     message, condition = validate_mark.find_quality_image(image_path)
                        #     if condition == 'success' and length:
                        #         lst = qr.qr_all_details(image_path)
                        #         student_id, paper_id = qr.qr_details_mark_sheet(image_path)
                        #         subject = str(lst).split('/')[-8]
                        #         scan_data =
                        #         new_path = out_path + '/' + condition + '/MCQMarkSheet/' + str(subject) + '/' + str(
                        #             paper_id)
                        #         data_mark_sheet.insert_or_update(student_id, paper_id, lst)
                        #         itr = itr + 1
                        #         if not os.path.exists(new_path):
                        #             os.makedirs(new_path)
                        #         path_move = out_path + '/' + condition + '/MCQMarkSheet/' + str(subject) + '/' + str(
                        #             paper_id) + '/' + str(student_id) + '_' + str(itr) + '.jpg'
                        #         shutil.move(image_path, path_move)
                        #         df.append([paper_id, "success", student_id, new_path])
                        #
                        #     else:
                        #         student_id, paper_id = qr.qr_details_mark_sheet(image_path)
                        #         new_path = out_path + '/' + 'fail/MCQMarkSheet'
                        #         if not os.path.exists(new_path):
                        #             os.makedirs(new_path)
                        #         path_move = out_path + '/' + 'fail/MCQMarkSheet/' + img
                        #         shutil.move(image_path, path_move)
                        #         df.append([paper_id, "fail", student_id, new_path])
                        #
                        # else:
                        #     message, condition = validate_answer.find_quality_image(image_path)
                        #     length = validate_answer.array_length(image_path)
                        #     if condition == 'success' and length:
                        #         lst = qr.qr_all_details(image_path)
                        #         student_id, paper_id = qr.qr_details_answer_sheet(image_path)
                        #         subject = str(lst).split('/')[-7]
                        #         data_answer_sheet.insert_or_update(image_path)
                        #         itr = itr + 1
                        #         new_path = out_path + '/' + condition + '/MCQAnswerSheet/' + str(subject) + '/' + str(
                        #             paper_id)
                        #         if not os.path.exists(new_path):
                        #             os.makedirs(new_path)
                        #         path_move = out_path + '/' + condition + '/MCQAnswerSheet/' + str(subject) + '/' + str(
                        #             paper_id) + '/' + str(student_id) + '_' + str(itr) + '.jpg'
                        #         shutil.move(image_path, path_move)
                        #         df.append([paper_id, "success", student_id, new_path])
                        #
                        #     else:
                        #         student_id, paper_id = qr.qr_details_answer_sheet(image_path)
                        #         new_path = out_path + '/' + 'fail/MCQAnswerSheet'
                        #         if not os.path.exists(new_path):
                        #             os.makedirs(new_path)
                        #         path_move = out_path + '/' + 'fail/MCQAnswerSheet/' + img
                        #         shutil.move(image_path, path_move)
                        #         df.append([paper_id, "fail", student_id, new_path])

                    else:
                        length = validate_oeq.array_length(image_path)
                        _, condition = validate_oeq.find_quality_image(image_path)
                        if condition == 'success' and length:
                            lst = qr.qr_all_details(image_path)
                            student_id, paper_id = qr.qr_details_oeq(image_path)
                            subject = str(lst).split('/')[-6]
                            new_path = out_path + '/' + condition + '/OEQ/' + str(subject) + '/' + str(paper_id)
                            scan_data = prepare_data.paper_df_data(image_path)
                            data_oeq.insert_or_update(student_id, paper_id, lst, scan_data)
                            itr = itr + 1
                            if not os.path.exists(new_path):
                                os.makedirs(new_path)
                            path_move = out_path + '/' + condition + '/OEQ/' + str(subject) + '/' + str(
                                paper_id) + '/' + str(student_id) + '_' + str(itr) + '.jpg'
                            shutil.move(image_path, path_move)
                            df.append([paper_id, "success", student_id, new_path])

                        else:
                            lst = qr.qr_all_details(image_path)
                            student_id = str(lst).split('/')[-3]
                            paper_id = str(lst).split('/')[-2]
                            new_path = out_path + '/' + 'fail/OEQ'
                            if not os.path.exists(new_path):
                                os.makedirs(new_path)
                            path_move = out_path + '/' + 'fail/OEQ/' + img
                            shutil.move(image_path, path_move)
                            df.append([paper_id, "fail", student_id, new_path])

                else:
                    # print("done")
                    mess = 'QR code cannot able to identify for {}'.format(image_path)
                    messagebox.showerror(message=mess)
                    continue
            else:
                # print('done')
                mess = '{} file cannot read from system'.format(image_path)
                messagebox.showerror(message=mess)
                continue

    except OSError as ex:
        messagebox.showerror("Error", ex)

    columns = ['New File Path', 'Is Success', 'Paper Id', 'Student Id']
    # self.df = pd.DataFrame(np.array(df), columns=columns)
    # print(self.df.head())
    # self.df.style.apply(self.highlight_col, axis=None)
    # self.f = Frame(self.main)
    if df:
        for row in df:
            if row[1] == "success":
                tree.insert('', 0, values=row, tags="success")
            else:
                tree.insert('', 0, values=row, tags="fail")
        # self.f.pack(fill=BOTH, expand=1)
        # self.table = Table(self.f, dataframe=self.df, showtoolbar=True, showstatusbar=True)
        # # self.df = pd.DataFrame
        # # self.table.colorRows()
        # # self.table.update()
        # self.table.show()

    return


scan_button = Button(root, text="Scan", width=10, command=process, bg="#9d41f4")
scan_button_window = canvas.create_window(550, 100, anchor='nw', window=scan_button)
root.resizable(width=False, height=False)
root.iconbitmap('logo.ico')
root.mainloop()
