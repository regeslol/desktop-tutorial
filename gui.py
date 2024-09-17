Import tkinter as tk

From tkinter import messagebox, simpledialog, colorchooser

From tkcalendar import Calendar

Import models as aux



Class FinanceApp:

    Def __init__(self, root):

        Self.root = root

        Self.root.title(“Aplicativo de Finanças”)



        # Frame principal

        Self.main_frame = tk.Frame(root)

        Self.main_frame.pack(fill=”both”, expand=True)



        # Botões principais

        Self.create_main_buttons()



        # Armazenar as bolhas de cálculo

        Self.bubbles_frame = tk.Frame(self.main_frame)

        Self.bubbles_frame.pack(pady=10)



        # Frame para o calendário

        Self.calendar_frame = tk.Frame(self.main_frame)

        Self.calendar_frame.pack(pady=10)

        Self.create_calendar()



    Def create_main_buttons(self):

        Button_frame = tk.Frame(self.main_frame)

        Button_frame.pack(pady=10)



        Calc_button = tk.Button(button_frame, text=”Adicionar Cálculo Rápido”, command=self.add_quick_calc)

        Calc_button.grid(row=0, column=0, padx=5)



        Fixed_trans_button = tk.Button(button_frame, text=”Adicionar Transação Fixa”, command=self.add_fixed_transaction)

        Fixed_trans_button.grid(row=0, column=1, padx=5)



        Estimate_button = tk.Button(button_frame, text=”Calcular Produto Estimado”, command=self.calculate_estimate)

        Estimate_button.grid(row=0, column=2, padx=5)



    Def add_quick_calc(self):

        Expression = simpledialog.askstring(“Cálculo Rápido”, “Digite a expressão a ser calculada:”)

        If expression:

            Try:

                Result = eval(expression)

                Self.create_bubble(expression, result)

            Except Exception as e:

                Messagebox.showerror(“Erro”, f”Erro na expressão: {e}”)



    Def create_bubble(self, expression, result):

        Bubble_frame = tk.Frame(self.bubbles_frame, bg=”lightgrey”, padx=10, pady=5, bd=1, relief=”solid”)

        Bubble_frame.pack(pady=5, fill=”x”)



        Bubble_label = tk.Label(bubble_frame, text=f”{expression} = {result}”, bg=”lightgrey”)

        Bubble_label.pack(side=”left”, padx=5)



        Expand_button = tk.Button(bubble_frame, text=”Expandir”, command=lambda: self.expand_bubble(bubble_frame, expression, result))

        Expand_button.pack(side=”right”, padx=5)



    Def expand_bubble(self, bubble_frame, expression, result):

        Bubble_detail = tk.Toplevel(self.root)

        Bubble_detail.title(“Detalhes do Cálculo”)



        Detail_label = tk.Label(bubble_detail, text=f”{expression} = {result}”)

        Detail_label.pack(padx=10, pady=10)



        Color_button = tk.Button(bubble_detail, text=”Alterar Cor”, command=lambda: self.change_color(bubble_frame, bubble_detail))

        Color_button.pack(padx=10, pady=10)



    Def change_color(self, bubble_frame, bubble_detail):

        Color = colorchooser.askcolor()[1]

        If color:

            Bubble_frame.config(bg=color)

            For widget in bubble_frame.winfo_children():

                Widget.config(bg=color)

            Bubble_detail.config(bg=color)



    Def add_fixed_transaction(self):

        Desc = simpledialog.askstring(“Transação Fixa”, “Descrição:”)

        If desc:

            Try:

                Value = float(simpledialog.askstring(“Transação Fixa”, “Valor:”))

                Date = simpledialog.askstring(“Transação Fixa”, “Data (AAAA-MM-DD):”)

                Tipo = simpledialog.askstring(“Transação Fixa”, “Tipo (Lucro/Prejuízo):”)

                Aux.adicionar_transacao_fixa(desc, value, date, tipo)

                Messagebox.showinfo(“Sucesso”, “Transação Fixa Adicionada com Sucesso”)

            Except Exception as e:

                Messagebox.showerror(“Erro”, f”Erro ao adicionar transação: {e}”)



    Def create_calendar(self):

        Self.calendar = Calendar(self.calendar_frame, selectmode=”day”)

        Self.calendar.pack(pady=10)



    Def calculate_estimate(self):

        Selected_date = self.calendar.get_date()

        Result = aux.calcular_produto_estimado(selected_date)

        Messagebox.showinfo(“Produto Estimado”, f”Produto Estimado para {selected_date}: {result}”)



If __name__ == “__main__”:

    Root = tk.Tk()

    App = FinanceApp(root)

    Root.mainloop()

