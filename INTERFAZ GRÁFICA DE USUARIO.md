# ==========================================
# INTERFAZ GRÁFICA DE USUARIO 
# ==========================================
class AppSoftwareFJ:
    def __init__(self, root):
        self.root = root
        self.root.title("Software FJ - Integrated Management System (UNAD Phase 4)")
        self.root.geometry("820x620")
        self.root.config(bg="#f4f6f9")

        # Estilo visual de la interfaz
        style = ttk.Style()
        style.theme_use("clam")

        # Contenedor de pestañas (Notebook)
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)

        # Pestaña 1: Simulación de Operaciones
        self.frame_simulacion = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_simulacion, text=" Operations Simulation ")
        self.crear_pestana_simulacion()

        # Pestaña 2: Registro Interactivo de Clientes
        self.frame_interactivo = ttk.Frame(self.notebook)
        self.notebook.add(self.frame_interactivo, text=" Interactive Customer Registration ")
        self.crear_pestana_interactiva()

    def crear_pestana_simulacion(self):
        titulo = tk.Label(self.frame_simulacion, text="Automated 10-Operation Simulation (Software FJ)", font=("Arial", 12, "bold"), fg="#003865")
        titulo.pack(pady=10)

        btn_ejecutar = tk.Button(self.frame_simulacion, text="Run Full Simulation", bg="#003865", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5, command=self.ejecutar_simulacion_gui)
        btn_ejecutar.pack(pady=5)

        self.texto_consola = scrolledtext.ScrolledText(self.frame_simulacion, width=90, height=25, bg="#1e1e1e", fg="#00ff00", font=("Consolas", 9))
        self.texto_consola.pack(padx=10, pady=10, fill="both", expand=True)

    def ejecutar_simulacion_gui(self):
        self.texto_consola.delete(1.0, tk.END)
        self.texto_consola.insert(tk.END, "=== STARTING 10-OPERATION SIMULATION ===\n\n")
        
        operaciones_totales = 10
        for i in range(1, operaciones_totales + 1):
            self.texto_consola.insert(tk.END, f"--- Operation #{i} ---\n")
            try:
                if i == 1:
                    c1 = Cliente("C001", "Ana María Pérez", "ana.perez@email.com", "3104567890")
                    s1 = ReservaSala("S001", "North Executive Room", 150000.0, 10)
                    res1 = Reserva("R001", c1, s1)
                    msg = res1.confirmar()
                    self.texto_consola.insert(tk.END, f"{msg}\nTotal cost with taxes: ${s1.calcular_costo(descuento=0.1)}\n")

                elif i == 2:
                    self.texto_consola.insert(tk.END, "Attempting to register customer with invalid email...\n")
                    Cliente("C002", "Carlos Ruiz", "invalid-email.com", "3201234567")

                elif i == 3:
                    c3 = Cliente("C003", "Lucía Gómez", "lucia.gomez@email.com", "3009876543")
                    s3 = AlquilerEquipo("S002", "HP Server Rack", 80000.0, 5)
                    res3 = Reserva("R002", c3, s3)
                    msg = res3.confirmar()
                    self.texto_consola.insert(tk.END, f"{msg}\nRental cost: ${s3.calcular_costo(seguro=25000.0)}\n")

                elif i == 4:
                    self.texto_consola.insert(tk.END, "Attempting to create service with negative cost...\n")
                    AlquilerEquipo("S003", "Cisco Switch", -500.0, 2)

                elif i == 5:
                    c5 = Cliente("C004", "Andrés Felipe Marín", "andres.marin@email.com", "3112223344")
                    s5 = AsesoriaEspecializada("S003", "AWS Cloud Architecture", 120000.0, 4)
                    res5 = Reserva("R003", c5, s5)
                    msg = res5.confirmar()
                    self.texto_consola.insert(tk.END, f"{msg}\nConsulting cost: ${s5.calcular_costo(bono_especial=50000.0)}\n")

                elif i == 6:
                    self.texto_consola.insert(tk.END, "Attempting to register customer with invalid phone number...\n")
                    Cliente("C005", "Sofía Castro", "sofia@email.com", "ABC12345")

                elif i == 7:
                    c7 = Cliente("C006", "Jorge Higuita", "jorge@email.com", "3123334455")
                    s7 = ReservaSala("S004", "Creative Room", 100000.0, 6)
                    res7 = Reserva("R004", c7, s7)
                    self.texto_consola.insert(tk.END, f"{res7.confirmar()}\n")
                    self.texto_consola.insert(tk.END, f"{res7.confirmar()}\n") # Doble confirmación

                elif i == 8:
                    self.texto_consola.insert(tk.END, "Creating room with zero capacity...\n")
                    reserva_falsa = ReservaSala("S005", "Auditorium Room", 200000.0, 0)
                    reserva_falsa.validar_parametros()

                elif i == 9:
                    c9 = Cliente("C007", "Mariana Ríos", "mariana@email.com", "3156667788")
                    s9 = AlquilerEquipo("S006", "Laser Projector", 50000.0, 1)
                    res9 = Reserva("R005", c9, s9)
                    self.texto_consola.insert(tk.END, f"[INFO] Reservation {res9.id_reserva} successfully cancelled.\n")

                elif i == 10:
                    self.texto_consola.insert(tk.END, "Registering customer with a very short name...\n")
                    Cliente("C008", "Al", "al@email.com", "3189990000")

            except (SoftwareFJException, ValueError, TypeError) as ex:
                logging.warning(f"Exception caught in operation #{i}: {type(ex).__name__} - {ex}")
                self.texto_consola.insert(tk.END, f"[CONTROLLED EXCEPTION] Failed safely -> {ex}\n")
            else:
                self.texto_consola.insert(tk.END, f"[STATUS] Operation #{i} completed successfully.\n")
            finally:
                self.texto_consola.insert(tk.END, f"--- End of Operation #{i} cycle ---\n\n")

        self.texto_consola.insert(tk.END, "=== SIMULATION COMPLETED. CHECK 'app_errors.log' ===\n")

    def crear_pestana_interactiva(self):
        lbl_info = tk.Label(self.frame_interactivo, text="Customer Data Validation Test", font=("Arial", 12, "bold"), fg="#003865")
        lbl_info.pack(pady=15)

        form_frame = tk.Frame(self.frame_interactivo, bg="#f4f6f9")
        form_frame.pack(pady=5)

        tk.Label(form_frame, text="Customer ID:", font=("Arial", 10), bg="#f4f6f9").grid(row=0, column=0, sticky="w", pady=5, padx=5)
        self.ent_id = tk.Entry(form_frame, width=35)
        self.ent_id.grid(row=0, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Full Name:", font=("Arial", 10), bg="#f4f6f9").grid(row=1, column=0, sticky="w", pady=5, padx=5)
        self.ent_nombre = tk.Entry(form_frame, width=35)
        self.ent_nombre.grid(row=1, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Email Address:", font=("Arial", 10), bg="#f4f6f9").grid(row=2, column=0, sticky="w", pady=5, padx=5)
        self.ent_email = tk.Entry(form_frame, width=35)
        self.ent_email.grid(row=2, column=1, pady=5, padx=5)

        tk.Label(form_frame, text="Phone (digits only):", font=("Arial", 10), bg="#f4f6f9").grid(row=3, column=0, sticky="w", pady=5, padx=5)
        self.ent_tel = tk.Entry(form_frame, width=35)
        self.ent_tel.grid(row=3, column=1, pady=5, padx=5)

        btn_validar = tk.Button(self.frame_interactivo, text="Register & Validate Customer", bg="#28a745", fg="white", font=("Arial", 10, "bold"), padx=10, pady=5, command=self.validar_cliente_interactivo)
        btn_validar.pack(pady=20)

    def validar_cliente_interactivo(self):
        try:
            cli = Cliente(
                self.ent_id.get(),
                self.ent_nombre.get(),
                self.ent_email.get(),
                self.ent_tel.get()
            )
            messagebox.showinfo("Success", f"Customer registered successfully:\n{cli.obtener_detalle()}")
        except SoftwareFJException as e:
            logging.warning(f"Interactive validation error: {e}")
            messagebox.showerror("Validation Error (Exception)", str(e))
        except Exception as ex:
            messagebox.showerror("Unexpected Error", str(ex))


if __name__ == "__main__":
    root = tk.Tk()
    app = AppSoftwareFJ(root)
    root.mainloop()
