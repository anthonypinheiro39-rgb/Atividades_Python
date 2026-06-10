import tkinter as tk
from tkinter import scrolledtext
import re

# =========================
# IDENTIFICADOR DE LINGUAGEM
# =========================

linguagens = {
    "Python": [
        r'^\s*def\s+\w+\(.*\):',
        r'^\s*print\(.*\)',
        r'^\s*import\s+\w+',
        r'^\s*if\s+.*:',
        r'^\s*for\s+\w+\s+in\s+.*:',
        r'^\s*#.*'
    ],

    "JavaScript": [
        r'^\s*function\s+\w+\(.*\)\s*\{?',
        r'^\s*console\.log\(.*\);?',
        r'^\s*(let|const|var)\s+\w+',
        r'=>',
        r'^\s*if\s*\(.*\)\s*\{?'
    ],

    "Java": [
        r'^\s*public\s+class\s+\w+',
        r'^\s*public\s+static\s+void\s+main',
        r'^\s*System\.out\.println\(.*\);',
        r'^\s*(int|double|String|boolean)\s+\w+\s*=',
        r'^\s*import\s+java\.'
    ],

    "C": [
        r'^\s*#include\s*<.*>',
        r'^\s*int\s+main\s*\(.*\)',
        r'^\s*printf\(.*\);',
        r'^\s*scanf\(.*\);',
        r'^\s*(int|float|char|double)\s+\w+\s*=',
    ],

    "PHP": [
        r'^\s*<\?php',
        r'^\s*echo\s+.*;',
        r'^\s*\$\w+',
        r'^\s*function\s+\w+\(.*\)\s*\{',
    ]
}


def identificar_linguagem(codigo):
    pontuacao = {}

    for linguagem, padroes in linguagens.items():
        pontos = 0

        for padrao in padroes:
            if re.search(padrao, codigo, re.MULTILINE):
                pontos += 1

        pontuacao[linguagem] = pontos

    maior_pontuacao = max(pontuacao.values())

    if maior_pontuacao == 0:
        return "Linguagem não identificada", pontuacao

    provaveis = []

    for linguagem, pontos in pontuacao.items():
        if pontos == maior_pontuacao:
            provaveis.append(linguagem)

    if len(provaveis) == 1:
        return provaveis[0], pontuacao
    else:
        return "Ambíguo: " + ", ".join(provaveis), pontuacao


# =========================
# FUNÇÃO DO BOTÃO
# =========================

def analisar():
    codigo = campo_codigo.get("1.0", tk.END)

    resultado, pontuacao = identificar_linguagem(codigo)

    resultado_label.config(
        text=f"✓ Linguagem Detectada: {resultado}"
    )

    texto = ""

    for linguagem, pontos in pontuacao.items():
        texto += f"{linguagem}: {pontos} ponto(s)\n"

    pontuacao_box.config(state="normal")
    pontuacao_box.delete("1.0", tk.END)
    pontuacao_box.insert(tk.END, texto)
    pontuacao_box.config(state="disabled")


# =========================
# INTERFACE
# =========================

BG = "#0F172A"
CARD = "#1E293B"
AZUL = "#3B82F6"
AZUL_HOVER = "#2563EB"
TEXTO = "#F8FAFC"
VERDE = "#22C55E"

janela = tk.Tk()
janela.title("Detector de Linguagem")
janela.geometry("900x650")
janela.minsize(450, 500)
janela.configure(bg=BG)

janela.grid_rowconfigure(1, weight=1)
janela.grid_columnconfigure(0, weight=1)

titulo = tk.Label(
    janela,
    text="Detector de Linguagem de Programação",
    font=("Segoe UI", 24, "bold"),
    bg=BG,
    fg=AZUL
)

titulo.grid(row=0, column=0, pady=20)

frame = tk.Frame(
    janela,
    bg=CARD,
    highlightbackground="#334155",
    highlightthickness=1
)

frame.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=20,
    pady=10
)

frame.grid_rowconfigure(1, weight=1)
frame.grid_columnconfigure(0, weight=1)

lbl = tk.Label(
    frame,
    text="Cole seu código abaixo:",
    font=("Segoe UI", 12),
    bg=CARD,
    fg=TEXTO
)

lbl.grid(row=0, column=0, sticky="w", padx=15, pady=10)

campo_codigo = scrolledtext.ScrolledText(
    frame,
    font=("Consolas", 13),
    wrap=tk.WORD,
    bg="#0B1220",
    fg="#F8FAFC",
    insertbackground="white",
    relief="flat",
    borderwidth=0
)

campo_codigo.grid(
    row=1,
    column=0,
    sticky="nsew",
    padx=15,
    pady=10
)

btn = tk.Button(
    frame,
    text="🔍 Analisar Código",
    command=analisar,
    bg=AZUL,
    fg="white",
    activebackground=AZUL_HOVER,
    activeforeground="white",
    relief="flat",
    cursor="hand2",
    font=("Segoe UI", 12, "bold"),
    pady=10
)

btn.grid(row=2, column=0, pady=15)

resultado_label = tk.Label(
    frame,
    text="✓ Linguagem Detectada:",
    font=("Segoe UI", 16, "bold"),
    bg=CARD,
    fg=VERDE
)

resultado_label.grid(row=3, column=0, pady=10)

pontuacao_box = tk.Text(
    frame,
    height=8,
    bg="#0B1220",
    fg="#F8FAFC",
    insertbackground="white",
    relief="flat",
    borderwidth=0,
    font=("Segoe UI", 11)
)

pontuacao_box.grid(
    row=4,
    column=0,
    sticky="ew",
    padx=15,
    pady=10
)

pontuacao_box.config(state="disabled")

janela.mainloop()