#importing modules
from tkinter import *
from tkinter.filedialog import *
from PIL import ImageTk,Image
from stegano import exifHeader as stg
from tkinter import messagebox
import sys

#Binary to UTF
def bin_to_utf(data):
    
    Unicode_data = ''
    for d in data:
        binary_int = int(d,2)
        byte_number = binary_int.bit_length() + 7 # 8
        binary_array = binary_int.to_bytes(byte_number, "big")
        ascii_text = binary_array.decode("utf-8", 'ignore')       
        
        Unicode_data = Unicode_data + ascii_text        

    return Unicode_data


# decoding the file
def Decode():
    Screen.destroy()
    DecScreen = Tk()
    DecScreen.title("Decode")
    DecScreen.geometry("500x500+300+300")
    DecScreen.config(bg="pink")
    def OpenFile():
        global FileOpen
        FileOpen=StringVar()
        FileOpen = askopenfilename(initialdir ="/Desktop",title="Select the File",filetypes=(("only jpeg files","*jpg"),("all type of files","*.*")))
        
    def Decoder():
        Message=stg.reveal(FileOpen)
        def decode(image):    
            arr = np.array(image)
            red = arr[..., 0]  # All Red values
            green = arr[..., 1]  # All Green values
            blue = arr[..., 2]  # All Blue values

            height,width = blue.shape
            total_size = height*width
            data = []
            bit_size = 0
            data_byte = ''

            if count < total_size:
                new_count = 0
                for i in range(height):
                    for j in range(width):
                        if new_count <= count:                    
                            if bit_size < 8:
                                data_byte = data_byte + str((blue[i][j] & 1))
                                bit_size+=1
                            else:
                                data.append(data_byte)                        
                                bit_size = 0
                                data_byte = '' 

                                data_byte = data_byte + str((blue[i][j] & 1))
                                bit_size+=1
                                
                            new_count+=1
                        else:
                            break

            elif count > total_size and count < 2*total_size:
                new_count = 0
                for i in range(height):
                    for j in range(width):                                    
                        if bit_size < 8:
                            data_byte = data_byte + str((blue[i][j] & 1))
                            bit_size+=1
                        else:
                            data.append(data_byte)                        
                            bit_size = 0
                            data_byte = '' 

                            data_byte = data_byte + str((blue[i][j] & 1))
                            bit_size+=1
                bit_size = 0
                data_byte = ''                                                        
                        
                for i in range(height):
                    for j in range(width):
                        if new_count <= count:                    
                            if bit_size < 8:
                                data_byte = data_byte + str((green[i][j] & 1))
                                bit_size+=1
                            else:
                                data.append(data_byte)                        
                                bit_size = 0
                                data_byte = '' 

                                data_byte = data_byte + str((green[i][j] & 1))
                                bit_size+=1
                                
                            new_count+=1
                        else:
                            break
            else: 
                new_count = 0
                for i in range(height):
                    for j in range(width):                                    
                        if bit_size < 8:
                            data_byte = data_byte + str((blue[i][j] & 1))
                            bit_size+=1
                        else:
                            data.append(data_byte)                        
                            bit_size = 0
                            data_byte = '' 

                            data_byte = data_byte + str((blue[i][j] & 1))
                            bit_size+=1
                bit_size = 0
                data_byte = ''

                for i in range(height):
                    for j in range(width):                                    
                        if bit_size < 8:
                            data_byte = data_byte + str((green[i][j] & 1))
                            bit_size+=1
                        else:
                            data.append(data_byte)                        
                            bit_size = 0
                            data_byte = '' 

                            data_byte = data_byte + str((green[i][j] & 1))
                            bit_size+=1
                bit_size = 0
                data_byte = ''                                                        
                        
                for i in range(height):
                    for j in range(width):
                        if new_count <= count:                    
                            if bit_size < 8:
                                data_byte = data_byte + str((red[i][j] & 1))
                                bit_size+=1
                            else:
                                data.append(data_byte)                        
                                bit_size = 0
                                data_byte = '' 

                                data_byte = data_byte + str((red[i][j] & 1))
                                bit_size+=1
                                
                            new_count+=1
                        else:
                            break    
            return data
        label3 = Label(text=Message)
        label3.place(relx=0.3,rely=0.3)
        
    SelectButton = Button(text="Select the file",command=OpenFile)
    SelectButton.place(relx=0.1,rely=0.4)
    EncodeButton=Button(text="Decode",command=Decoder)
    EncodeButton.place(relx=0.4,rely=0.5)


#encoding the file
def Encode():
    Screen.destroy()
    EncScreen = Tk()
    EncScreen.title("Encode")
    EncScreen.geometry("500x500+300+300")
    EncScreen.config(bg="yellow")
    label = Label(text="Confidential Message")
    label.place(relx=0.1,rely=0.2)
    entry=Entry()
    entry.place(relx=0.5,rely=0.2)
    label1 = Label(text="Name of the File")
    label1.place(relx=0.1,rely=0.3)
    SaveEntry = Entry()
    SaveEntry.place(relx=0.5,rely=0.3)

    def OpenFile():
        global FileOpen
        FileOpen=StringVar()
        FileOpen = askopenfilename(initialdir ="/Desktop",title="SelectFile",filetypes=(("only jpeg files","*jpg"),("all type of files","*.*")))

        label2 = Label(text=FileOpen)
        label2.place(relx=0.3,rely=0.3)

    def Encoder():
        Response= messagebox.askyesno("PopUp","Do you want to encode the image?")
        if Response == 1:
            stg.hide(FileOpen,SaveEntry.get()+".jpg",entry.get())
            def embed(image,data):
                # iterate the image pixels
                # store user input in LSB(least significant bit) of each pixels RGB depending on need
                # start with B then G then R..
            
                arr = np.array(image)
                # print(arr.shape) ...to see size of img
                
                # 3d array....2d pixel array with 3 channels
                red = arr[..., 0]  # All Red values
                green = arr[..., 1]  # All Green values
                blue = arr[..., 2]  # All Blue values
                
                # pixels can be odd or even    
                
                height,width = blue.shape
                incompBlue = True
                incompGreen = True
                incompRed = True

                blue[0][0] = 193
                blue[0][2] = 882
                i = 0
                j = -1
                global count
                c = 0
                for char in data:
                    for bit in char:  
                        count += 1
                        if incompBlue == True:
                            if i < height:
                                if j < width:                       
                                    j+=1     
                                if j >= width:
                                    i+=1
                                    j=0
                                # print("{0:b}".format(blue[i][j]))
                                # if bit of char is 1
                                
                                #print(i,j)
                                if i < height:
                                    if bit=='1':
                                        blue[i][j] = blue[i][j] | 1  #set the last bit to 1
                                    elif bit=='0':
                                        blue[i][j] = blue[i][j] & (blue[i][j] -1)   #set the last bit to 0
                                    c += 1  
                                else:
                                    incompBlue = False
                                    i = 0
                                    j = -1
                                
                                
                                # print("{0:b}".format(blue[i][j]))
                                # print('\n')
                
                            else:
                                incompBlue = False  
                                i = 0
                                j = -1                                                              
                            
                        if incompBlue == False and incompGreen == True:
                            if i < height:
                                if j < width:                        
                                    j+=1
                                if j >= width:
                                    i+=1
                                    j=0   
                                # print("{0:b}".format(green[i][j]))
                                # if bit of char is 1
                                # print("g",i,j)
                                if i < height:
                                    if bit=='1':
                                        green[i][j] = green[i][j] | 1  #set the last bit to 1
                                    elif bit=='0':
                                        green[i][j] = green[i][j] & (green[i][j] -1)   #set the last bit to 0
                                    c += 1
                                else:
                                    incompGreen = False
                                    i = 0
                                    j = -1                    
                                
                                # print("{0:b}".format(green[i][j]))
                                # print('\n')    
                            else:
                                incompGreen = False  
                                i = 0
                                j = -1
                        if incompBlue == False and incompGreen == False:
                            if i < height:
                                if j < width:                        
                                    j+=1
                                if j >= width:
                                    i+=1
                                    j=0   
                                # print("{0:b}".format(red[i][j]))
                                # if bit of char is 1
                                # print("r",i,j)
                                if i < height:
                                    if bit=='1':
                                        red[i][j] = red[i][j] | 1  #set the last bit to 1
                                    elif bit=='0':
                                        red[i][j] = red[i][j] & (red[i][j] -1)   #set the last bit to 0
                                    c += 1
                                else:
                                    incompRed = False  
                                    sys.exit("Choose a higher quality image")                     

                                # print("{0:b}".format(red[i][j]))
                                # print('\n')    
                            else:
                                incompRed = False  
                                i = 0
                                j = -1
                                break
                            
                if incompRed == False:
                    sys.exit("Choose a higher quality image")        

                w, h = image.size
                test = np.zeros((h, w, 3), dtype=np.uint8)
                
                #reconstructing image
                test[:,:,0] = red
                test[:,:,1] = green
                test[:,:,2] = blue

            messagebox.showinfo("Pop Up","Successfully Encoded")
        else:
            messagebox.showwarning("Pop Up","Unsuccessful, please try again")

    SelectButton = Button(text="Select the file",command=OpenFile)
    SelectButton.place(relx=0.1,rely=0.4)
    EncodeButton=Button(text="Encode",command=Encoder)
    EncodeButton.place(relx=0.4,rely=0.5)

#Initializing the screen
Screen = Tk()
Screen.title("Image Steganography")
Screen.geometry("300x300+300+300")
Screen.config(bg= "white")
#creating buttons
EncodeButton = Button(text="Encode",command=Encode)
EncodeButton.place(relx=0.3,rely=0.4)

DecodeButton = Button(text="Decode",command=Decode)
DecodeButton.place(relx=0.6,rely=0.4)

mainloop()