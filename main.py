import customtkinter as ctk
import qrcode
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk


ctk.set_appearance_mode("Dark") 
ctk.set_default_color_theme("green")
app = ctk.CTk()
app.title("Gerador de QR Code")
app.geometry("400x550")
app.resizable(False, False)

def gerar_qrcode():
    texto = entrada.get()
    if not texto:
        messagebox.showwarning("Aviso", "Digite algo antes de gerar.")
        return

    qr = qrcode.make(texto)
    qr.save("qrcode_temp.png")
    img = Image.open("qrcode_temp.png").resize((200, 200))
    img_tk = ImageTk.PhotoImage(img)
    imagem_label.configure(image=img_tk)
    imagem_label.image = img_tk

def salvar_qrcode():
    texto = entrada.get()
    if not texto:
        messagebox.showwarning("Aviso", "Nada para salvar.")
        return
    caminho = filedialog.asksaveasfilename(defaultextension=".png")
    if caminho:
        qrcode.make(texto).save(caminho)
        messagebox.showinfo("Salvo", f"QR Code salvo em: {caminho}")


titulo = ctk.CTkLabel(app, text="Gerador de QR Code", font=ctk.CTkFont(size=20, weight="bold"))
titulo.pack(pady=20)

entrada = ctk.CTkEntry(app, width=300, placeholder_text="Digite texto ou URL")
entrada.pack(pady=10)

botao_gerar = ctk.CTkButton(app, text="Gerar QR Code", command=gerar_qrcode)
botao_gerar.pack(pady=10)

botao_salvar = ctk.CTkButton(app, text="Salvar QR Code", command=salvar_qrcode)
botao_salvar.pack(pady=5)

imagem_label = ctk.CTkLabel(app, text="")
imagem_label.pack(pady=20)

app.mainloop()
