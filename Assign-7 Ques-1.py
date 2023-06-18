from tkinter import *

def findGst():
    org_cost = int(org_priceField.get())
    N_price = int(net_priceField.get())
    gst_rate = ((N_price - org_cost) * 100) / org_cost
    gst_rateField.insert(10, str(gst_rate) + " %")

root = Tk()
root.geometry("400x250")
root.title("GST Tax Finder Calculator")

org_price = Label(root, text="Original Cost", font=("Helvetica", 16))
org_price.grid(row=0, column=0)

net_price = Label(root, text="Net Price", font=("Helvetica", 16))
net_price.grid(row=1, column=0)

org_priceField = Entry(root)
net_priceField = Entry(root)

org_priceField.grid(row=0, column=1)
net_priceField.grid(row=1, column=1)

calculate = Button(root, text="Calculate GST", command=findGst)
calculate.grid(row=2, column=1)

gst_rate = Label(root, text="GST Rate", font=("Helvetica", 16))
gst_rate.grid(row=3, column=0)

gst_rateField = Entry(root)
gst_rateField.grid(row=3, column=1)

root.mainloop()
