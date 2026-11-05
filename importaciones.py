import logging
from abc import ABC, abstractmethod
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext

# Configuración del sistema de Logs 
logging.basicConfig(
    filename='app_errors.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
